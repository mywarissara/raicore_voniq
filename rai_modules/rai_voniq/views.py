from django.shortcuts import render
from . import chatbot
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
import json

from . import raiuser_api
from . import linebot_api
# Create your views here.
def index(request):
	response = ""
	try:
		message = request.POST['message']
		response = chatbot.chatbot(message)
	except: 
		pass
	return render(request, 'rai_voniq/index.html', {'response':response})

def passPara(request):
	message = request.GET['message']
	# return chatbot.chatbot(message)
	return HttpResponse(chatbot.chatbot(message))

def invite(request):
	print('response from liff')
	return render(request, 'rai_voniq/liff.html')



def results(req):
	# print(req)
	inputword = req["queryResult"]['queryText']
	print(req)
	if "originalDetectIntentRequest" in req:
		if 'source' in req["originalDetectIntentRequest"]:	
			source = req["originalDetectIntentRequest"]["source"]
			if source == 'line':
				userId = req["originalDetectIntentRequest"]["payload"]["data"]["source"]["userId"]
				print("query from " + source)
				raiuser = raiuser_api.request(userId)
				name = raiuser['first_name']
				username = raiuser['username'] # ask for a request
				print(name)
				
				# push_msg = linebot_api.pushmsg(userId, "hello" + str(userId))
				# print(push_msg)
			else:
				print("unknown platform")
		else:
			print("query from web")
	else:
		print ("query from dialogflow web")


	action = req["queryResult"]["action"]
	if action == "input.unknown":
		if 'danc' in inputword.lower():
			return {'fulfillmentText': 'Let\'s get dance together! LaLaLaLa DeDooDe Da LaLaLaaaaaa LaLaLaLa DeDooDe Da LaLaLaaaaaa'}
		if 'walk' in inputword.lower():
			return {'fulfillmentText': 'I like to walk burning calories.'}
		if 'run' in inputword.lower():
			return {'fulfillmentText': 'Running out of your heart is like I\'m runing on the treadmill.'}
		if 'sit' in inputword.lower() or 'rest' in inputword.lower():
			return {'fulfillmentText': 'Thank you captain. I feel so stiff.'}
		if 'stop' in inputword.lower():
			return {'fulfillmentText': 'Ok man. As your wish!'}
		if 'fuck' in inputword.lower() or 'shit' in inputword.lower() or 'bitch' in inputword.lower() or 'ass' in inputword.lower():
			return {'fulfillmentText': 'Rude words is unacceptable.'}
		if 'hell' in inputword.lower() or 'die' in inputword.lower() or 'kill' in inputword.lower() or 'death' in inputword.lower() or 'f***' in inputword.lower():
			return {'fulfillmentText': 'You are so cruel.'}
		if 'stand' in inputword.lower():
			return {'fulfillmentText': 'Yes Captain!'}
		
	# if action == "PreBorrowequipment.PreBorrowequipment-custom.Borrowarduino-yes":
	# 	equip = req["queryResult"]["outputContexts"][0]["parameters"]["equip"]
	# 	brand = req["queryResult"]["outputContexts"][0]["parameters"]["brand"]
	# 	serie = req["queryResult"]["outputContexts"][0]["parameters"]["serie"]
	# 	return {'fulfillmentText': name.capitalize() + ' wants to borrow ' + equip.capitalize() +'. I will make a request for you. Thanks!'}
		
	# if action == "Preroomreservation.Preroomreservation-custom.ReserveBuilding-yes":
	# 	building = req["queryResult"]["outputContexts"][0]["parameters"]["building"]
	# 	room = req["queryResult"]["outputContexts"][0]["parameters"]["room"]
	# 	date = req["queryResult"]["outputContexts"][0]["parameters"]["date"]
	# 	time = req["queryResult"]["outputContexts"][0]["parameters"]["time"]
	# 	duration = req["queryResult"]["outputContexts"][0]["parameters"]["duration"]
	# 	return {'fulfillmentText': name.capitalize() + ' wants to reserve ' + room.capitalize() +" at "+ building.capitalize() +'. I will make a request for you. Thanks!'}
	
	return {}

@csrf_exempt
def hook(request): #web hook for dialoagflow
	print('rai_voniq POST data')
	req = json.loads(request.body)
	return JsonResponse(results(req), safe=False)

def liff(request):
	print('response from liff')
	return render(request, 'rai_voniq/liff.html')


