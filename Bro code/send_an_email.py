import smtplib

sender = "sender email"
receiver = "receiver email"
password = "dfhfgjdlksasdfg"    # < not an actual password https://support.google.com/accounts/answer/185833?hl=en
subject = "Python email test"
body = "PUT YOUR GRASSES ON"

# header            # """ means multiple quote string, that's a string that can hold multiple lines
message = f"""From: {sender} 
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender, password)
    print("logged in...")
    server.sendmail(sender, receiver, message)
    print("email has been sent")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")