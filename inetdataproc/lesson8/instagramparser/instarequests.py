import scrapy
from scrapy.http import HtmlResponse, Request, FormRequest

from urllib.parse import urlencode


class _InstaGraphqlRequest:
    service_url = 'https://www.instagram.com/graphql/query/'
    query_id = ''

    def do(self, response: HtmlResponse, callback, meta: dict = None, **query_vars) -> Request:
        url = f'{self.service_url}?query_hash={self.query_id}&{urlencode(query_vars)}'
        return response.follow(url, callback=callback, meta=meta)


class _UserRequest(_InstaGraphqlRequest):
    def __init__(self, user_id: str):
        self.user_id = user_id
        super().__init__()

    def do(self, response: HtmlResponse, callback, meta: dict = None, **query_vars) -> Request:
        query_vars['id'] = self.user_id
        return super().do(response, callback, meta, **query_vars)


class _UserPagedRequest(_UserRequest):
    def __init__(self, user_id: str, cursor: str = None, page_items_count: int = 12):
        self.cursor = cursor
        self.page_items_count = page_items_count
        super().__init__(user_id)

    def do(self, response: HtmlResponse, callback, meta: dict = None, **query_vars) -> Request:
        query_vars['first'] = self.page_items_count
        if self.cursor:
            query_vars['after'] = self.cursor
        return super().do(response, callback, meta, **query_vars)


class _FollowRequest(_UserPagedRequest):
    def __init__(self, user_id: str, cursor: str = None, page_items_count: int = 12,
                 include_reel: bool = True, fetch_mutual: bool = False):
        self.include_reel = include_reel
        self.fetch_mutual = fetch_mutual
        super().__init__(user_id, cursor, page_items_count)

    def do(self, response: HtmlResponse, callback, meta: dict = None, **query_vars) -> Request:
        query_vars['include_reel'] = self.include_reel
        query_vars['fetch_mutual'] = self.fetch_mutual
        return super().do(response, callback, meta, **query_vars)


class PostsRequest(_UserPagedRequest):
    query_id = 'eddbde960fed6bde675388aac39a3657'


class FollowersRequest(_FollowRequest):
    query_id = 'c76146de99bb02f6415203be841dd25a'


class FollowingRequest(_FollowRequest):
    query_id = 'd04b0a864b4b54837c0d870b0e77e076'


class AuthRequest:
    service_url = 'https://www.instagram.com/accounts/login/ajax/'

    def __init__(self, login: str, encrypted_password: str, token: str):
        self.login = login
        self.encrypted_password = encrypted_password
        self.token = token

    def do(self, callback, meta: dict = None) -> FormRequest:
        return scrapy.FormRequest(
            self.service_url,
            method='POST',
            callback=callback,
            formdata={'username': self.login, 'enc_password': self.encrypted_password},
            headers={'X-CSRFToken': self.token},
            meta=meta
        )


class MainPageRequest:
    service_url = 'https://www.instagram.com/'

    def __init__(self, user_name: str):
        self.user_name = user_name

    def do(self, response: HtmlResponse, callback, meta: dict = None) -> Request:
        return response.follow(self.service_url + self.user_name, callback=callback, meta=meta)
