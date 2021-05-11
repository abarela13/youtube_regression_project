from bs4 import BeautifulSoup
from math import ceil
import requests
import pickle

def retrieve_channels(url):
    with open('data/channels_dict', "rb") as f:
        channels_dict = pickle.load(f)

    data = requests.get(url)

    # load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    content = soup.findAll('div', {'class': 'row'})[1]

    for channel in content.find_all('div', {'class': 'channel'}):
        if channel not in channels_dict.keys():
            id = channel.find('h4').find('a')['href'][31:]
            channels_dict[id] = 'pending'

    # Save page dictionary object
    with open('data/channels_dict', "wb") as f:
        pickle.dump(channels_dict, f)

def retrieve_results(result):
    # define base url
    url = f'https://channelcrawler.com/eng/results/{result}/page:1'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    pages = ceil(int(soup.find('h3', {'class': 'results-title'}).text.strip().split(' ')[0]) / 20)
    
    for page in range(1, pages+1):
        retrieve_channels(f'https://channelcrawler.com/eng/results/{result}/page:{page}')
        print(f'page {page} completed')

results_list = [1688649, 1688651, 1688655, 1688656]

for result in results_list:
    retrieve_results(result)