import requests


def get_deals(search_query: str = None) -> list:
    # [  {
    #     "internalName": "DEUSEXHUMANREVOLUTIONDIRECTORSCUT",
    #     "title": "Deus Ex: Human Revolution - Director's Cut",
    #     "metacriticLink": "/game/pc/deus-ex-human-revolution---directors-cut",
    #     "dealID": "HhzMJAgQYGZ%2B%2BFPpBG%2BRFcuUQZJO3KXvlnyYYGwGUfU%3D",
    #     "storeID": "1",
    #     "gameID": "102249",
    #     "salePrice": "2.99",
    #     "normalPrice": "19.99",
    #     "isOnSale": "1",
    #     "savings": "85.042521",
    #     "metacriticScore": "91",
    #     "steamRatingText": "Very Positive",
    #     "steamRatingPercent": "92",
    #     "steamRatingCount": "17993",
    #     "steamAppID": "238010",
    #     "releaseDate": 1382400000,
    #     "lastChange": 1621536418,
    #     "dealRating": "9.6",
    #     "thumb": "https://cdn.cloudflare.steamstatic.com/steam/apps/238010/capsule_sm_120.jpg?t=1619788192"
    #   },
    # ]

    # CheapShark API docs:
    # https://apidocs.cheapshark.com/#b9b738bf-2916-2a13-e40d-d05bccdce2ba

    base_url = "https://www.cheapshark.com/api/1.0"

    if search_query is None:
        url = f"{base_url}/deals"
    else:
        url = f"{base_url}/deals?title={search_query}"

    response = requests.get(url, params={"limit": 5})
    deals = response.json() if response.status_code == 200 else []
    return deals


def get_games_by_name(search_query: str = None) -> list:
    # [
    #   {
    #     "gameID": "612",
    #     "steamAppID": null,
    #     "cheapest": "15.95",
    #     "cheapestDealID": "0f%2B4gT2VVUn4UcmFzPxXnuqoXKAOYoJ5mpFZRWNyohc%3D",
    #     "external": "LEGO Batman",
    #     "internalName": "LEGOBATMAN",
    #     "thumb": "https://cdn.fanatical.com/production/product/400x225/105f34ca-7757-47ad-953e-7df7f016741e.jpeg"
    #   },
    # ]

    # CheapShark API docs:
    # https://apidocs.cheapshark.com/#b9b738bf-2916-2a13-e40d-d05bccdce2ba

    response = requests.get("https://www.cheapshark.com/api/1.0/games")
    games = response.json() if response.status_code == 200 else []
    return games
