import requests, bs4, webbrowser, sys 

if len(sys.argv) > 1:
    keywords = "+".join(sys.argv[1:])
else:
    print("You need to provide searching keywords as arguments.")

res = requests.get("https://www.google.com/search?q=" + keywords)
ressoup = bs4.BeautifulSoup(res.text, 'lxml')

anchors = ressoup.select('a') # the book recommends ".r a". but the 'r' class is missing in today's Google.
count = min(5, len(anchors))
for i in range(count):
    print(webbrowser.open(anchors[i].get('href')))

# this script doesn't actually work, as I couldn't found a way to select only
# result anchor elements, so every href valid or not will try to open on the browser.
# This can be partially solved by verifying that every href leads to a valid (HTTP 200 response) site.
