flag = False;
s = [];
f = open("sports.json", "r")
for x in f:
  if 'flag' in x:
      x = x.split('\\\"')[1]
      x = x[1:]
      x = x.replace('-/-','-')
      s.append(x)
f.close()
#clearing files
f = open('sportsroutes.txt', 'w+')
f.write('')
f.close()
f = open('sportshtml.txt', 'w+')
f.write('')
f.close()
for x in s:
  #writing individual sports files
  f = open(x + ".html","w+")
  name = x.replace('-',' ').capitalize()
  pyname = x.replace('-','_')
  st_list = []
  st_list.append('<!DOCTYPE html>')
  st_list.append('<html>')
  st_list.append('<head>')
  st_list.append('<title>'+ name +'</title>')
  st_list.append('	<meta charset="utf-8">')
  st_list.append('  <meta name="viewport" content="width=device-width, initial-scale=1">')
  st_list.append('	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
  st_list.append('  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>')
  st_list.append('  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
  st_list.append('	<title></title>')
  st_list.append('</head>')
  st_list.append('<li><a href="sports/'+ x +'"> '+ name +'</a></li>')
  st_list.append('<body>')
  st_list.append('<nav class="navbar navbar-inverse navbar-fixed-top navbar-expand-lg justify-content-between">')
  st_list.append('	<div class="container-fluid">')
  st_list.append('		<div class="navbar-header">')
  st_list.append('			<a class="navbar-brand" href="#"> ' + name + '</a>')
  st_list.append('		</div>')
  st_list.append('	    <ul class="nav navbar-nav">')
  st_list.append('	<li><a href="/sports"> Back </a></li>')
  st_list.append('</nav>')
  st_list.append('<br><br><br><br>')
  st_list.append('<img src="imgs/'+x+'.png">')
  st_list.append('</body>')
  st_list.append('</html>)')
  st = '\n'.join(st_list)
  f.write(st)
  f.close()
  # writing routing info to add to main.py
  f = open('sportsroutes.txt', 'a+')
  st_list = []
  st_list.append("@app.route('/sports/"+ x +"')")
  st_list.append("def " + pyname + "():")
  st_list.append("  return render_template(")
  st_list.append("          'sports/" + x + ".html')\n\n")
  st = '\n'.join(st_list)
  f.write(st)
  # writing html to add links to sports.html
  f = open('sportshtml.txt', 'a+')
  st = '<a href="sports/' + x + '">' + name + '</a><br>\n'
  f.write(st)
  f.close()
