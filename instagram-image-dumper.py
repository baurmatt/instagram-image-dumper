#!/usr/bin/env python
# vim: tabstop=2 noexpandtab

"""
 Created by baurmatt@2014
 instagram-image-dumper.py
 Description: Script which downloads all images from Instagram for a specified user
"""

import sys, argparse, tempfile, urllib2, json, os
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--downloadpath', help='The path you wish to download all images.')
parser.add_argument('-u', '--username', help='The name of the user whose images you want to download', required=True)

args = parser.parse_args()

if args.downloadpath is None:
  args.downloadpath = tempfile.mkdtemp(prefix='instagramDump_')

print "Username:      " + args.username
print "Download path: " + args.downloadpath

##############################################
#                                            #
# Nothing to change for you below this line! #
#                                            #
##############################################

defaultURL = "http://instagram.com/" + args.username + "/media"

def downloadImages(jsonItemList):
  for item in jsonItemList:
    imageURL = item['images']['standard_resolution']['url']
    imageDownloadPath = args.downloadpath + "/" + imageURL.split('/')[-1]
    if os.path.isfile(imageDownloadPath):
      print "This is strange, this file already exists... " + imageDownloadPath
    file = open(imageDownloadPath, 'wb')
    file.write(urllib2.urlopen(imageURL).read())
    file.close()
    print "Downloaded: " + imageDownloadPath

# Get all images
round = 0
while round != -1:
  if round == 0:
    URL = defaultURL
    round += 1
  else:
    URL = defaultURL + "?max_id=" + jsonData['items'][-1]['id']

  rawContent = urllib2.urlopen(URL).read()
  jsonData = json.loads(rawContent)
  downloadImages(jsonData['items'])
  
  if jsonData['more_available'] == False:
    round = -1
