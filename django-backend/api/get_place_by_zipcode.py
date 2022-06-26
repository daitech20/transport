import requests

def get_place(ZIP_CODE):
    api_get_place_by_zipcode = 'https://ziptasticapi.com/' + str(ZIP_CODE)
    result = requests.get(api_get_place_by_zipcode)

    return result.json()
