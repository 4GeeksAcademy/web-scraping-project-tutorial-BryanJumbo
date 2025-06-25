import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

URL = "https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records"

response = requests.get(URL)

if response.status_code == 200:
  html_parseado = BeautifulSoup(response.text, "html.parser")


##html_parseado.find("div")

p_response = pandas.read_html(URL)
contador = 0
for tabla in p_response:
  tabla_limpia = tabla.dropna(how='all')  
  tabla_limpia = tabla_limpia.dropna(axis=1, how='all')  
  ##if not tabla_limpia.empty:
    ##print(tabla_limpia.replace("B", "", regex=True).replace("$", "", regex=True))
  print(tabla_limpia)
