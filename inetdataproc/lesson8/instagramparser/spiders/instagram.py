import scrapy
from scrapy.http import HtmlResponse
import re
import json

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
        yield FollowersRequest(profile['id']).do(response, self.process_user_followers, profile)
        yield FollowingRequest(profile['id']).do(response, self.process_user_following, profile)

    def process_user_followers(self, response: HtmlResponse):
        profile = response.meta
        data = json.loads(response.text)
        paginator = FollowersPaginator(data)
        if paginator.has_next_page:
            request = paginator.next_page(FollowersRequest(profile['id']))
            yield request.do(response, self.process_user_followers, profile)

    def process_user_following(self, response: HtmlResponse):
        profile = response.meta
        data = json.loads(response.text)
        paginator = FollowingPaginator(data)
        if paginator.has_next_page:
            request = paginator.next_page(FollowingRequest(profile['id']))
            yield request.do(response, self.process_user_following, profile)

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
