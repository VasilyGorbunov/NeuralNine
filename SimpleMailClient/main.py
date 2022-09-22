import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.mailtrap.io', 2525)
server.ehlo()

server.login("776eadbd8f9bb1", "51d4e9a292ef4c")

msg = MIMEMultipart()
msg['From'] = 'VasilyGorbunov'
msg['To'] = 'app@app.com'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = "coding.jpg"
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('admin@app.com', 'app@app.com', text)