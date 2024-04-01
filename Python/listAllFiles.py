import requests
from bs4 import BeautifulSoup

#get html data from url
def list_all_files(url):
    req= requests.get(url, verify=False).content

    my_json = req.decode("utf-8").replace("'", '"')
    return BeautifulSoup(my_json, 'html.parser')

# get values from html data
def get_all_sub_folders(html_data, file_object):
    endpoint_suffix=[]
    for each_div in html_data.find_all('div',class_='main'):
        for each_attr in each_div.find_all('a'):
            # if the link is a folder, we will add it to a suffix list
            if each_attr['href'][:-1].isalnum():
                endpoint_suffix.append(each_attr['href'])
            # if link is a terminal end point and has a file with extention
            else:
                if each_attr['href'].find('.') > -1:
                    file_object.write(each_attr['href']+'\n')
    return (endpoint_suffix)
