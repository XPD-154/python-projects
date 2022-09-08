import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('ambassadorj.boy@gmail.com', '')

server.sendmail('ambassadorj.boy@gmail.com', 'igho.iruesiri@bemas.biz', 'testing python sendmail')

print('Mail sent')
