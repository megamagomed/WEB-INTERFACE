import requests
import json

import requests

url = "https://sudoku-all-purpose-pro.p.rapidapi.com/sudoku"

querystring = {"create":"32","output":"raw"}

headers = {
	"X-RapidAPI-Key": "3f08ed03a7msh2bb88890105babcp1aeff4jsnb6cf585b978d",
	"X-RapidAPI-Host": "sudoku-all-purpose-pro.p.rapidapi.com"
}
def response_function():
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)
	sudoku_task = json.loads(response.text)['output']['raw_data']
	return sudoku_task
response_function()