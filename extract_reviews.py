# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:24:50 2017

@author: gautam

"""
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

## Extract and store , reviews of 3 Cab App's reviews Uber, Ola and Meru Cabs  


import requests
import pandas as pd
from bs4 import BeautifulSoup


uber_url = "https://play.google.com/store/apps/details?id=com.ubercab&hl=en";
ola_url = "https://play.google.com/store/apps/details?id=com.olacabs.customer&hl=en";
meru_url = "https://play.google.com/store/apps/details?id=com.winit.merucab&hl=en";

url_list = [uber_url,ola_url,meru_url];
appName_list = ["Uber","OlaCabs","Meru Cabs"];
               
review_df = pd.DataFrame();
for index, url in enumerate(url_list):
    response = requests.get(url);
    item_url_html = response.content;
    item_soup = BeautifulSoup(item_url_html);
    review_list = item_soup.findAll('div', attrs={'class':'review-text'})
    item_text_List = [];                      
    for item in review_list:
        item_text_List.append(item.get_text());
    se=pd.Series(item_text_List);
    review_df[appName_list[index]] = se;
             
review_df.to_csv("CabApp_reviews_df.csv");         

    
        
    




#print(uber_soup.title.string)


 

                         
#uber_df = pd.DataFrame(uber_text_List);
#uber_df.columns = ['uber']

#uber_df.to_csv("Uber_reviews.csv");
    
#print(review_list[0].get_text())


