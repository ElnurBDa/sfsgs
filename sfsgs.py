'''
Search Files in Subdomains with Google Search

'''
import requests
from googlesearch import search

ext = 'doc'
count = 0
query = f"site:edu.az ext:{ext}"
list_text = ''

for j in search(query, tld="co.in", pause=2):
    file_name = str(count) + "." + ext
    row = file_name + " is " + j
    print(row)
    list_text += row
    response = requests.get(j)
    open(file_name, "wb").write(response.content)
    count+=1


open("list", "wb").write(list_text)
