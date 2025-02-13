#!/Users/eimansherzada/anaconda3/bin/python3

import os

fav_season = input("What is your favorite season? ")
fav_language = input("What is your language to code in? ")
bev_choice = input("Coffee or tea? ")

os.environ["FAV_SEASON"] = fav_season
os.environ["FAV_LANGUAGE"] = fav_language
os.environ["BEV_CHOICE"] = bev_choice

print(os.getenv("FAV_SEASON"))
print(os.getenv("FAV_LANGUAGE"))
print(os.getenv("BEV_CHOICE"))
