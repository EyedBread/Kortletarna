from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sys
import json
import requests
from webFuncs import *
from gui import *
# from notifications import *
from random import randrange
import time
import csv


class graphicsCard:
    def __init__(self, name, manufacturer, model, url, sitename):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.url = url
        self.sitename = sitename

cards = []

with open ("grafikkort.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_counter = 0
    for row in csv_reader:
        if line_counter == 0:
            line_counter += 1
        elif row[0]== "#":
            line_counter +=1
        else:
            cards.append(graphicsCard(row[0], row[1], row[2], row[3], row[4]))
            line_counter += 1

running = True
    # Time_between_cycles = 30 #seconds

while(running):
    for card in cards:
        if card.sitename == "webhallen": #javascript exception
            webhallenFunc(card)
        else:
            if card.sitename == "inet":
                inetFunc(card)
            elif card.sitename == "proshop":
                proshopFunc(card)
            elif card.sitename == "":
                #do nothing
                continue
            else:
                print('Could not identify sitename!')
        time.sleep(0.5)
    time.sleep(10) #60 seconds wait, goal is 10 minutes but I don't have the patience when testing