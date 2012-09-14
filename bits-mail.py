#!C:\Python27\python.exe -u
#!/usr/bin/env python

import smtplib

print "You can send mail from any BITS Student ID to any other Student ID of the form f20XXYYY.\n"
sndr = raw_input("Enter the sender's email ID (f20XXYYY): ")
print
rcpt = raw_input("Enter the recepient's email ID (f20XXYYY): ")

sndr = sndr.__add__("@bits-goa.ac.in")
rcpt = rcpt.__add__("@bits-goa.ac.in")

recepients = []
recepients.append(rcpt)

op = raw_input("Do you want to add more recepients?(y/n)")

if op is "y":
	rcpt = raw_input("Enter the recepient's email ID (f20XXYYY): ")
	rcpt = rcpt.__add__("@bits-goa.ac.in")
	recepients.append(rcpt)


#print recepients

sub = raw_input("Enter the subject line: ")
body = raw_input("Enter the body of the message: ")

try:
	final_body = "From: "+sndr+"\nTo: "+recepients[0]+", "+recepients[1]+"\nSubject: "+sub+"\nBody: "+body
except:
	final_body = "From: "+sndr+"\nTo: "+recepients[0]+", "+"\nSubject: "+sub+"\nBody: "+body
#print final_body

try:
	smtpObj = smtplib.SMTP('warrior.bits-goa.ac.in')
	smtpObj.helo('warrior.bits-goa.ac.in')
	smtpObj.sendmail(sndr, recepients, final_body)
	smtpObj.quit()
	print "Message submitted successfully!"
except:
	print "Could not send the message, there might be some problem with the server!"
