flag = False
s = []
f = open("sports.json", "r")
for x in f:
  if 'flag' in x:
      x = x.split('\\\"')[1]
      x = x[1:]
      x = x.replace('-/-','-')
      s.append(x)
f.close()
#clearing files
f = open('sportshtml.txt', 'w+')
f.write('')
f.close()
f = open('sport.json', 'w+')
f.write('[')
f.close()
banners = []
f = open("banners.json", "r")
for x in f:
  x = x.split()[0]
  banners.append(x)
f.close()
banner = 0
for x in s:
  name = x.replace('-',' ').capitalize()
  f = open('sport.json', 'a+')
  st_list = []
  st_list.append('{"name":"' + name)
  st_list.append('","ref":"' + x)
  st_list.append('","img":"imgs/' + x + '.png')
  st_list.append('","banner":"' + banners[banner])
  st_list.append('"},')
  st = ''.join(st_list)
  f.write(st)
  f.close()
  # writing html to add links to sports.html
  f = open('sportshtml.txt', 'a+')
  st = '<a href="sports/' + x + '">' + name + '</a><br>\n'
  f.write(st)
  f.close()
  banner += 1
f = open('sport.json', 'a+')
#need to remove comma after running this
st = ']'
f.write(st)
f.close()
