import requests

download_url = 'https://projects.fivethirtyeight.com/mlb-api/mlb_elo.csv'
target_path = 'mlb_elo.csv'


response = requests.get(download_url)#download the page
response.raise_for_status() #check for download success

with open(target_path,'wb') as my_file:
    my_file.write(response.content)
print("Finished downloading. Thank you.")
