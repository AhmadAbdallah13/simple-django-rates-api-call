import requests

def getLatestRates():
    # payload = {'base': 'USD', 'symbols': 'GBP'}
    # response1 = requests.get("https://api.exchangeratesapi.io/latest",params=payload)
    response2 = requests.get("https://api.exchangeratesapi.io/latest")
    context = {
        'latest' : response2.json()
    }
    return context


def getRatesInYear(year:int, month:int, day:int):
    response = requests.get(f"https://api.exchangeratesapi.io/{year}-{month}-{day}")
    context = {
        'year': response.json(),
    }
    return context

def getSpecificExchangeRates(base:str, sym:str):
    payload = {'base': base, 'symbols': sym}
    response = requests.get("https://api.exchangeratesapi.io/latest",params=payload)
    context = {
        'compare' : response.json()
    }
    return context