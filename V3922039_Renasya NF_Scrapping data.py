#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import digunakan untuk mengimport modul yang dibutuhkan
import requests
from bs4 import BeautifulSoup as bs
import csv

# URL yang akan di scrape
URL = 'https://proxyway.com/reviews'
titles_list = []

# Melakukan perulangan untuk mengabil data judul di setiap halaman
for page in range(1, 4):
    req = requests.get(f"{URL}/page/{page}")
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('h3')
    count = 1
    
    for title in titles:
        d = {}
        d['Page Number'] = f'Page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text.strip()
        count += 1
        titles_list.append(d)

# Menyimpan data ke dalam file CSV
filename = 'title_review.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Page Number', 'Title Number', 'Title Name'])
    writer.writeheader()
    writer.writerows(titles_list)

# Print keterangan jika proses scraping sukses dilakukan 
print("Scraping selesai. Data telah disimpan ke dalam file CSV.")


# In[3]:


# AMBIL DATA GAMBAR DARI https://proxyway.com/reviews

# Import digunakan untuk mengimport modul yang dibutuhkan
import requests
from bs4 import BeautifulSoup as bs
import csv
from requests.exceptions import Timeout, RequestException

# URL yang akan di scrape
URL = "https://proxyway.com/reviews"
timeout = 5  # Contoh timeout 5 detik

print("\n")
print("Scraping images from:", URL, "\n")

# Menyiapkan file CSV
csv_file = open('image_urls.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'URL'])

# Menentukan nomor halaman yang akan di scrape
page = 1
max_page = 3 

# Melakukan perulangan untuk mengambil data gambar di setiap halaman
while page <= max_page:
    try:
        req = requests.get(f"{URL}/page/{page}", timeout=timeout)
        req.raise_for_status()  # Raise an exception if the request was unsuccessful
        soup = bs(req.text, 'html.parser')
        images = soup.find_all('img')

        if not images:
            break

        for i, image in enumerate(images):
            if 'src' in image.attrs:
                image_url = image['src']
                csv_writer.writerow([f"Image {i+1}", image_url])

        page += 1

    except (Timeout, RequestException) as e:
        print("An error occurred:", str(e))
        break

# Menutup file CSV
csv_file.close()

# Print keterangan jika proses scraping sukses dilakukan 
print("Data telah disimpan ke dalam file image_urls.csv")


# In[4]:


# Import digunakan untuk mengimport modul yang dibutuhkan
import requests
from bs4 import BeautifulSoup as bs
import csv

# URL yang akan di scrape
URL = 'https://proxyway.com/news'
titles_list = []

# Melakukan perulangan untuk mengabil data judul di setiap halaman
for page in range(1, 4):
    req = requests.get(f"{URL}/page/{page}")
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('h3')
    count = 1
    
    for title in titles:
        d = {}
        d['Page Number'] = f'Page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text.strip()
        count += 1
        titles_list.append(d)

# Menyimpan data ke dalam file CSV
filename = 'title_news.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Page Number', 'Title Number', 'Title Name'])
    writer.writeheader()
    writer.writerows(titles_list)
    
# Print keterangan jika proses scraping sukses dilakukan 
print("Scraping selesai. Data telah disimpan ke dalam file CSV.")


# In[5]:


# AMBIL DATA GAMBAR DARI https://proxyway.com/news

# Import digunakan untuk mengimport modul yang dibutuhkan
import requests
from bs4 import BeautifulSoup as bs
import csv
from requests.exceptions import Timeout, RequestException

# URL yang akan di scrape
URL = "https://proxyway.com/news"
timeout = 5  # Contoh timeout 5 detik

print("\n")
print("Scraping images from:", URL, "\n")

# Menyiapkan file CSV
csv_file = open('image_news.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'URL'])

# Menentukan nomor halaman yang akan di scrape
page = 1
max_page = 6 

# Melakukan perulangan untuk mengambil data gambar di setiap halaman
while page <= max_page:
    try:
        req = requests.get(f"{URL}/page/{page}", timeout=timeout)
        req.raise_for_status()  # Raise an exception if the request was unsuccessful
        soup = bs(req.text, 'html.parser')
        images = soup.find_all('img')

        if not images:
            break

        for i, image in enumerate(images):
            if 'src' in image.attrs:
                image_url = image['src']
                csv_writer.writerow([f"Image {i+1}", image_url])

        page += 1

    except (Timeout, RequestException) as e:
        print("An error occurred:", str(e))
        break

# Menutup file CSV
csv_file.close()

# Print keterangan jika proses scraping sukses dilakukan 
print("Data telah disimpan ke dalam file image_news.csv")


# In[ ]:




