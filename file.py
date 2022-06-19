import requests
import json

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": "3f08ed03a7msh2bb88890105babcp1aeff4jsnb6cf585b978d",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response = json.loads(requests.request("GET", url, headers=headers).text)

img_url = response['icon_url']
with open("img_url.png", "wb") as file:
    picture_response = requests.get(img_url)
    file.write(picture_response.content)