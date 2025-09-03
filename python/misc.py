## For sending emails to a lot of people (undfined) create the below function
send_email(*emails):
    for email in emails:
        draft_email(......,reciepents=email, sender=email) # (basically call the main function)

send_email('bbla@google.com','bsxhjbk@yahoo.com','bbbla@rediffmail.com'.........)
