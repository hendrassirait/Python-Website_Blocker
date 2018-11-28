import time
from datetime import datetime as dt #datetime format is year,month,day,hour,minute,second. right now we only use from year to hour only to define work hour

hosts_temp="hosts" #only temp file to check if code is working or not
hosts_path="/etc/hosts" #this is hosts file location for mac and linux, the location is deifferent for windows
# on windows the default address is C:\Windows\System32\drivers\etc\hosts
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
		print("working hour...")
		with open(hosts_path,'r+') as file: #r+ is used to enable read and write the document
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n") #hosts file format to block website is "localhost website",the "\n" at the end of the line is to create break lie for each website				
	else:
		with open(hosts_path,'r+') as file:
			content=file.readlines()
			file.seek(0)# it moves pointer to the first of the line
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate() # this function delete every text in hosts that came after the first lines
		print("Fun Hours...")
	time.sleep(5) #it check the time every 5 secons
