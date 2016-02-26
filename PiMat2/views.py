from django.shortcuts import render

def post_list(request):
    return render(request, 'PiMat2/homepage.html', {})
