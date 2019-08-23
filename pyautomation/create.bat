cd
REM replace quotes with 'path to this folder//create.py'
python "" %*
REM replace quotes with path from the path variable in create.py (important: do not add '+ folder')
cd ""//%1
echo %1 >> README.md
git init
git add README.md
git commit -m "first commit"
REM replace quotes with your github username
git remote add origin https://github.com/""/%1
git push -u origin master
pause

