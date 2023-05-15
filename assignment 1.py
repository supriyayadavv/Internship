#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install requests


# In[5]:


pip install bs4


# In[4]:


pip install pandas


# In[2]:


import requests 
from bs4 import BeautifulSoup
import pandas as pd
import csv


# In[7]:


url = "http://quotes.toscrape.com/page/1/"


# In[8]:


response = requests.get(url)


# In[9]:


html = response.content


# In[10]:


soup = BeautifulSoup(response.content,'html.parser')


# In[11]:


quotes = soup.find_all('div', {'class': 'quote'})


# In[20]:


for quote in quotes:
    text = quote.find('span', {'class': 'text'}).text
    print(text[1:])


# In[21]:


for quote in quotes:
   author = quote.find('small', {'class': 'author'}).text
   print(author)


# In[14]:


for quote in quotes:
  tags = [tag.text for tag in quote.find_all("a", class_="tag")]
  print(tags)


# In[15]:


data=[]
for i in range(1,11):
  url = "http://quotes.toscrape.com/page/1"
  response = requests.get(url)
  html = response.content
  soup = BeautifulSoup(response.content,'html.parser')
  quotes = soup.find_all('div', {'class': 'quote'})
  for quote in quotes:
     text = quote.find('span', {'class': 'text'}).text  
     author = quote.find('small', {'class': 'author'}).text
     tags = [tag.text for tag in quote.find_all("a", class_="tag")]
     data.append([text,author,tags])



# In[28]:


df=pd.DataFrame(data,columns=['quote','author','tags'])
df.index=pd.RangeIndex(start=1,stop=len(df)+1)


# In[29]:


df


# In[32]:


df = pd.read_csv('D:\quotes.csv')


# In[37]:


df.to_csv('D:\quotes.csv', index=False, encoding='utf-8-sig', header=True)


# In[35]:


df


# In[3]:


df=pd.read_csv('D:\quotes.csv')


# In[4]:


df


# In[ ]:




