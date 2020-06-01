import random
import string
import sys

import requests


# Variables
host = "http://localhost:8081"


if __name__ == '__main__':
    # Get the map informations
    user = sys.argv[1]
    #pw = sys.argv[2]
    pw = "7b13984732384f60854f0fe451d01241"
    
    end = requests.put(host + '/game/endturn' , auth=(user, pw))
    print(end.status_code)
    if(end.status_code != 200):
        print(end.json())
