from requests_html import HTMLSession

session = HTMLSession()

#r = session.get('https://python.org/')

#print(r.html.links)
#print(r.html.absolute_links)

#about = r.html.find('#about', first=False)
## first를 False로 하면 리스트로 만들어줌
#print(about[0].text)
#print(about.text)
#print(about[0].html)
#about.find('a')



r = session.get('http://html.python-requests.org/')



box = r.html.find('.highlight', first=True)

print(box.html)

    