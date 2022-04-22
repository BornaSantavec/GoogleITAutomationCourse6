#! /usr/bin/env python3

import os
import requests

home_dir = "/data/feedback/"
Files = os.listdir(home_dir)

feedback_list = []

for feedback in Files:
  with open (home_dir + feedback, "r") as file:
   feedback_list.append({"title": file.readline().rstrip("\n"),"name": file.readline().rstrip("\n"), "date": file.readline().rstrip("\n"), "feedback": file.readline().rstrip("\n")})

for item in feedback_list:
  response = requests.post("http://34.135.95.195/feedback/", json=item)
  response.raise_for_status()
  print ("Added feedback ID: {}",format(response.json()["id"]))
