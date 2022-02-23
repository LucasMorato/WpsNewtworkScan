# ------------------------------------------------
# Importante: THIS SCRIPT SHOULD BE USED WITH CAUTION. OVERLOADING GOOGLE SERVERS MAY CAUSE TEMPORARY BLOCKING OF YOUR IP ADDRESS
# You must have installed Wpscan By WPScan Team https://github.com/wpscanteam/wpscan before running the script
# ------------------------------------------------

from googlesearch import search
import urllib.parse
import sys
import os

print('\n')
print('█░█░█ █▀█   █▄░█ █▀▀ ▀█▀ █░█░█ █▀█ █▀█ █▄▀   █▀ █▀▀ ▄▀█ █▄░█')
print('▀▄▀▄▀ █▀▀   █░▀█ ██▄ ░█░ ▀▄▀▄▀ █▄█ █▀▄ █░█   ▄█ █▄▄ █▀█ █░▀█')
print('\n')
print('by Lucas F. Morato')
print('Version 1.0')
print('\n')

keyword_search = "brasilia" ############# change here
country = "org.br" ############# change here
token = "" ############# change here | you can get a plan here: https://wpscan.com/pricing

# stores the search for websites
palavra_chave = f'site:"{country}" intext:"{keyword_search}" inurl:wp-content/'

# search for addresses and send to a tmp file
try:
  print("Searching Url's...")
  sys.stdout = open("urls.tmp", "w")
  for urls in search(palavra_chave, num=5, stop=5, pause=4): # IMPORTANT: DO NOT DECREASE THE "PAUSE TIME" TO LESS THAN 4
    print(urls)

  sys.stdout.close()
except ImportError:
  print('Google Database connection error!')

# filters the website address (url.com.br for exemple)
new_urls = []

with open("urls.tmp", "r") as urls_file:
    old_urls = urls_file.readlines()

for line in old_urls:
    url_parts = urllib.parse.urlparse(line)
    proc_url = "{uri.scheme}://{uri.netloc}/\n".format(uri=url_parts)
    new_urls.append(proc_url)

with open("urls.tmp", "w") as urls_file:
    urls_file.writelines(new_urls)

# remove duplicated urls
a_file = open("urls.tmp", "r")
writeFile = open("updatedUrls.tmp", "w")
tmp = set()
for txtLine in a_file:
    if txtLine not in tmp:
        writeFile.write(txtLine)
        tmp.add(txtLine)
a_file.close()
writeFile.close()
os.remove("urls.tmp")

# run wpscan and show only vulnerabilities

with open("updatedUrls.tmp", "r") as h:
  for line in h:
    wpsfile = line.strip()
    os.system(f"wpscan --url {wpsfile} --api-token {token} --random-user-agent --ignore-main-redirect | grep -i '[!]\| url:\|started\|Aborted' | grep -v 'Effective\|style\|WARNING\|The version'") 
