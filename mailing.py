# Sending function
import smtplib
import keys

# Email module
from email.mime.text import MIMEText

# These work, enjoy your new gmail account
donut = "willycheestick6@gmail.com"
pwd = "raymondchee"

def sendEmail(txt, to, firstname, lastname):

	print("Sending email...\n")
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(keys.username(), keys.password())

	header = "To: " + to + "\n" + "From: " + donut
	header = header + "\n" + "Subject: Donut Reply :-)\n"

	msg = header + "\n" + txt + "\n\n"
	smtpserver.sendmail(donut, to, msg)
	smtpserver.close()

	return
