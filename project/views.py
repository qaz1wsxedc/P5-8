from django.shortcuts import render

def main_page(request):
    return render(request, 'main\Main.html')

def research_page(request):
    return render(request, 'main\Research.html')

def author_page(request):
    return render(request, 'main\Author.html')