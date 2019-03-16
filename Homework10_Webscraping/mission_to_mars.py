#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pandas as pd


# # NASA Mars News
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# In[27]:

def scrape():
    # URL of page to be scraped
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'


    # In[28]:


    # Retrieve page with the requests module
    response = requests.get(url)


    # In[29]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')


    # In[30]:


    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


    # In[33]:


    #First Scrape Variables
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="rollover_description_inner").text
    news_p


    # # JPL Mars Space Images - Featured Image

    # In[7]:


    #Configuring Splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Visiting Site And Navigating To Full Image
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    browser.click_link_by_partial_text('.jpg')
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')

    #Storing Image URL As A Variable
    nasa_image = soup.find('img')["src"]
    


    # # Mars Weather

    # In[8]:


    #Configuring Splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit('https://twitter.com/marswxreport?lang=en')
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_weather = soup.find("p", class_ ="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


    # In[9]:


    mars_weather


    # # Mars Facts

    # In[10]:


    url = "https://space-facts.com/mars/"
    pandas_scrape = pd.read_html(url)


    # In[11]:


    pandas_scrape_df = pandas_scrape[0]
    pandas_scrape_df.columns = ["Field", "Value"]
    pandas_scrape_df.head()


    # In[12]:


    facts_html = pandas_scrape_df.to_html().replace('\n', '')


    # In[13]:


    facts_html


    # # Mars Hemispheres

    # In[14]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_hemispheres = soup.find_all("div", class_ ="item")

    #initiate list
    hemisphere_images = []
    root_url = 'https://astrogeology.usgs.gov'

    #loop through hemisphere <div>s
    for hemisphere in mars_hemispheres:
        #store the name
        name = hemisphere.find("h3").text
        #contruct path to image page
        branch_url = hemisphere.find('a', class_='itemLink product-item')['href']
        browser.visit(root_url+branch_url)
        #store image path
        image = bs(browser.html, 'html.parser').find("a", target="_blank")['href']
        #append to dictionary
        hemisphere_images.append({"title" : name, "img_url" : image})
        #return to main page
        browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
        browser.quit()


    final_dictionary = []

    final_dictionary.append(hemisphere_images)
    final_dictionary.append({'latest_tweet': mars_weather})
    final_dictionary.append(pandas_scrape_df.to_dict("records"))
    final_dictionary.append({"Nasa Image":nasa_image})
    final_dictionary.append({"latest_news":news_p})
    final_dictionary.append({"news_title":news_title})
    # In[ ]:
    return final_dictionary




# In[ ]:




