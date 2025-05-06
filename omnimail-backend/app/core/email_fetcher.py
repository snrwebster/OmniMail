# app/utils/email_fetcher.py

import imaplib
import email
from email.header import decode_header

def fetch_emails(username, password, imap_server="imap.gmail.com"):
    mail_conn = imaplib.IMAP4_SSL(imap_server)
    mail_conn.login(username,password)
    mail_conn.select("INBOX")
    status,inbox_emails = mail_conn.search(None,"all")
    return mail_conn.fetch("1","(RFC822)")
            
