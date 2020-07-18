import feedparser

News = feedparser.parse('https://feeds.feedburner.com/ndtvnews-latest')

Myfile = open('MyNewsFeed.txt','w')

Myfile.write("Welcome to the NewsFeed V1\n")
Myfile.write("By Saravanan T")
Myfile.write ("\n\n")
Myfile.write (News['feed']['title'])
Myfile.write ("\n")
Myfile.write (News['feed']['link'])
Myfile.write ("\n\n")
items = len(News['entries'])
#Myfile.write (News['entries'][0])
Myfile.write ("Today's Headlines are : " )
Myfile.write ("\n\n")

for i in range(items):
    temp = 1 + i
    Myfile.write (str(temp) + '. ' + News['entries'][i]['title'])
    Myfile.write ("\n\n")
    Myfile.write (News['entries'][i]['summary'])
    Myfile.write ("\n\n")
    Myfile.write ("Learn More At : " + News['entries'][i]['link'])
    Myfile.write ("\n\n")
    Myfile.write ("Article Published on : " + News['entries'][i]['published'])
    Myfile.write ("\n\n")
    Myfile.write("------------------------------------------------------------------------------------------------")
    Myfile.write ("\n\n")

Myfile.close()