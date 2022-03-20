from colorama import init
from termcolor import colored
import os
import shutil
import json



os.system('cls' if os.name == 'nt' else 'clear')

def center_print(s):
    print(s.center(shutil.get_terminal_size().columns))

init()

print("\n")

center_print(colored("SAM (System Assistant Module) Setup", "green", attrs=["bold"]))
colored("Please fill in all of the following information for the program to work properly.", "red", attrs=["bold"])

MASTER = input(colored("    What is your name?: ", "cyan", attrs=["bold"]))
BROWSER_NAME = input(colored("    What is the name of the web browser you use?: ", "cyan", attrs=["bold"]))
BROWSER_EXE_PATH = input(colored("    Please specify the executable path for your browser: ", "cyan", attrs=["bold"]))

setup_email = input(colored("    Would you like to connect a GMail account (you will have to enable 'Less Secure Apps' in your email account)? y/n: ", "cyan", attrs=["bold"]))

EMAIL = None
EMAIL_PASSWORD = None
EMAIL_CONTACTS = None
if setup_email.lower() == "y":
	EMAIL = input(colored("    Enter your GMail address: ", "cyan", attrs=["bold"]))
	EMAIL_PASSWORD = input(colored("    Enter your GMail password: ", "cyan", attrs=["bold"]))
	print(colored("    You must add at least one contact:", "blue", attrs=["bold"]))
	add_contacts = True
	EMAIL_CONTACTS = {}
	while add_contacts:
		contact_name = input(colored("    Contact Name: ", "cyan", attrs=["bold"]))
		contact_email = input(colored("    Contact Email Address: ", "cyan", attrs=["bold"]))
		EMAIL_CONTACTS[contact_name] = contact_email
		more = input(colored("    Do you want to add more contacts? y/n: ", "cyan", attrs=["bold"]))
		add_contacts = True if more.lower() == 'y' else False


dict_data = {
	"MASTER": MASTER,
	"BROWSER_NAME": BROWSER_NAME.lower(),
	"BROWSER_EXE_PATH": BROWSER_EXE_PATH,
	"EMAIL": EMAIL,
	"EMAIL_PASSWORD": EMAIL_PASSWORD,
	"EMAIL_CONTACTS": EMAIL_CONTACTS,
}

json_obj = json.dumps(dict_data, indent=4)

with open("config.json", "w") as f:
	f.write(json_obj)

print("\n")
print(colored("    Setup complete!", "green", attrs=["bold"]) + " You may now run the __init__.py file to start SAM.")
print("    Activate Sam by saying 'Hey Sam.', 'Ok Sam.' or just say 'Sam' (works best by just saying 'Sam'). Have fun!")
input('    Press Enter To Exit...')
