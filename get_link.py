#!/usr/bin/python3
# Using my own account (that has all emails from my stuy.edu) I use this script
# to get the link for the day. It's made from an alnighter and stackoverflow so
# it might have some bugs. Get's the work done.
import email
import imaplib


mail = imaplib.IMAP4_SSL("imap.gmail.com")
imap_user = "username"
imap_pass = "password"
mail.login(imap_user, imap_pass)
mail.select("script")
result, data = mail.uid('search', None, "ALL")

script_items = data[0].split()

new = script_items[0]

result2, email_data = mail.uid('fetch', new, '(RFC822)')
raw_email = email_data[0][1]
full_email = email.message_from_bytes(raw_email)
body = ""

if full_email.is_multipart():
    for part in full_email.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
else:
    body = full_email.get_payload(decode=True)

body = body.decode('utf-8')
day = body[body.find("\n")+1:body.find("2020")+4]
print(day)
first = body.find("https")
body = body[first:]
last = body.find("\n")
print(body[:last])
