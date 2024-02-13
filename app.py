import os, base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_message(sender, to, subject, body):
    message = f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{body}"
    return {'raw': base64.urlsafe_b64encode(message.encode()).decode()}


def send_message(service, sender, to, subject, body):
    try:
        message = create_message(sender, to, subject, body)
        message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Message sent. Message Id: {message['id']}")
        return message
    except Exception as error:
        print(f"An error occurred: {error}")


def main():
    credentials = get_credentials()
    service = build('gmail', 'v1', credentials=credentials)

    sender_email = "from_name <user101@gmail.com>"
    recipient_email = "mohamedzahi33@gmail.com"
    email_subject = "Hi"
    email_body = "email body" 

    send_message(service, sender_email, recipient_email, email_subject, email_body)

if __name__ == '__main__':
    main()
