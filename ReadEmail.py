import imaplib
import email


def searchMail(username, password):
    # login
    host = "imap.gmail.com"
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    _, searchData = mail.search(None, "UNSEEN") # get unseen mesages

    for x in searchData[0].split():
        
        emailData = {}
        _, data = mail.fetch(x, "(RFC822)")
        _, b = data[0]
        emailMessage = email.message_from_bytes(b)
        # format to usable form
        for header in ["subject", "to", "from", "date"]:
            emailData[header] = emailMessage[header] # get meta data + subject


        for part in emailMessage.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                emailData["body"] = body.decode() 
                # get main body of the email
        
        yield emailData # yield dictionary of data        
    yield "stop"