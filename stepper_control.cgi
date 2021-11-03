#!/usr/bin/python37all

import cgi

datain = cgi.FieldStorage()

import json

s1 = datain.getvalue('slider1')
b1 = datain.getvalue('zeroing')

data = {'slider1':s1, 'zeroing':b1}

with open("Lab5.txt", 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')

print('<input type="hidden" name="reset" value="1">')
print('<input type="hidden" name="slider1" value="0">')
print('<input type="submit" name="zeroing" value="zero stepper"> <br><br>')

print('</form>')

print('<br>')

print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')

print('<input type="hidden" name="reset" value="0">')
print('<input type="range" name="slider1" min="0" max="360" value="%s"><br>' % s1)
print('<input type="submit" value="apply stepper angle">')

print('</form>')
print('Angle = %s' % s1)
print('</html>')
