from bookstore.main.views import error_404, Error404View


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return Error404View.as_view()(request)

        # if response.status_code == 404:
        #     return error_404(request)

        return request
    return middleware
