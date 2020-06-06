import requests
import json

def request(line_userid):
	token = 'gNpYN4}-FZJ$weWvtyVFX0Xw9(F#n=5O'
	url = 'https://lab.krai.io/modules/user/api'
	r = requests.post(url, data={'token':token,'line_userid':line_userid})
	if r.status_code == 200: return json.loads(r.text)
	else: return None