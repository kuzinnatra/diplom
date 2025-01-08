from rest_framework.pagination import PageNumberPagination

class BookPaginator(PageNumberPagination):
    """Пагинатор для книг"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10

class AuthorPaginator(PageNumberPagination):
    """Пагинатор для Авторов"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10