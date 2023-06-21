import urllib.request
import sys
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=P&Season=2022-23&SeasonType=Regular%20Season&Sorter=DATE"


r = requests.get(URL)
