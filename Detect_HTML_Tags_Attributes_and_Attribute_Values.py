from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

tc = int(input())
html = ""
while tc > 0:

    html+=input()
    html+='\n'

    tc-=1
now = MyHTMLParser()
now.feed(html)
now.close()