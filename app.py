import imaplib
import base64
import os
import email
import PyPDF2 
import getpass
print("Gmail id:")
email_user = input()
email_pass = getpass.getpass('Password:')
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
try:
    mail.login(email_user,email_pass)
    try:
        print("Password: ************")
        mail.select('Inbox')
        type, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0]
        id_list = mail_ids.split()
        #print(id_list)
        for i in id_list:
            num=i
            #print(num)
            typ, data = mail.fetch(num, '(RFC822)' )
            raw_email = data[0][1]
            # converts byte literal to string removing b''
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            # downloading attachments
            for part in email_message.walk():
                    # this part comes from the snipped I don't understand yet... 
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                print(fileName)
                if bool(fileName):
                    filePath = os.path.join('./', fileName)
                    if not os.path.isfile(filePath) :
                        
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
    except Exception as e:
        print("Error occured")                    
except Exception as e:
    print("invalid Email or password")