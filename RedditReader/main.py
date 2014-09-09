__author__ = 'jordankidd'

from urllib import request
import json

def main():
    again = True
    while again == True:
        subr = input("\nPlease enter the subreddit name to view: ")
        url = "http://www.reddit.com/r/" + str(subr) + "/.json"
        jsonStr = request.urlopen(url).read().decode("utf-8")
        jsonObs = json.loads(jsonStr)
        posts = jsonObs['data']['children']
        for i in range(1, 6):
            post = posts[i]
            title = post['data']['title']
            print("#" + str(i) + ": " + title)
        more = input("Look up more? y / n\n")
        if more == 'y':
            again = True
        else:
            again = False

if __name__ == '__main__':
    main()