import smtplib as smtp
from email.message import EmailMessage
f = open("file1.txt")
email=f.read()
msg = EmailMessage()
msg['To']=email
msg['From']='aghloansandservices@gmail.com'
msg['Subject']='YOUR APPLICATION HAS BEEN REJECTED\n'
msg['Dear Customer']= "Your Application Has Been Rejected In AGH Loans. Please check the website for further details.ThankingYou,Regards AGH Teams"


#msg= f'Subject: {subject}\n\n{body}'

with smtp.SMTP('smtp.gmail.com', 25) as smtp:
    
    smtp.starttls()
   
    
    smtp.login("aghloansandservices@gmail.com", "Aghloans@123")

    smtp.send_message(msg)
    print("Your loan Apllication Has Been rejected And Email Has Been Sent")