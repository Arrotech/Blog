from django.shortcuts import render


# Create your views here.
def home(request):
    """Landing page."""
    return render(request, 'myblog/index.html', {})
