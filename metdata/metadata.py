#!/usr/bin/env python

import requests
import json
import sys

#Declare global variable for meta URL and dictionary

metaurl = 'http://169.254.169.254/latest/meta-data/'
metadict = {}

# Converts AWS EC2 instance metadata to a dictionary
def load():
    datacrawl(metaurl,metadict)
    return metadict

# Gets value for a key
def printValue(key):
    datacrawl(metaurl,metadict)
    print( key + ":" + str(metadict[key]))


def datacrawl(url,d):
    r = requests.get(url)
    if r.status_code == 404:
        return

    for l in r.text.split('\n'):
        if not l: # "instance-identity/\n" case
            continue
        newurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/'
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            datacrawl(newurl, d[newkey])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None

if __name__ == '__main__':

    if (len(sys.argv) == 1):
      print(json.dumps(load()))
    elif (len(sys.argv) == 2):
      printValue(sys.argv[1])
    else:
      sys.exit(1)
