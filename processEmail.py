import ReadEmail
import writeEmail

def check(recived, file, loginDetails):
    with open(file, "r") as f:
        for i in f:
            c = i.split(";") 
            for v in recived["body"].split():
                if c[0] == v:
                    writeEmail.send_mail(c[1], "automatic response", loginDetails[2],
                     [recived["from"]], loginDetails[0], loginDetails[1])

def main():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables
    file = "keywords.txt" # can change file name
    loginDetails = [username, password, emailName] 
    d = ReadEmail.searchMail(username, password)
    
    while True:
        f = next(d)
        if f == "stop":
            break
        check(f, file, loginDetails) 
if __name__ == "__main__":
    main()
