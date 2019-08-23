PythonAutomation 

Using python to automate the beginning of a project. create.py will open desired applications and start a github repository with project name.

For this to work you will need the path to the executable files for any applications you want to open. 
You will also need your git username and password. (I suggest storing these in environment variables and using os.environ but hardcoding them will work just fine)

To get this program to work:
-Add all the neccessary information to the .bat and .py files.
-Move create.bat to C: -> Windows -> System32
-In cmd, type "create" followed by project name
