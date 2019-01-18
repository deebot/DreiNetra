import smtplib
from time import sleep, localtime
import dynamic as dyn
import MotionMod

def bot_detection():
	email_list = dyn.email_extractor()
	motionState=False
	content='Hi. Your camera has been configured in Security Camera Mode. You will receive intrution alerts on this Email Address'
	mail = smtplib.SMTP('smtp.gmail.com',587)
	while True:
		motionState=MotionMod.motion()
		
		if motionState==True:
			
			mail.ehlo()
			mail.starttls()
			mail.login('picamerax@gmail.com', 'N1kk0N1kk0')
			for mail_ in email_list:
				print(mail_)
				mail.sendmail('picamerax@gmail.com', mail_, content)
			mail.close()
			currenttime=localtime()
#			logging.debug('This message should go to the log file hr{} sec{} '.format(currenttime[3],currenttime[4]))
			Confirmation= True
			print("detected")
			sleep(5)
		else:
			pass
			

bot_detection()