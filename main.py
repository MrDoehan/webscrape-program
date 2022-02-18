import requests

from bs4 import BeautifulSoup
import time

while True:
  org = requests.get("https://prac-resume.mrdoe.repl.co").text
  html = BeautifulSoup(org, "html.parser")
  tag = input("What is the tag: ")
  whole = html.find_all(f'{tag}')
  for whole in whole:
    names = whole.contents[0]
    print(names)
    time.sleep(0.25)
  cont = input("Do you want to continue? y/n")
  if cont == "y":
    True
  else: break  
