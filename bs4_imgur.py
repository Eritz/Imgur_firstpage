import os, requests
from bs4 import BeautifulSoup

# Let the user give the imgur site
print('This program will download and save images from a given imgur link.',
'\nPlease provide the full imgur link (excluding the .png, .jpeg, .gif, etc.)')

imgur_site = input('Copy and paste the imgur full link here:\n')
imgur_site_append = imgur_site +'/all?scrolled'
# Creates the folder
print('Where would you like to make your folder?')
folder_location = str(input())
print('Okay. What would you like to name it?')
folder_name = str(input())
location = folder_location+'/'+folder_name
os.makedirs(location, exist_ok=True)
print('Okay. The folder has been created.')

url = requests.get(imgur_site_append)
url.raise_for_status()
soup = BeautifulSoup(url.text, "html.parser")

links = soup.find_all('div', {"class":"post"})

for link in links:
    site = link.select('a')
    for s in site:
        image_link = "https:" + s.get('href')
        download = requests.get(image_link)
        download.raise_for_status()
        imagefile = open(os.path.join(location,os.path.basename(image_link)), 'wb')  
        print('Downloading... %s' %(imagefile))
        for chunk in download.iter_content(10000):
            imagefile.write(chunk)
        imagefile.close()
print('Done.')
