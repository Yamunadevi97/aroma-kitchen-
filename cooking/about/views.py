from django.shortcuts import render
def home(request):
	return render(request, 'hom/home.html')
# Create your views here.
