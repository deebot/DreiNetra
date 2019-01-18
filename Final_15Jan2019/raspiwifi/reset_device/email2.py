import smtplib
import logging
from time import sleep, localtime
import dynamic as dyn


def bot_mailer():
	email_list = dyn.email_extractor()
	sleep(20)
	LOG_FILENAME = 'example.log'
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	Confirmation=False # it controls sending of confirmation. So that email about configuration is sent only once
	content='heheke hdhkd'
	mail = smtplib.SMTP('smtp.gmail.com',587)
	while True:
		if Confirmation == False:
			mail.ehlo()
			mail.starttls()
			mail.login('picamerax@gmail.com', 'N1kk0N1kk0')
			for mail_ in email_list:
				print(mail_)
				mail.sendmail('picamerax@gmail.com', mail_, content)
			mail.close()
			currenttime=localtime()
			logging.debug('This message should go to the log file hr{} sec{} '.format(currenttime[3],currenttime[4]))
			Confirmation= True
		else:
			pass

bot_mailer()
sleep(10)
bot_mailer()
sleep(10)
bot_mailer()
