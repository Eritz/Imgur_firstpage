import os, requests
from selenium import webdriver

# Let the user give the imgur site
print('This program will download and save images from a given imgur link.',
'\nPlease provide the full imgur link (excluding the .png, .jpeg, .gif, etc.)')

imgur_site = input('Copy and paste the imgur full link here:\n')
imgur_site_append = imgur_site +'/all?scrolled'
# Create the folder
print('Where would you like to make your folder?')
folder_location = str(input())
print('Okay. What would you like to name it?')
folder_name = str(input())
location = folder_location+'/'+folder_name
os.makedirs(location, exist_ok=True)
print('Okay. The folder has been created.')

browser = webdriver.Firefox()
browser.get(imgur_site_append)

image_links = []
# Saves the href links found on the expanded page into image_links
for ele in browser.find_elements_by_css_selector('div.post'):
    tags = ele.find_elements_by_tag_name('a')
    for hrefs in tags:
        image_links.append(hrefs.get_attribute('href'))
# Uses requests to download the links    
for link in image_links:
    url = requests.get(link)
    url.raise_for_status()
    imagefile = open(os.path.join(location,os.path.basename(link)), 'wb')
    print('Downloading... %s' %(imagefile))
    for chunk in url.iter_content(10000):
        imagefile.write(chunk)
    imagefile.close()
print('Done.')
