class NormalizeDoubleSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Normalize double slashes in request paths to support both trailing-slash and no-trailing-slash base URLs
        if '//' in request.path_info:
            request.path_info = request.path_info.replace('//', '/')
        return self.get_response(request)
