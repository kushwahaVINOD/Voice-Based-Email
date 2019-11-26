
import smtplib    
import text_to_speech as ts
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib

class Gmail_smtp:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    def compose_mail(self):
        print("incompose")
        ts.t2s("Welcome to compose mail. Speak subject of message")
        print(" Speak your message")
        subject = ts.get_command()
        ts.t2s("Now speak the email content")
        text = ts.get_command()
        # ts.t2s("Your message is:"+msg)
        # ts.t2s("If corect say yes else say no")
        print("Your message is:" + text)
        print("If correct say yes else say no")
        msg = 'Subject: {}\n\n{}'.format(subject, text)

        # msg = email.message.Message()
        # msg['Subject'] = 'subject of the message'
        # msg['From'] = self.userid
        #
        # msg.set_payload(text)


        ts.t2s("Your message has been recorded. Say send to send this mail and save to save it to drafts")
        choice = ts.get_command(["send","save"])
        if choice == "send":
            self.send_mail(msg)
        elif choice == "save":
            self.save_mail(msg)
        return


    def send_mail(self, msg):
        print("in send_mail")
        # the function should take take user name and password and return the contents of inbox
        # in a format that we can extract mails from it
        # raise NotImplemented
        ts.t2s(" Speak recepient's email address")
        print(" Speak recepient's email address")
        receiever = ts.get_email()
        print(receiever)
        reciever = "gaurav.singh.atoria@gmail.com"
        ts.t2s("Your message reciever is:" + reciever)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Connected to gmail server")
        server.starttls()
        server.login(self.userid, self.password)
        print("logged in")
        server.sendmail(self.userid,receiver, msg)
        ts.t2s("your message has been sent")
        return

    def forward_mail(self, msg):
        ts.t2s(" Speak recepient's email id")
        print(" Speak recepient's email id")

        receiever = ts.get_email()
        print(receiever)
        reciever = "gaurav.singh.atoria@gmail.com"
        ts.t2s("Your message reciever is:" + reciever)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Connected to gmail server")
        server.starttls()
        server.login(self.userid, self.password)
        print("logged in")
        server.sendmail(self.userid, "gaurav.singh.atoria@gmail.com", msg)
        ts.t2s("your message has been sent")
        return

    def reply_mail(self,recepient_id):
        ts.t2s("Please provide your reply")
        print(" Speak your reply")
        reply = ts.get_command()
        # ts.t2s("Your message is:"+msg)
        # ts.t2s("If corect say yes else say no")
        #print("Your message is:" + reply)
        #print("If correct say yes else say no")
        ts.t2s("Your reply has been recorded. Say send to send the reply")
        choice = ts.get_command(["send","save"])
        if choice == "send":
            server = smtplib.SMTP('smtp.gmail.com', 587)
            print("Connected to gmail server")
            server.starttls()
            server.login(self.userid, self.password)
            print("logged in")
            server.sendmail(self.userid, recepient_id, reply)
            ts.t2s("your reply has been sent to " + recepient_id)
            return
        else:
            ts.t2s("Reply not sent")
    def save_mail(self, message):
        # msg = email.message.Message()
        # msg['Subject'] = 'subject of the message'
        # msg['From'] = self.userid
        # msg['To'] = MY_EMAIL
        # msg.set_payload(message)
        # # append the message to the drafts folder
        # now = imaplib.Time2Internaldate(time.time())
        # imap.append('[Gmail]/Drafts', '', now, msg.as_bytes())
        msg = MIMEMultipart("alternative")
        msg.set_charset("utf-8")
        msg.attach(MIMEText(message, "plain", "utf-8"))
        msg['Subject'] = "SUBJECT"
        msg['From'] = self.userid
        msg['To'] = "rajsrivastava871@gmail.com"
        conn = imaplib.IMAP4_SSL('imap.gmail.com', port=993)
        conn.login(self.userid, self.password)
        conn.select('[Gmail]/Drafts')
        conn.append("[Gmail]/Drafts", '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
        ts.t2s("Saved to drafts")
