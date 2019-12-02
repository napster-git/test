#lets create my first view

from django.http import HttpResponse

def my_view(request):
    import pdb; pdb.set_trace()
    return  HttpResponse("First Hello World!!")

