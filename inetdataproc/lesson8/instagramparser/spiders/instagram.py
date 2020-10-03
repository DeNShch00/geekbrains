import scrapy
from scrapy.http import HtmlResponse
import re
import json
from functools import partial

from instagramparser.instarequests import AuthRequest, MainPageRequest, FollowersRequest, FollowingRequest
from instagramparser.instapaginators import FollowersPaginator, FollowingPaginator


credentials = {
    'login': '123',
    'enc_password': '456'
}


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']

    def __init__(self, target_users):
        self.target_users = target_users
        super().__init__()

    def parse(self, response: HtmlResponse, **kwargs):
        yield AuthRequest(credentials['login'], credentials['enc_password'],
                          self.fetch_csrf_token(response.text)).do(self.auth_complete)

    def auth_complete(self, response: HtmlResponse):
        data = json.loads(response.text)
        if data['authenticated']:
            for user in self.target_users:
                yield self.process_user(user, response)

    def process_user(self, name: str, response: HtmlResponse):
        profile = {'name': name}
        return MainPageRequest(name).do(response, self.process_user_main_page, profile)

    def process_user_main_page(self, response: HtmlResponse):
        profile = response.meta
        profile['id'] = self.fetch_user_id(response.text, profile['name'])
        callback = partial(self.process_user_follow, paginator_class=FollowersPaginator, request_class=FollowersRequest)
        yield FollowersRequest(profile['id']).do(response, callback, profile)
        callback = partial(self.process_user_follow, paginator_class=FollowingPaginator, request_class=FollowingRequest)
        yield FollowingRequest(profile['id']).do(response, callback, profile)

    def process_user_follow(self, response: HtmlResponse, paginator_class, request_class):
        profile = response.meta
        data = json.loads(response.text)
        paginator = paginator_class(data)
        if paginator.has_next_page:
            request = paginator.next_page(request_class(profile['id']))
            callback = partial(self.process_user_follow, paginator_class=paginator_class, request_class=request_class)
            yield request.do(response, callback, profile)

    @staticmethod
    def fetch_csrf_token(text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    @staticmethod
    def fetch_user_id(text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')
