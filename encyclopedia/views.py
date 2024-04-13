from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse

from . import util

from .forms import NewEntryForm

import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "entry": util.html_to_markdown(entry)},
        )

    else:
        return render(
            request,
            "encyclopedia/error.html",
            {"message": f'"{title}" Not Found In Wiki Entries'},
        )


def search(request):
    if request.method == "GET":
        query = request.GET.get("query")
        entries = util.list_entries()
        matches = [entry for entry in entries if query.lower() in entry.lower()]
        exact_match = [entry for entry in entries if query.lower() == entry.lower()]

        if exact_match:
            return HttpResponseRedirect(reverse("entry", kwargs={"title": exact_match}))

        elif matches:
            return render(
                request,
                "encyclopedia/search.html",
                {"matches": matches, "query": query},
            )
        else:
            return render(
                request,
                "encyclopedia/error.html",
                {"message": f'"{query}" Not Found in Wiki Entries'},
            )
    else:
        return redirect(reverse("index"))


def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(
                    request,
                    "encyclopedia/error.html",
                    {"message": "Entry Already Exists in Wiki", "title": title},
                )
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(
                    reverse("encyclopedia:entry", kwargs={"title": title})
                )
        else:
            return render(request, "encyclopedia/new.html", {"form": form})
    else:
        form = NewEntryForm()
        return render(request, "encyclopedia/new.html", {"form": form})


def edit(request, title):
    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():
            new_content = form.cleaned_data["content"]
            print(new_content)
            util.save_entry(title, new_content)
            return HttpResponseRedirect(
                reverse("encyclopedia:entry", kwargs={"title": title})
            )
        else:
            return render(
                request, "encyclopedia/edit.html", {"form": form, "title": title}
            )

    else:
        form = NewEntryForm(initial={"title": title, "content": util.get_entry(title)})
        form.fields["title"].widget.attrs["readonly"] = True
        return render(request, "encyclopedia/edit.html", {"form": form, "title": title})


def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect(reverse("encyclopedia:entry", kwargs={"title": random_entry}))
