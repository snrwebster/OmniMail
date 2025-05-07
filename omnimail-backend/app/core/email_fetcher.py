# app/utils/email_fetcher.py

import imaplib
import email
from email.header import decode_header
from models.models import Email


def fetch_emails(username, password, imap_server="imap.gmail.com"):
    mail_conn = imaplib.IMAP4_SSL(imap_server)  # to add checks for wrong server
    mail_conn.login(username, password)  # to add handling for wron authentication
    mail_conn.select("INBOX")  # to make modular for user selection folder
    status, emails_id_bytestring = mail_conn.search(None, "all")  # to add checks
    emails_ids = emails_id_bytestring[0].split()  # to add checks

    emails_list = []
    for email_id in emails_ids[-5:]:
        status, email_data = mail_conn.fetch(email_id, "(RFC822)")
        if status != "OK":
            continue  # to add logic

        raw_email = email_data[0][1]
        parsed_email = email.message_from_bytes(
            raw_email
        )  # check other data as well prppably something useful
        
    return parsed_email.keys()
