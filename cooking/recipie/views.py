from django.shortcuts import render
def pizza(request):
	return render (request,'rec/pizza.html')
def burger(request):
	return render (request,'rec/burger.html')
def noodles(request):
	return render (request,'rec/noodles.html')
def sandwich(request):
	return render (request,'rec/sandwich.html')
def gravy(request):
	return render (request,'rec/gravy.html')
def soup(request):
	return render (request,'rec/soup.html')
def homepage(request):
	return render(request,'index.html')

# Create your views here.
