print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/Lab5/stepper_control.cgi" method="POST">')

print('  <input type="submit" name="zeroing" value="zeroing"> zero stepper <br><br>')

print('<input type="range" name="slider1" min="0" max="360" value="%s"><br>' % s1)
print('<input type="submit" value="apply stepper angle">')
print('</form>')
print('Angle = %s' % s1)
print('</html>')