__author__ = 'jordankidd'

from urllib import request
import json


def main():
    again = True
    while again == True:
        subr = input("\nPlease enter the subreddit name to view: ")
        url = "http://www.reddit.com/r/" + str(subr) + "/.json"
        error = False
        
        try:
            jsonStr = request.urlopen(url).read().decode("utf-8")
        except:
            error = True
            print("Error occurred with data fetch. Is the subreddit spelled correctly?")

        if error == False:
            jsonObs = json.loads(jsonStr)
            posts = jsonObs['data']['children']
            if len(posts) > 5:
                for i in range(1, 6):
                    post = posts[i]
                    title = post['data']['title']
                    ups = post['data']['ups']
                    print("#" + str(i) + ": " + title + ". UPS: " + str(ups))
                more = input("Look up more? y / n\n")
                if more == 'y':
                    again = True
                else:
                    again = False
            else:
                print("That subreddit was not found.")
                again = True


if __name__ == '__main__':
    main()
    print("Goodbye.")
