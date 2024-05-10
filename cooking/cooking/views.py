def recipies(request):
	return render(request, 'ho/recipie.html')
def home(request):
	return render(request, 'ho/home.html')
def suggestion(request):
	return render(request,'sug/suggestion.html')