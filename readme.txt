
This is a simple app, where user will be able to 

1) Add list of tasks they planned to do

2) Delete list of tasks which was already added

3) List the tasks added.

Reference:
https://www.youtube.com/watch?v=ovql0Ui3n_I&t=606s

Installation:
-------------------------------------------------------------------------------------------------------------------

C:\>cd App_Dojo

C:\App_Dojo>pipenv install django
Creating a virtualenv for this project…
Pipfile: C:\App_Dojo\Pipfile
Using c:\users\ajith\appdata\local\programs\python\python37-32\python.exe (3.7.1) to create virtualenv…
[=   ] Creating virtual environment...Already using interpreter c:\users\ajith\appdata\local\programs\python\python37-32\python.exe
Using base prefix 'c:\\users\\ajith\\appdata\\local\\programs\\python\\python37-32'
New python executable in C:\Users\ajith\.virtualenvs\App_Dojo-y7cIq619\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\ajith\.virtualenvs\App_Dojo-y7cIq619
Creating a Pipfile for this project…
Installing django…
Adding django to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (4f9dd2)!
Installing dependencies from Pipfile.lock (4f9dd2)…
  ================================ 2/2 - 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

C:\App_Dojo>pipenv shell
Launching subshell in virtual environment…
Microsoft Windows [Version 10.0.10586]
(c) 2015 Microsoft Corporation. All rights reserved.

(App_Dojo-y7cIq619) C:\App_Dojo>django-admin startproject editdojo_project .

(App_Dojo-y7cIq619) C:\App_Dojo>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

(App_Dojo-y7cIq619) C:\App_Dojo>dir
 Volume in drive C is Windows 10
 Volume Serial Number is F84F-2D17

 Directory of C:\App_Dojo

03/20/2019  11:48 AM    <DIR>          .
03/20/2019  11:48 AM    <DIR>          ..
03/20/2019  11:48 AM    <DIR>          editdojo_project
03/20/2019  11:48 AM               563 manage.py
03/20/2019  11:44 AM               151 Pipfile
03/20/2019  11:45 AM             1,053 Pipfile.lock
               3 File(s)          1,767 bytes
               3 Dir(s)  35,805,990,912 bytes free

(App_Dojo-y7cIq619) C:\App_Dojo>python mange.py runserver
python: can't open file 'mange.py': [Errno 2] No such file or directory

(App_Dojo-y7cIq619) C:\App_Dojo>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 20, 2019 - 11:48:58
Django version 2.1.7, using settings 'editdojo_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[20/Mar/2019 11:49:10] "GET / HTTP/1.1" 200 16348
[20/Mar/2019 11:49:11] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[20/Mar/2019 11:49:11] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 82564
[20/Mar/2019 11:49:11] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 80304
[20/Mar/2019 11:49:11] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 81348
Not Found: /favicon.ico
[20/Mar/2019 11:49:11] "GET /favicon.ico HTTP/1.1" 404 1982
