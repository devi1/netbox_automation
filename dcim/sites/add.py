#!/usr/bin/python3

from jinja2 import Template, Environment, FileSystemLoader
import requests

site_count = 150
url = 'http://10.10.10.10:32769/api/dcim/sites/'
headers = {'content-type': 'application/json', 'Authorization': 'Token QFS2t4353qRwsr2qwrfDGWFgvw4524'}

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template  = env.get_template('template.j2')

for i in range(site_count):
  payload = template.render(i=i)
  r = requests.post(url, data=payload, headers=headers)
  print(r.text)
