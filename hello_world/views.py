from django.shortcuts import render

"""
When this function is called, it will render an HTML file called hello_world.html.
This file must be created beforehand
"""
def hello_world(request):
    """
    request: This object is an HttpRequestObject that is created whenever a page is loaded.
    It contains information about the request, such as the method, which can take several values including GET and POST.
    """
    return render(request, 'hello_world.html', {})
