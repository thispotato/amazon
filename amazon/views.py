from django.shortcuts import render

def get_object_or_404(request):
    page_title = 'This page was not found'
    return render(request, '404.html', locals()) 