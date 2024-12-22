import smtplib
import csv
def mail(date_entity,time_entity,user_names_found,event_names_found):
    gmail_user ="""admin email"""                      
    gmail_password = """"admin app password"""
    user_emails=[]
    with open('users.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            username = row['username']
            email = row['email']

          
            if username in user_names_found:
                user_emails.append(email)
    if len(user_names_found) == 1:
        participants= ""  
    else:
        
        participants = " between " + ", ".join(user_names_found[:-1]) + " and " + user_names_found[-1]
    sent_from = gmail_user
    to = user_emails
    subject = "Scheduled"+event_names_found[0]
    body = "On "+str(date_entity) +" "+str(time_entity)+" "+event_names_found[0]+" is scheduled"+participants

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)