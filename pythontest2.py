import smtplib as smtp
from email.message import EmailMessage
f = open("file2.txt")
email=f.read()
msg = EmailMessage()
msg['To']=email
msg['From']='aghloansandservices@gmail.com'
msg['Subject']="Loan Approved In AGH Loans\n"
msg['Dear Customer']= "Your Application Has Been Approved In AGH Loans. Please check the website for further details.ThankingYou,Regards AGH Teams"



#msg= f'Subject: {subject}\n\n{body}'

with smtp.SMTP('smtp.gmail.com', 25) as smtp:
    
    smtp.starttls()
   
    
    smtp.login("aghloansandservices@gmail.com", "Aghloans@123")

    smtp.send_message(msg)
    print("Your loan Apllication Has Been Approveds And Email Has Been Sent")
