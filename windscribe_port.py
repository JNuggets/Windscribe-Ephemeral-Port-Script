from selenium import webdriver
import selenium      
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

# For using sleep function because selenium  
# works only when the all the elements of the  
# page is loaded. 
import time  

import qbittorrentapi

#Required for running chromedriver headless
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless") #Disable to view chrome

from selenium.webdriver.common.keys import Keys  
  
# Creating an instance webdriver 
browser = webdriver.Chrome(options=chrome_options)  
browser.get('https://www.windscribe.com/login') 
time.sleep(2) 
  
print("Login to Windscribe") 
  
user = browser.find_element("xpath", '//*[@id="username"]') 
  
# Enter User Name 
user.send_keys('username') 
  
passw = browser.find_element("xpath", '//*[@id="pass"]') 
  
# Enter and Submit Password
passw.send_keys('password') 
passw.submit()

print("Login Successful") 

time.sleep(5) 
browser.get('https://windscribe.com')
time.sleep(5)
browser.get('https://windscribe.com/myaccount#porteph')
print("Load Request Ephemeral Port Page")
time.sleep(5)

print("")
delPort = browser.find_element("xpath", '//*[@id="request-port-cont"]/button')
delPort.click()
print("Delete Port")
time.sleep(5)

reqMatchPort = browser.find_element("xpath", '//*[@id="request-port-cont"]/button[2]')
reqMatchPort.click()
print("Request New Port")
time.sleep(5)

port = browser.find_element("xpath", '//*[@id="epf-port-info"]/span[1]')

        
print("New Port: " + port.text)
aquiredPort = port.text
# print("Saving to port.txt")
# with open("port.txt", "w") as text_file:
#     print(aquiredPort, file=text_file)
  
# closing the browser 
browser.close()

# instantiate a Client using the appropriate WebUI configuration
client = qbittorrentapi.Client(host='https://qbittorrent.example.com', port=443, username='username', password='password')
# the Client will automatically acquire/maintain a logged in state in line with any request.
# therefore, this is not necessary; however, you many want to test the provided login credentials.
try:
    client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

# display qBittorrent info
# print(f'qBittorrent: {client.app.version}')
# print(f'qBittorrent Web API: {client.app.web_api_version}')

#Set qBittorrent listening port
prefs = client.application.preferences
prefs['listen_port'] = aquiredPort
client.app.preferences = prefs
print("Set qBittorrent listening port to " + aquiredPort)
