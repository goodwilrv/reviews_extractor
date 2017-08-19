# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:24:50 2017

@author: gautam

"""

## Extract and store , reviews of 3 Cab App's reviews Uber, Ola and Meru Cabs  


import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver


uber_url = "https://play.google.com/store/apps/details?id=com.ubercab&hl=en";
ola_url = "https://play.google.com/store/apps/details?id=com.olacabs.customer&hl=en";
meru_url = "https://play.google.com/store/apps/details?id=com.winit.merucab&hl=en";

url_list = [uber_url,ola_url,meru_url];
appName_list = ["Uber","OlaCabs","Meru Cabs"];
driver = webdriver.Chrome();
               
review_df = pd.DataFrame();
for index, url in enumerate(url_list):
    driver.get(url);
    time.sleep(5);
    item_text_List = [];

    driver.execute_script("window.scrollTo(0, 1100);")
    time.sleep(3);
    buttonToClick = driver.find_element_by_xpath("//div[@class='button-image'][(ancestor::button[@class='expand-button expand-next'])][(ancestor::div[@class='details-section reviews'])]");
   ## print("Extracting the review ::===>>> buttonToClick ",buttonToClick);
    action = webdriver.ActionChains(driver);
  ##  print("Extracting the review ::===>>> move to element ",buttonToClick);
    action.move_to_element(buttonToClick)
    action.perform()
  ##  print("Extracting the review ::===>>> Just before clicking ",buttonToClick);
    buttonToClick.click();
    time.sleep(2);
                                                
                                                
    for i in range(1,200):
        print("Extracting the review ::===>>> No. of iteration ",i);
        expandbuttonToClick = driver.find_element_by_xpath("//div[@class='button-image'][(ancestor::button[@class='expand-button expand-next'])][(ancestor::div[@class='details-section reviews'])]");
       ## print("Extracting the review Inside loop ::===>>> buttonToClick ",expandbuttonToClick);
        action = webdriver.ActionChains(driver);
      ##  print("Extracting the review Inside loop::===>>> move to element ",expandbuttonToClick);
        action.move_to_element(expandbuttonToClick)
        action.perform()
      ##  print("Extracting the review Inside loop::===>>> Just before clicking ",expandbuttonToClick);
        expandbuttonToClick.click();
        time.sleep(2);
        
        
        items_html= driver.find_elements_by_class_name('review-text');
       # print("Extracting the review ::===>>> item_html ",item_html);
        for item in items_html:
            content = item.get_attribute('outerHTML');
            soup = BeautifulSoup(content, "html.parser");
            review = soup.find('div',class_='review-text').get_text()
            item_text_List.append(review);
        
        
       ## review_list = item_soup.findAll('div', attrs={'class':'review-text'})
        time.sleep(2);
                  
    print("Extracting the review ::===>>> item_text_List ",item_text_List);
         
    se=pd.Series(item_text_List);
    review_df[appName_list[index]] = se;
    print("Extracting the review ::===>>> review_df ",review_df.count());
    
    
             
review_df.to_csv("CabApp_reviews_df.csv");         

 


