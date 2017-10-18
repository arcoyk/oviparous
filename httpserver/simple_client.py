import urllib.request
with urllib.request.urlopen('http://localhost:8000/candidate') as res:
  html = res.read().decode('utf-8')
  print(html)
