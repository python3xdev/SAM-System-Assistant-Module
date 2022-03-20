import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
import sys

f = open("config.json")
json_data = json.load(f)
f.close()

sam_short = "Sam"
sam_full = "System Assistant Module"

print('Initializing Sam. Your System Assistant Module.')

MASTER = json_data['MASTER']
BROWSER_NAME = json_data['BROWSER_NAME']
BROWSER_EXE_PATH = json_data['BROWSER_EXE_PATH']
EMAIL = json_data['EMAIL']
EMAIL_PASSWORD = json_data['EMAIL_PASSWORD']
EMAIL_CONTACTS = json_data['EMAIL_CONTACTS']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
	engine.say(text)
	engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak(f'Good Morning {MASTER}.')
	elif hour >= 12 and hour < 18:
		speak(f'Good Afternoon {MASTER}.')
	else:
		speak(f'Good Evening {MASTER}.')
	speak(f'I am {sam_short}. Your {sam_full}. Activate me at any time by saying the following commands. Sam. Hey Sam. Ok Sam.')
	print(f"Activate {sam_short} by saying 'Hey {sam_short}.', 'Ok {sam_short}.' or just say '{sam_short}'.")

# Microphone input
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		audio = r.listen(source)
	try:
		print('Recognizing...')
		query = r.recognize_google(audio, language = 'en-US')
		print(f'user said: {query}\n')
	except Exception as e:
		speak('I am sorry, can you repeat that please...')
		query = None

	return query



def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(EMAIL, EMAIL_PASSWORD)
	server.sendmail(EMAIL, to, content)
	server.close()

def reboot_jarvis(usr_said=False):
	if usr_said:
		speak("Rebooting...")
	else:
		speak('Initializing...')
	wishMe()

reboot_jarvis()

r = sr.Recognizer()
while True:
	hidden_query = None
	with sr.Microphone() as source:
		print('Listening for activation keyword...')
		audio = r.listen(source)
		try:
			hidden_query = r.recognize_google(audio, language = 'en-US')
			print(f'user said: {hidden_query}\n')
		except:
			pass
		if hidden_query is not None:
			if (f"hey {sam_short}".lower() in hidden_query.lower()) or (f"play {sam_short}".lower() in hidden_query.lower()) or (f"ok {sam_short}".lower() in hidden_query.lower()) or (f"{sam_short}".lower() in hidden_query.lower()):
				speak("Yes?")
				while True:
					query = takeCommand()
					if query:
						break
				print("Thinking...")

				#-----------------------------------------LOGIC-----------------------------------------
				# checking is the question is valid math
				try:
					if query.lower() != 'help':
						m = eval(query.lower().replace('what is', '').replace('how much is', '').replace('x', '*').replace('squared', '**2').replace('^', '**'))
						speak(f"The result is {m}.")
						continue
					else:
						pass
				except:
					pass  # continuing to the code below
				# Controlling SAM
				if "reboot" == query.lower():
					reboot_jarvis(usr_said=True)
					continue
				elif ("shutdown" == query.lower()) or ("shut down" == query.lower()):
					speak(f"Shutting down... Goodbye {MASTER}.")
					sys.exit()
				elif "your name" in query.lower():
					speak(f"My name is {sam_short}. It stands for {sam_full}.")
					continue
				elif ("help" == query.lower()) or ('what can you do' in query.lower()):
					url = 'https://github.com/python3xdev/SAM-System-Assistant-Module'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					speak('I have opened the official Github repository for my code. Here you can look at the documentation.')
					continue
				elif ('never mind' in query.lower()) or ('nevermind' in query.lower()):
					speak('Ok')
					continue
				elif 'the time' in query.lower():
					strTime = datetime.datetime.now().strftime('%H:%M:%S')
					speak(f'The time is {strTime}')
					continue
				elif 'the date' in query.lower():
					strTime = datetime.datetime.now().strftime('day %d of %B, %Y')
					speak(f'It is {strTime}')
					continue

				# Open Websites
				elif 'open youtube' in query.lower():
					url = 'youtube.com'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue
				elif 'open github' in query.lower():
					url = 'github.com'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue
				elif ('open stack overflow' in query.lower()) or ('open stackoverflow' in query.lower()):
					url = 'stackoverflow.com'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue
				elif 'open weather.com' in query.lower():
					url = 'weather.com'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue

				elif 'open google translate' in query.lower():
					url = 'https://translate.google.com/'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue

				elif 'open gmail' in query.lower():
					url = 'https://gmail.com/'
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue

				# Translate to RUSSIAN
				elif ('in russian' in query.lower()) or ('on russian' in query.lower()) or ('to russian' in query.lower()):
					speak('Translating...')
					query = query.replace('in Russian', '').replace('on Russian', '').replace('to Russian', '')
					query = query.replace('translate', '')
					url = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=ru&text=' + query
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue

				# Translate to UKRAINIAN
				elif ('in ukrainian' in query.lower()) or ('on ukrainian' in query.lower()) or ('to ukrainian' in query.lower()):
					speak('Translating...')
					query = query.replace('in Ukrainian', '').replace('on Ukrainian', '').replace('to Ukrainian', '')
					query = query.replace('translate', '')
					url = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=uk&text=' + query
					webbrowser.register(BROWSER_NAME,None,
					webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
					webbrowser.get(BROWSER_NAME).open(url)
					continue

				# SOFTWARE  # IMPORTANT - the below programs will only open (for Windows) if they are installed to the default location

				elif 'open google chrome' in query.lower():
					try:
						url = 'google.com'
						webbrowser.register('google-chrome',None,
						webbrowser.BackgroundBrowser("C://Program Files (x86)/Google/Chrome/Application/chrome.exe"))
						webbrowser.get('google-chrome').open(url)
						continue
					except:
						speak('Google Chrome is not installed to the default location. Cannot open the program.')
						continue

				elif 'open sublime text' in query.lower():
					try:
						programPath = "C://Program Files//Sublime Text 3//sublime_text.exe"
						os.startfile(programPath)
						continue
					except:
						speak('Sublime Text 3 is not installed to the default location. Cannot open the program.')
						continue

				elif f'open {BROWSER_NAME}' in query.lower():
					try:
						programPath = BROWSER_EXE_PATH
						os.startfile(programPath)
						continue
					except:
						speak('Cannot open the program. Executable file not found.')
						continue

				try:

					# WIKIPEDIA
					if 'wikipedia' in query.lower():
						speak('Searching wikipedia...')
						query = query.replace('wikipedia', '')
						results = wikipedia.summary(query, sentences = 2)
						speak(results)
						continue

					elif 'what is' in query.lower():
						speak('Searching wikipedia...')
						query = query.replace('what is', '')
						results = wikipedia.summary(query, sentences = 2)
						speak(results)
						continue

				except wikipedia.DisambiguationError as e:
					speak('Too many results to this phrase. Explanation might not be accurate. Please manually search for this in Wikipedia to find the proper explanation.')
					continue

				# Send an Email
				for name in EMAIL_CONTACTS:
					if f'email to {name}'.lower() in query.lower():
						if not EMAIL:
							speak('You have not yet connected an email. Please do so by running the setup.py file.')
							break
						try:
							speak('What should I send?')
							content = takeCommand()
							to = EMAIL_CONTACTS[name]
							sendEmail(to, content)
							speak('Email has been sent successfully.')
						except Exception as e:
							if ('Username and Password not accepted' in str(e)) and ('gsmtp' in str(e)):
								url = 'https://myaccount.google.com/lesssecureapps?pli=1'
								webbrowser.register(BROWSER_NAME,None,
								webbrowser.BackgroundBrowser(BROWSER_EXE_PATH))
								webbrowser.get(BROWSER_NAME).open(url)
								speak("You must enable Less Secure Apps in your email Inbox. I have opened a page where you can enable this feature. After doing this, please retry sending your email.")
							else:
								speak("There has been an error in sending your email. Please check the log file for more details.")
								with open("log.txt", 'a') as f:
									f.write(f"{e}\n\n")
						break
					elif f'email to' in query.lower() and name.lower() not in query.lower():
						speak(f'A contact by that name was not found in your email contact list. To add more contacts, edit the config.jayson file.')  # the bot will say jayson instead of spelling out j s o n
						break

		# Just For Fun
		if hidden_query and (("hey google" == hidden_query.lower()) or ("hey siri" == hidden_query.lower()) or ("hey alexa" == hidden_query.lower()) or ("hey jarvis" == hidden_query.lower())):
			speak("I'll take that as a compliment, but I'm Sam. Let me know how I can help.")
			continue
