
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
f = open('sportsroutes.txt', 'w+')
f.write('')
f.close()
for x in s:
  f = open(x + ".html","w+")
  name = x.replace('-',' ').capitalize()
  st_list = []
  st_list.append('<!DOCTYPE html>\n')
  st_list.append('<html>\n')
  st_list.append('<head>\n')
  st_list.append('<title>'+ name +'</title>\n')
  st_list.append('	<meta charset="utf-8">\n')
  st_list.append('  <meta name="viewport" content="width=device-width, initial-scale=1">\n')
  st_list.append('	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">\n')
  st_list.append('  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\n')
  st_list.append('  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>\n')
  st_list.append('	<title></title>\n')
  st_list.append('</head>\n')
  st_list.append('<li><a href="sports/'+ x +'"> '+ name +'</a></li>\n')
  st_list.append('<body>\n')
  st_list.append('<nav class="navbar navbar-inverse navbar-fixed-top navbar-expand-lg justify-content-between">\n')
  st_list.append('	<div class="container-fluid">\n')
  st_list.append('		<div class="navbar-header">\n')
  st_list.append('			<a class="navbar-brand" href="#"> ' + name + '</a>\n')
  st_list.append('		</div>\n')
  st_list.append('	    <ul class="nav navbar-nav">\n')
  st_list.append('	<li><a href="sports"> Back </a></li>\n')
  st_list.append('</body>\n')
  st_list.append('</html>)')
  st = ''.join(st_list)
  f.write(st)
  f.close()
  f = open('sportsroutes.txt', 'a+')
  st_list = []
  st_list.append("@app.route('/sports/"+ x +"')\n")
  st_list.append("def " + x + "():\n")
  st_list.append("  return render_template(\n")
  st_list.append("          'sports/" + x + ".html')\n")
  st = ''.join(st_list)
  f.write(st)
  f.close()
