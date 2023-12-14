#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

company_name = input("Enter the company name: ")
url = f"https://www.google.com/search?q={company_name}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

search_results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
if search_results:
    print(f"Here's some information about {company_name}:")
    for result in search_results:
        print(result.get_text())
else:
    print(f"Sorry, I couldn't find any information about {company_name} on Google.com.")
#SXL

