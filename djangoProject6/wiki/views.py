from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import wikipedia
from django.shortcuts import render

def wikiSearch(request):
    if request.method =="POST":
        term = request.POST['term']
        try:
            definition = wikipedia.summary(term)
        except:
            return HttpResponse("Please search for new term")
        return render(request, "wiki/index.html", {"definition": definition})
    return render(request, "wiki/index.html")


