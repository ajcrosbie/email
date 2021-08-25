import writeEmail
import processEmail
import ReadEmail

def test_SendRead():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables
    
    
    temp = True
    t = ReadEmail.searchMail(username, password) 
    while temp:
        c = next(t)
        if c == "stop":
            temp = False
    # only test if no unread emails are there but this will clear them
    
    
    writeEmail.send_mail("dog", "none", emailName, [username], username, password) # change 1st argument
    f = ReadEmail.searchMail(username, password)
    
    v = []
    temp = True
    while temp:
        c = next(f)
        if c == "stop":
            temp = False
        else:
            v.append(i for i in c.split())
    assert "dog" in v # change to keyword from actual keywords file

def test_process():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables
    # change and use environment variables
    temp = True
    t = ReadEmail.searchMail(username, password) 
    while temp:
        c = next(t)
        if c == "stop":
            temp = False
    
    writeEmail.send_mail("dog", "none", emailName, [username], username, password)# change 1st argument
    processEmail.main()
    f = ReadEmail.searchMail(username, password)
    assert "best" in next(f)["body"].split()