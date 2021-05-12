from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sys
import json
import requests
from webClass import *
#from notifications import *
from random import randrange
import time
import csv

class graphicsCard:
    def __init__(self, name, url, sitename):
        self.name = name
        self.url = url
        self.sitename = sitename

cards = []

with open ("grafikkort.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_counter = 0
    for row in csv_reader:
        if line_counter == 0:
            line_counter += 1
        else:
            cards.append(graphicsCard(row[0], row[1], row[2]))
            line_counter += 1

running = True
# Time_between_cycles = 30 #seconds

while(running):
    time.sleep(30*1) #30 seconds wait, goal is 10 minutes but I don't have the patience when testing
    for card in cards:
        if card.sitename == "webhallen": #javascript exception
            webhallenFunc(card.url,card.name)
        else:
            if card.sitename == "inet":
                inetFunc(card.url,card.name)
            elif card.sitename == "proshop":
                proshopFunc(card.url,card.name)
                
