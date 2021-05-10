from bs4 import BeautifulSoup
from os import path, listdir
import requests
import pickle
import time

def generate_dict(url, file_name):
    data = requests.get(url)

    # load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    channel_dictionary = {}

    content = soup.findAll('div', {'class': 'row'})[1]

    for channel in content.find_all('div', {'class': 'channel'}):
        title = channel.find('h4').find('a')['title']
        id = channel.find('h4').find('a')['href'][31:]

        channel_dictionary[id] = title

    # Save page dictionary object
    with open(file_name, "wb") as f:
        pickle.dump(channel_dictionary, f)

def retrieve_results(results, pages):
    # define base url
    url = f'https://channelcrawler.com/eng/results/{results}/page:'
    
    # define downloads folder directory
    file_root = f'download/channelcrawler/{results}'

    for page in range(1, pages+1):
        # generate file name
        file_name = f'{file_root}_{str(page).zfill(2)}'

        if not path.isfile(file_name):
            generate_dict(f'{url}{page}', file_name)

            #Wait for page to load
            time.sleep(20)

def read_pickle(file):
    # Read the soup object from a file
    with open(file, "rb") as f:
        return pickle.load(f)

def channels_list():
    download_directory = 'download/channelcrawler/'

    result = []

    for file in listdir(download_directory):
        f = path.join(download_directory, file)

        if path.isfile(f):
            try:
                 result.extend(list(read_pickle(f).keys()))
            except:
                raise Exception('Filetype was invalid')

    
    # Save page dictionary object
    with open('download/channelcrawler/merged', "wb") as f:
        pickle.dump(result, f)
    
    return result

# print(list(read_pickle('download/channelcrawler/1677375_01').keys()))

print(channels_list())


# retrieve_results(1677375, 50)