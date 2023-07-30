'''
Search Files in Subdomains with Google Search

'''
response = requests.get(URL)
from googlesearch import search

query = "site:bhos.edu.az \"Elnur Badalov\" ext:pdf"

for j in search(query, tld="co.in", pause=2):
    print(j)

