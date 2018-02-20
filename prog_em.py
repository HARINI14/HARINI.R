# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("harini.rajanna14@gmail.com", "9742028299")
 
# message to be sent
message = "hello"
 
# sending the mail
s.sendmail("harini.rajanna14@gmail.com", "harini.rajanna14@gmail.com", message)
 
# terminating the session
s.quit()
"print" 
