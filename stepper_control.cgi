print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/Lab5/stepper_control.cgi" method="POST">')

print('  <input type="submit" name="zeroing" value="zeroing"> Zero Stepper <br><br>')

print('<input type="range" name="slider1" min="0" max="360" value="%s"><br>' % s1)
print('<input type="submit" value="Apply Stepper Angle">')
print('</form>')
print('Angle = %s' % s1)
print('</html>')