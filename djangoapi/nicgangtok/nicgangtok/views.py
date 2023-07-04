from django.http import HttpResponse
def home_page(request):

    print("home page requested")
    friends=[
        'sneha',
        'riya',
        'sujata',
    ]
    

    return HttpResponse(friends)

    