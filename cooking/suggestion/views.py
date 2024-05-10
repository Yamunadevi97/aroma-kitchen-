from django.shortcuts import render
from suggestion.models import cus
from suggestion.forms import cusModelForm

def suggestion(request):
	form=cusModelForm
	cusform= {'form':form}
	if request.method=="POST":
		form=cusModelForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'sug/suggestion.html',cusform)


