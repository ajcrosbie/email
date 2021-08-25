import writeEmail
import processEmail
import ReadEmail

def test_SendRead():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables

    writeEmail.send_mail("dog", "none", emailName, [username], username, password) # change 1st argument
    f = ReadEmail.searchMail(username, password)
    v = next(f)["body"].split()
    assert "dog" in v # change to keyword from actual keywords file

def test_process():
    username = "experiencework4@gmail.com" # change and use environment variables
    password = "work.experience1" # change and use environment variables
    emailName = "Work Experience <experiencework4@gmail.com>" # change and use environment variables
    file = "keywords.txt"  # change and use environment variables
    processEmail.main()
    writeEmail.send_mail("dog", "none", emailName, [username], username, password)# change 1st argument
    processEmail.main()
    f = ReadEmail.searchMail(username, password)
    assert "best" in next(f)["body"].split()