import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from csv import DictReader
from datetime import datetime

ID = 1
#sender info
sender_address = '#' #add email address
sender_pass = '#' #add password here

#database
f = open('newdb.csv', 'r', encoding='utf-8')

reader = DictReader(f)
for row in reader:
    try:
        receiver_address = row['email']
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Registration Confirmation"
        content = f"""Dear {row['name']},

This is to let you know that your request for joining Notre Dame English Club has been accepted. 
It is my utmost pleasure to confirm your membership and I delightedly welcome you to the club.

Your club roll: {row['clubroll']}

Join our online communities:
Facebook Group: https://www.facebook.com/groups/356913678922538
Discord Server: https://discord.gg/Hcc98W98RR

Please note that you were told to submit a Passport Size Photo with the form. In case you have uploaded a selfie/casual photo, please email us to replace your photo. The club will not take any responsibility if your photo in id card gets cropped or stretched out. 
    
{row['message']}


Thank you.


Sincerely,
Notre Dame English Club
    """
        message.attach(MIMEText(content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print(f'Mail Sent to {receiver_address}. ID: {ID}')
        ID+=1
    except:
        pass