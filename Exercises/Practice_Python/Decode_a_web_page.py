"""
Use the BeautifulSoup and requests Python packages to print out
a list of all the article titles on the New Yourk Times homepage.
"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
coverage = soup.find_all("h2",class_="css-1vvhd4r esl82me0")

coverage_list = []
for i in range(len(coverage)):
    coverage_list.append(coverage[i].get_text())

print('Little class:\n')
pp(coverage_list)

#head_line = soup.find_all('h2',class_=".esl82me1")
head_line = soup.select("[class~=esl82me1]")
head_line_list = []
for i in range(len(head_line)):
    head_line_list.append(head_line[i].get_text())

print('Head Line List:\n')
pp(head_line_list)


# from https://gist.github.com/M8T3/7ac7ab09236cfa4ec183305396a29864
title1 = soup.find_all('span')   #the tag for the headline, can't use class_="balancedHeadline" to search
'''
title2 = soup.find_all('h2')    #not included
'''
all_title = title1 #+ title2
articles = []
for item in all_title:
        articles.append(item.get_text())

articles = list(filter(None, articles))
for item in articles:
    print(item)
