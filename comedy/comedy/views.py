from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import chatterbot_corpus
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
from django.core.files import File
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)


trainer = ChatterBotCorpusTrainer(chatbot)
# chatbot.trainer.train('chatterbot.corpus.english')
# chatbot.trainer.export_for_training('./export.yml')

import gpt_2_simple as gpt2
import os
import requests


# model_name="124M"
# if not os.path.isdir(os.path.join("models", model_name)):
# 	print(f"Downloading {model_name} model...")
# 	gpt2.download_gpt2(model_name=model_name) 
# checkpoint_path = "/Users/pawelk/Downloads/django-chat/checkpoint/run1"

# response = chatbot.get_response("Hi there")
# print(response)
# Train based on the english corpus

#Already trained and it's supposed to be persistent
#chatbot.train("chatterbot.corpus.english")

# f = open('blank.txt', 'w')
# f.close()
	
@csrf_exempt
def get_response(request):
	response = {'status': None}
	# f = open('blank.txt', 'r+')	
	
	
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		message = data['message']
		# f.write()
		print(message)
		# numb = random.randint(31,88)	
		# if message=="random":
		# 	sess = gpt2.start_tf_sess()
		# 	gpt2.load_gpt2(sess)
		# 	chat_response = gpt2.generate(sess,
		# 		# prefix=message,
		# 		# include_prefix=False,
		# 		length=numb,
		# 		temperature=0.7,
		# 		nsamples=5,
		# 		batch_size=5,
		# 		top_p=0.9,
		# 		top_k=20,
		# 		# truncate="<|endoftext|>",
		# 		return_as_list=True)[0]
				
		# 	response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True, 'username' : "Bot: "}
		# 	response['status'] = 'ok'
		# else:
    		
		chat_response = chatbot.get_response(message).text
			# chat_response2 = gpt2.generate(sess,
			# 	prefix=message,
			# 	include_prefix=True,
			# 	length=numb,
			# 	temperature=0.75,
			# 	nsamples=5,
			# 	batch_size=5,
			# 	top_p=0.9,
			# 	top_k=30,
			# 	# truncate="<|endoftext|>",
			# 	return_as_list=True)[0]
			# # print(chat_response)
			
			
			
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True, 'username' : "Bot: "}
		response['status'] = 'ok'
			# chat_response2.rstrip()
			# f.write("Paul: " + message + "\nBot: " + chat_response2 + "\n")
			# if len(f.read()) > 200:
        	# 		f=f[::100]
		

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="home.html"):
	context = {'title': 'Chatbot Version 1.0'}
	return render_to_response(template_name, context)