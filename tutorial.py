from bs4 import *
import requests
import os

# CREATE FOLDER
def folder_create(images):
	try:
		folder_name = input("Enter Folder Name:- ")
		# folder creation
		os.mkdir(folder_name)

	# if folder exists with that name, ask another name
	except:
		print("Folder Exist with that name!")
		

	# image downloading start
	download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):

	# initial count is zero
 
    val  = 315
	# print total images found in URL
    print(f"Total {len(images)} Image Found!")
    image_set  = {}

	# checking if images is not zero
    if len(images) != 0:
	    for i, image in enumerate(images):
                if image_set.get(image)==None:
                    image_set[image] = 1
                    try:
                        image_link = image["src"]
                    except:
                        pass
                    try:
                        r =  requests.get(image_link).content
                        try:
                            
                            r =str(r, 'utf-8')
                        except UnicodeDecodeError:
                            with open(f"{folder_name}/images{val+1}.jpg", "wb+") as f:
                                f.write(r)
                            val  = val +1
                    except :
                        pass
                        
                            
                    
            
              

    
# MAIN FUNCTION START
def main(url):
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
  
	# content of URL
    r = requests.get(url, headers =  headers)

	# Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')
  
	# find all images in URL
    images = soup.findAll('img')

	# Call folder create function
    folder_create(images)


# take url

url = input("Enter URL:- ")

# CALL MAIN FUNCTION
main(url)
