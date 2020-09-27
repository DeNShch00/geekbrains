from instagramparser.instarequests import _UserPagedRequest


class _Paginator:
    root_edge = ''

    def __init__(self, current_page_json: dict):
        page_info = current_page_json['data']['user'][self.root_edge]['page_info']
        self.has_next_page = page_info['has_next_page']
        if self.has_next_page:
            self.cursor = page_info['end_cursor']

    def next_page(self, request: _UserPagedRequest):
        if self.has_next_page:
            request.cursor = self.cursor

        return request


class PostsPaginator(_Paginator):
    root_edge = 'edge_owner_to_timeline_media'


class FollowersPaginator(_Paginator):
    root_edge = 'edge_followed_by'


class FollowingPaginator(_Paginator):
    root_edge = 'edge_follow'
