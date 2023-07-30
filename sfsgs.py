'''
Search Files in Subdomains with Google Search

'''
import requests
from googlesearch import search

# exts = ['xls','xlsx','doc','docx','csv', txt] 
# exts = ['log', 'txt', 'conf', 'cnf', 'ini', 'env', 'sh', 'bak', 'backup', 'swp', 'old', '~', 'git', 'svn', 'htpasswd', 'htaccess']
# exts = ['pdf']
exts = ['txt']
list_text = ''

for ext in exts:
    print(f"\next:{ext}")
    count = 0
    query = f"site:edu.az ext:{ext}"

    for j in search(query, start=count, tld="co.in", pause=2):
        file_name = str(count) + "." + ext
        row = file_name + " is " + j 
        print(row)
        list_text += row + "\n"
        response = requests.get(j)
        open(file_name, "wb").write(response.content)
        count+=1


open("list.txt", "w").write(list_text)
