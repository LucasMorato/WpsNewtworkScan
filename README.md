# WP Network Scan

<img src="https://i.postimg.cc/2848fzvy/download.png" alt="wpnetworkscan">

This script was developed with the intention of improving the internet in order to find vulnerabilities in an automated way and report to the respective owners the flaw to be corrected.

The script searches for wordpress sites on the internet according to the settings you establish.
This script is not for personal profit and uses Wpscan By WPScan Team. You must create an account on their website: https://wpscan.com/ to get your token.

The FREE account is limited to a few scans per day, however, you have the option to search for the best plan for you.

Use it wisely and for good.
By using this script you are agreeing that any misuse is not my responsibility.

How to use:
After downloading and saving the script on your Linux, with a text editor (like nano) edit the commented lines with #:
```
nano wpnetworkscan.py
```
```
keyword_search = "brasilia" # change here
country = "org.br" # change here
token = "F91V12GFJNFSJSFOM8LdSHtWayd8PrT6VTiH19FU8" # change here | you can get a plan here: https://wpscan.com/pricing
```

Also change the number of sites you want to search in the `"num="` argument. Noting that the more sites searched at a time, the greater the chance that Google will temporarily block your IP.
```
for urls in search(keyword, num=5, stop=5, pause=4)
```

After changing the lines run with the command:
```
python3 wpnetworkscan.py
```

The script takes a while to run depending on the number of sites that are fetched.
