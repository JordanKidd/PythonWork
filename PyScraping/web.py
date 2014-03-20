__author__ = 'jordankidd'

from bs4 import BeautifulSoup
from urllib import request as req
import time


def main():
    print("Web Scraping Personal Project:")
    again = ""
    while True:
        mainmenu()
        again = input("\nAgain? 'y' / 'n'\n>>> ")
        if again == 'n':
            print("Goodbye.")
            break


def mainmenu():
    dict = {"1" : "http://www.reddit.com/r/programming", "2" : "http://www.reddit.com/r/technology",
            "3" : "https://news.ycombinator.com/", "4" : "TODO"}
    resp = input("\nWebsites:\n1 = /r/programming\n2 = /r/technology\n3 = HackerNews\n>>> ")
    ok = False

    try:
        url = dict[resp]
        funcs = {
            "1" : prog,
            "2" : tech,
            "3" : hnews
        }
        ok = True
    except:
        print("Error on input")

    if ok:
        funcs[resp](url)


def prog(url):
    """/r/programming function"""
    ok = False
    start = time.time()
    try:
        data = req.urlopen(url)
        soup = BeautifulSoup(data)
        ok = True
    except:
        print("\nError on data retrieval.")
    if ok:
        limiter = 0
        print("\n/r/programming:")
        for links in soup.find_all('a', attrs = {'class' : 'title '}):
            if limiter < 6:  #display limiter
                print("\t" + links.text)
                limiter += 1
            else:
                end = time.time()
                print("Request time: " + str(round((end - start), 4)) + " second(s).")
                break


def tech(url):
    """/r/technology function"""
    ok = False
    start = time.time()
    try:
        data = req.urlopen(url)
        soup = BeautifulSoup(data)
        ok = True
    except:
        print("\nError on data retrieval.")
    if ok:
        limiter = 0
        print("\n/r/tech:")
        for links in soup.find_all('a', attrs = {'class' : 'title '}):
            if limiter < 6:
                print("\t" + links.text)
                limiter += 1
            else:
                end = time.time()
                print("Request time: " + str(round((end - start), 4)) + " second(s).")
                break


def hnews(url):
    """hacker news function"""
    raise NotImplementedError("Not done!")


if __name__ == '__main__':
    main()
