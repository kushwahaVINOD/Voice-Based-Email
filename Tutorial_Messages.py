import text_to_speech as ts
# class Tutorial_Messages:
def dashboard_msg():
    ts.t2s("Welcome to your email account.   Here are your options.   Compose to  compose.  Inbox to access your  inbox. Logout to  logout form this account ")


def inbox_msg():
    ts.t2s("Welcome to your inbox. Please listen to your choice.  Read all, to read all mails. Dashboard, to go to your mail dashboard.")

def readAll_msg():
    ts.t2s("reading all mails give command after each mail information after you listen speak now, read to read complete message next to read next mail forward to forward mail Delete to delete mail reply to reply mail stop to stop reading all mails and go to inbox")
