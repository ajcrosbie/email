import ReadEmail
import writeEmail

def check(recived, file, loginDetails):
    message = []
    with open(file, "r") as f:
        for i in f:
            c = i.split(";") 
            for v in recived["body"].split():
                if c[0] == v:
                    message.append(c[1])
                    
    if len(message) == 0:
        writeEmail.send_mail("I found nothing that help, sorry", "automatic response", loginDetails[2],
        [recived["from"]], loginDetails[0], loginDetails[1]) # if no keywords were found
    
    else:
        m1 = "I found this that might help" 
        for i in message:
            m1 = m1 + i
        writeEmail.send_mail(m1, "automatic response", loginDetails[2],             
        [recived["from"]], loginDetails[0], loginDetails[1]) # can process multiple requests 

def main():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables
    file = "keywords.txt" # can change file name
    loginDetails = [username, password, emailName] 


    d = ReadEmail.searchMail(username, password) # login
    con = True
    
    while con:
        f = next(d)
        if f == "stop":
            con = False
        else:
            check(f, file, loginDetails) # go through all unread emails

if __name__ == "__main__":
    main()
