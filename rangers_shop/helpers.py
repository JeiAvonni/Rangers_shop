import requests
import requests_cache
import json
import decimal


# Setup our API cache location ( this will be our temporary database storing our api calls)
requests_cache.install_cache('image_cache', backend='sqlite')




def get_image(search):
    # 4 parts to every api
    # url required
    # queries/paremeters Optional
    # headers/authorization
    # body/posting optional

    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
    	"X-RapidAPI-Key": "b226938cdamsh247c1449ae911b5p14ba56jsna97b793eae8c",
    	"X-RapidAPI-Host": "google-search72.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    data = (response.json())
    img_url = data['items'][0]['originalImageUrl']

    if 'items' in data.keys():
        img_url = data['items'][0]['originalImageUrl']

    return img_url

# ADD THIS IMPORT TO THE TOP OF THE PAGE
import decimal

# THIS GOES BELOW the get_image() method
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it