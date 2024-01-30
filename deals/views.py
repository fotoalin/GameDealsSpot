import requests
from django.shortcuts import render

from deals.api.games import get_deals, get_games_by_name


def index(request):
    return render(request, "deals/index.html")


def deals(request):
    deals = get_deals()
    context = {
        "deals": deals,
    }
    # if request.htmx:
    #     return render(request, "deals/snippets/deals_partial.html", context)

    return render(request, "deals/deals.html", context)


def filter(request):
    return render(request, "deals/filter.html")


def search(request):
    search_query = request.GET.get("search", "")

    if request.htmx:
        if request.method == "POST":
            search_query = request.POST.get("search", "")
        elif request.method == "GET":
            search_query = request.GET.get("search", "")

        deals = get_deals(search_query)
        # games = get_games_by_name(search_query)

        context = {
            "deals": deals,
            # "games": games,
        }

        template = "deals/snippets/deals_partial.html"
        return render(request, template, context)
    else:
        deals = get_deals()

        context = {
            "deals": deals,
        }

        template = "deals/deals.html"
        return render(request, template, context)


def contact(request):
    return render(request, "deals/contact.html")
