from cgitb import html
from email import message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sendMail(toMail,subject,content):
    fromMail="ataoz412@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    
    
    server.starttls()

    server.login(fromMail,"Yusuf2021!")

    message =MIMEMultipart('alternative')   
    message['Subject'] = subject

    htmlContent = MIMEText(content,'html')
    message.attach(htmlContent)


    server.sendmail(fromMail,toMail,message.as_string())    

    server.quit()