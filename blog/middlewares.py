from django.shortcuts import HttpResponse

def my_middleware(get_response):
    print("One time initialization")
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function


class my_middleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization 2")

    def __call__(self, request):
        print("This is before view 2")
        response = self.get_response(request)
        #response = HttpResponse("Go back")
        print("This is after view 2")
        return response


class my_middleware3:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization 3")

    def __call__(self, request):
        print("This is before view 3")
        response = self.get_response(request)
        print("This is after view 3")
        return response


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print("This is Process View - Before View")
        #return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process Template Response")
        response.context_data['name'] = 'Mayank'
        return response
