#!/bin/bash/python3
# by shiky

from time import sleep
import csv as cs
from selenium import webdriver
#browser=webdriver.Chrome()
browser=webdriver.Firefox(executable_path="./geckodriver")

def gloin(em,passed):
    #browser.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    browser.get("https://gmail.com")
    browser.find_element_by_id("identifierId").send_keys(em)
    browser.find_element_by_id("identifierNext").click()
    sleep(5)
    browser.find_element_by_name("password").send_keys(passed)
    browser.find_element_by_id("passwordNext").click()
    sleep(5)

def glogout():
    browser.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
    browser.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()

def add_lis(f):
    dlist=[]
    em = cs.reader(f)
    for r in em:
        dlist.append(r)
    return dlist
looges=open("email.txt",'r')
#passer=open("pass.txt",'r')
email_list=add_lis(looges)
#pass_list=add_lis(passer)
#password=str(input("Enter the password for all emails :"))
password="22149388" # Enter the password for all emails make it one pass
c=len(email_list)
s=0
#video=str(input("Enter the youtube channel link here : "))
video="https://www.youtube.com/watch?v=dR_hFRa5EZk" # set the video link
vtime=9000 #set the video time insec  edite that 
video_time=vtime+4
number_of_views=2 #that will douple the number of views  in the list edit it with the number you wants
for v in range(number_of_views):
	for i in range(len(email_list)):
    		try:
                   gloin(email_list[i],password)
                   browser.get(video)
                   sleep(video_time)
                   glogout()
                   browser.close()
                   browser = webdriver.Firefox(executable_path="./geckodriver")
    		except:
                    print("try again")

print("done")
browser.close()
