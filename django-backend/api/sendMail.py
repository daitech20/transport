import smtplib

def sendMail(email, code):
    gmail_user = 'ndpd2001@gmail.com'
    gmail_password = '01682200122'

    sent_from = gmail_user
    to = [email]
    subject = 'Validate Email'
    body = f'Click link to validate Email: <a href="http://localhost:8000/api/validateEmail/{email}/{code}/">click here</a>'

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