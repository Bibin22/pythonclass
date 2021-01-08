from re import *
f = open('email', 'r')
fout =open('validemail', 'w')
email = set()
for mails in f:
    email.add(mails.rstrip('\n'))
rule = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
for emails in email:
    matcher = match(rule, emails)
    if matcher != None:
        fout.write(emails + "\n")
    else:
        print(emails,"invalid")