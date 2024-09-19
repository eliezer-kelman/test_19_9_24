import requests


def get_players(season):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}"
    response = requests.request('GET', url)
    return response.json()
