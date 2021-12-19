# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:36:36 2020

This code uses ProPublica's API to gather search results of Non-profit organizations.
Using the key information gathered, the ein number, the code will generate URLs for the NPO's web page on GuideStar
Then, using random user_agents, the code webscrapes the NPO's mission statement listed on Guidestar
So far, the code can only process 100 NPOs at a time, with a max limit of 900 (due to limited user_agents) as additional go-arounds will trigger MFA from Guidestar
@author: lawrence liu, pamela pan
"""


import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


#For each search, simply alter the q variable at the end of the url below
#e.g. q=%new%york% yields results related to 'new york', q = philadelphia yields results related to philadelphia. 
#each search will yield 100 npo results
#there is also a method to reach the next page of results, using the page parameter that defaults at 0, provided by the api
#e.g. q=childcare&page=%2% <- Supposedly...
url = 'https://projects.propublica.org/nonprofits/api/v2/search.json?q=%childcare%NY%'

search_response = requests.get(url)
r_search = search_response.json()

method_response = requests.get(url)
r_method = method_response.json()
new_dict = r_method['organizations']

#empty dataframe for ProPublica variables
df = pd.DataFrame(columns=['Name','Sub_name','City','State','ntee_code'])

name = {'Name':[]}
subname = {'Sub_name':[]}
city = {'City':[]}
state = {'State':[]}
ntee = {"ntee_code":[]}

for d in new_dict:
    for i in d:
        if i == "name":
            st2 = d[i]
            name["Name"].append(st2)
        if i == "sub_name":
            st3 = d[i]
            subname["Sub_name"].append(st3)
        if i == "city":
            st4 = d[i]
            city["City"].append(st4)
        if i == "state":
            st5 = d[i]
            state["State"].append(st5)
        if i == "ntee_code":
            st6 = d[i]
            ntee["ntee_code"].append(st6)
    
    #inserting variables into propublica dataframe    
    new_row = [st2,st3,st4,st5,st6]
    new_df = pd.DataFrame([new_row],columns=['Name','Sub_name','City','State','ntee_code']  )
    df = pd.concat([df,new_df])

#parsing out the ein into correct URL format
ein_num = []
ein_url = []
for item in r_search['organizations']:
   ein_num.append(item['ein'])
   
for item in ein_num:
    ein = str(item)
    einstr = ein[0:2] + '-' + ein[2:]
    ein_url.append(einstr)
    
      
#generating url list
guide_url = []
for ein in ein_url:
    guide_url.append('https://www.guidestar.org/profile/' + ein)

#pulling in the user agents and converting txt file to a list
agents = open('C:/Users/lwrnc/Desktop/Datathon/users.txt', 'r')
agents_list = []

#removing the \n from all user_agents
for line in agents:
   agents_list.append(line[:-2])

#creating 2-column dataframe for mission statement retrieval from Guidestar
df1 = pd.DataFrame(columns = ['Ein', 'Mission Statement'])

#unethical?
count = 0
for url in guide_url:
    
    #changing up the user_agent each time
    headers = {"User-Agent": agents_list[0]}
    
    r = requests.get(url, headers = headers) 
    
    #sometimes NGOs do not have a guidestar website
    if r.status_code != 200:
        mission = 'There is no Guidestar Website'

    else:
        soup = BeautifulSoup(r.content, features = 'lxml')
        
        #there is possibility to pull more information from the Guidestar website, but we just ran out of time....
        mission = soup.find(id='mission-statement').get_text().strip()
    
    new_row = [ein_url[count], mission]
    new_df = pd.DataFrame([new_row],columns=['Ein','Mission Statement'])    
    df1 = pd.concat([df1, new_df])
    
    count += 1


#combining the ProPublica and Guidestar dataframe to one csv output
df['Ein'] = df1['Ein']
df['Mission Statement'] = df1['Mission Statement']
df.to_csv('npos.csv')
