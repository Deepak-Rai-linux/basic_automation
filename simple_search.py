#!/usr/bin/python3

#################################################
#Author : Deepak Rai                            #
#Copyright (c) 2022                             #
#Contact : deepak.rai.linux@gmail.com           #
#################################################

#This is a very basic script to list out top headings of a quick Google search

import bs4
import requests

keyword = input("Enter the search keyword: ")
url = "https://google.com/search?q=" + keyword

#Fetch the URL data
request_result = requests.get(url)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text, "html.parser")

#Grabbing all major headings from the seach result
heading_object=soup.find_all('h3')

#Iterate through obejct to print it as strings
print('Major heading in Google search result of ' + "\033[38;5;208m" + keyword + "\033[0;0m" + ' are:')
i = 1
for info in heading_object:
    print(f"{i} : {info.getText()}")
    print("=========================================")
    i = i+1
