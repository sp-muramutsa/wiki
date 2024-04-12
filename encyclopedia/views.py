from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse 

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })

    else: 
        return render(request, "encyclopedia/404.html", {
            "title": title
        })
    
def search(request):
    if request.method == "GET":
        query = request.GET.get("query")
        entries = util.list_entries()
        matches = [entry for entry in entries if query.lower() in entry.lower()]
        exact_match = [entry for entry in entries if query.lower() == entry.lower()]

        print(matches)
        if exact_match:
            return HttpResponseRedirect(reverse("entry", kwargs={"title": exact_match}))
        
        elif matches:
            return render(request, "encyclopedia/search.html", {
                "matches": matches,
                "query": query
            })
    else:
        return redirect(reverse("index"))
            