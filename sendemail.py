#make sure you allow less secure app access in google security https://myaccount.google.com/security
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#email address of sender
fromaddress = "email"
#email address of recipient 
toaddress = "email"

email = MIMEMultipart()

email['From'] = fromaddress
email['To'] = toaddress
#subject line
email['Subject'] = "Subject"
#stuff you want in the body
body = ""

email.attach(MIMEText(body, 'plain'))

filename = "filetobesend.txt"
# has to use raw string aka foward slashes or double slashes
attachment = open('put directory in here \filetobesend.txt', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

email.attach(part)
#connects to smtp server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#logs into gmail account
server.login(fromaddress, "password")
text = email.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()
