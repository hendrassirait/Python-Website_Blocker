# Python-Website_Blocker
Using python to edit hosts file and schedule it

Its an app to help me block some website on scheduled hour,
like i want to blok facebook.com from 10am to 18pm so i can focus on my job,
the app running on terminal (command prompt on windows)

a few things to remind,

1. im using mac so the hosts file is on etc/hosts the same as linux based os,
but in windows, the default location is C:\Windows\System32\drivers\etc\hosts

2. i'm not using input method to this app, so you need to edit the app (website that u want to block and the time range) directly in your code editor

3. this app need administrator permision to edit the hosts file, so in mac/linux you need to run 

{sudo python3 website_blocker}
and then input your password

4. to make the program run on your background automatically, you can use crontab on mac/linux
