#### Xiang Wang @ 2016-12-22 17:44:47

# basic auth configuration
call this function first
## example
    USERNAME = "ramwin"
    PASSWORD = "MYPASSWORD"
    config = Configuration(
        server='mail.example.com',
        credentials=Credentials(username=USERNAME, password=PASSWORD),
        auth_type=NTLM,
        verify_ssl=False,
    )
    EWSTimeZone.PYTZ_TO_MS_MAP["Asia/Shanghai"] = 'China Standard Time'
    # the PYTZ_TO_MS_MAP only contains few location, you should add your
    # special timezone refering the MS_TIMEZONE_DEFINITIONS

    tz = EWSTimeZone.timezone("Asia/Shanghai")
    account = Account(primary_smtp_address=USERNAME, config=get_config(),
                      access_type=DELEGATE)


# Mailbox
## example
    # a class represent mail
    mailbox = Mailbox(
      name="nickname",
      email_address="user@example.com",
      mailbox_type="MailBox",
      item_id=None)


# EmailAddress
## example
    from exchangelib.folders import EmailAddress
    # a class represent email for contact
    emailaddress = EmailAddress(email="user@example.com", label="EmailAddress1")


## parameters
* email: an email
* label: must in {'EmailAddress1', 'EmailAddress2', 'EmailAddress3'}


# Contact
## example
    from exchangelib.folders import Contact
    contact = Contact(
        nickname="name",
        email_addresses=[emailaddress], # isinstance(emailaddress, EmailAddress)
        )
    account.contacts.bulk_create(items=[contact])


# CalendarItem
an event
## example
    from exchangelib.folders import CalendarItem 
    item = CalendarItem(
        start = tz.localize(EWSDateTime(year, month, day, hour, 30)),
        end = tz.localize(EWSDateTime(year, month, day, hour+1, 30)),
        subject = "Subject",
        body = "Hello from python",
        location = "devnull",
        categories = ['foo', 'bar'],
        account = account,
        folder = account.calendar,
    )
## parameters
* start: starttime
* end: endtime
* subject
* body
* location

## function
* save
    * `send_meeting_invitations`: 'SendToNone', 'SendOnlyToChanged', 'SendToAllAndSaveCopy'


# Attendee
## example
    from exchangelib.folders import Attendee
    attendee = Attendee(
      mailbox = mailbox,
    )


# Message
email message
## example
    from exchangelib.folders import Message
    m = Message(
        folder=account.send,  # if folder is None, you can call m.save only
        account=account,
        subject="Subject",
        body="All bodies are beautiful",
        to_recipients=[Mailbox(email_address="user1@example.com"), Mailbox(email_address="user2@example.com")],
        cc_recipients=[Mailbox, Mailbox],
    )
    m.send_and_save()
    m.save()  # if folder is None
## parameters
* to_recipients: [Mailbox, Mailbox]
* cc_recipients: [Mailbox, Mailbox]
