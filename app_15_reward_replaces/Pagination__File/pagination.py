from rest_framework.pagination import PageNumberPagination

# Custom pagination for replace request list views
class RewardReplace_Pagination(PageNumberPagination):
    page_size = 5                       # Default rows per page
    page_query_param = 'p'              # URL param: ?p=2
    page_size_query_param = 'page_size' # URL param: ?page_size=10
    max_page_size = 100                 # Max allowed per page
