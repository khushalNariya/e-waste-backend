from rest_framework.pagination import PageNumberPagination

# -------------------- Local (use) -----------------

# --- Custom Pagination Class ------

# ---- (Type - 1) ---> PageNumberPagination
class user__Pagination(PageNumberPagination): 
    page_size = 5                           # Default records per page ( http://127.0.0.1:8000/student_Api/?page=4 )
    page_query_param = 'p'                # Change "page" to "p" (?p=2)
   # Enable client to send limit
    page_size_query_param = 'page_size'     # Allow client to control page size (?size=10)
    max_page_size = 100  

