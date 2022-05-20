from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Personal Navigator</h1> <a href="https://github.com/Chinmay1292">Github</a> <br> <a href="https://www.linkedin.com/in/chinmay-chougule-478909213/">LinkedIn</a>''')

def about(request):
    return HttpResponse("About")

def text(request):
    file = open("1.txt")
    return HttpResponse(file.read())