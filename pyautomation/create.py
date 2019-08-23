import os, sys, time
import subprocess
import webbrowser
from github import Github

folder = sys.argv[1]
username = "" #your github username
password = "" #your github password

application1 = "" #path to executable file of desired application 
application2 = "" #path to executable file of desired application 

# Path to be created
path = '' + folder
try:
   os.mkdir(path)
except OSError:
   print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

subprocess.Popen(application1)
time.sleep(2)
subprocess.Popen(application2)
time.sleep(2)


user = Github(username, password).get_user()
repo = user.create_repo(sys.argv[1])
webbrowser.open('https://github.com/login')
	

