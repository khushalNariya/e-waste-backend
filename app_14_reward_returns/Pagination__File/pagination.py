from rest_framework.pagination import PageNumberPagination

# Custom pagination class for returns list view
class RewardReturn_Pagination(PageNumberPagination): 
    page_size = 5                           
    page_query_param = 'p'                
    page_size_query_param = 'page_size'     
    max_page_size = 100  
