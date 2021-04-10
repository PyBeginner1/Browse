import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = 'https://images.google.com/'
browser.open(url)
print(browser.get_url())

#get html
browser.get_current_page()
#target search field
browser.select_form()                           #target all input tags
browser.get_current_form().print_summary()      #displays all input fields

#putting cat in search field
search_term =  'cat'
browser["q"] = search_term                      #q =name of search field

#hitting submit
browser.launch_browser()                        #types cat inside search
response = browser.submit_selected()            #hit submit button

print("new url is", browser.get_url())
print("response is", response.text[:500])

#new url
new_url = browser.get_url()
browser.open(new_url)

#get html of new url
page = browser.get_current_page()
all_images = page.find_all('img')

image_source = []
for image in all_images:
    image = image.get("src")
    image_source.append(image)

image_source[5:]



