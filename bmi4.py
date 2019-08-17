#!C:\Users\myung\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb

form = cgi.FieldStorage()

weight = form.getvalue('weight')
height = form.getvalue('height')
FTO= form.getvalue('FTO')
MC4R = form.getvalue('MC4R')
BDNF = form.getvalue('BDNF')
GNPDA2 = form.getvalue('GNPDA2')
NEGR1 = form.getvalue('NEGR1')
SH2B1 = form.getvalue('SH2B1')
ETV5 = form.getvalue('ETV5')
KCTD15 = form.getvalue('KCTD15')
SEC16B = form.getvalue('SEC16B')
TFAP2B = form.getvalue('TEAP2B')
FAIM2 = form.getvalue('FAIM2')

bmi = float(weight) / ( ( float(height) / 100 )**2 )

bmi_type = ''

if bmi < 25:
        bmi_type = 'Normal'
elif bmi >= 25 and bmi < 30:
        bmi_type = 'Overweight'
else:
        bmi_type = 'Severe'

print( "Content-type:text/html\r\n\r\n")
print( "<html>")

print( "<head>")
print( "<title>BMI Result</title>")
print("</head>")

print( '<img src=http://www.cpbmi.or.kr/main.jpg width="500" height="110">')
print( "<br />")
print( "<h2>BMI Result</h2>")

print( "<body>")
print( "Your Input : weight " + weight + ", height " + height)
print( "<br />")
print( "BMI : %.2f" % ( bmi ))
print( "<br />")
print( "BMI Type : " + bmi_type)
print( "<p>")
print( "<h2>Check Result</h2>")
print( "<font color='blue'><b>You checked</b></font><br>")

print("FTO : "+FTO+ "<br>")
print("MCR4 : "+MC4R+ "<br>")
print("BDNF : "+BDNF+ "<br>")
print("GNPDA2 : "+GNPDA2+ "<br>")
print("NEGR1 : "+NEGR1+ "<br>")
print("SH2B1 : "+SH2B1+ "<br>")
print("ETV5 : "+ETV5+ "<br>")
print("KCTD15 : "+KCTD15+ "<br>")
print("SEC16B : "+SEC16B+ "<br>")



Risk_score = float(FTO) + float(MC4R) + float(BDNF) + float(GNPDA2) + float(NEGR1) + float(SH2B1) + float(ETV5) + float(KCTD15) + float(SEC16B)
print("SNP Risk Score : %.0f" %(Risk_score))
print( "<br />")




print( "</body>")

print( "</html>")
