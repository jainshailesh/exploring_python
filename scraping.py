import re, urllib

root = "http://www.google.com"
for url in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(root).read(), re.I):
    if url[0] in ['/']:
        url = root + url
    print "parent: ", url
    source = ''
    try:
        source = urllib.urlopen(url).read()
    except :
        print "Caught exception on url: ", url
    for child in re.findall('''href=["'](.[^"']+)["']''', source, re.I):
        print "child: ", child
