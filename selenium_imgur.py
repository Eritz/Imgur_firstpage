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


#def album():
#    url = requests.get(imgur_site)
#    url.raise_for_status()
#    soup = BeautifulSoup(url.text, "xml")
#
#
#
#    album_links = soup.find_all('div', {"class":"image post-image"})
#    print(album_links)
#    
#    print('Now downloading images...')
#    for link in album_links:
#            item = link['src']
#            print(item)
#            title = link.find('alt')
#            
#            print('Downloading %s' %(item))
#            actual_image = "https:"+item
#            res = requests.get(actual_image)        
#            res.raise_for_status()  
#            imagefile = open(os.path.join(path, title), 'wb')
#            for chunk in res.iter_content(100000):
#                    imagefile.write(chunk)
#            imagefile.close()  
#
#album()
#print('Done.')