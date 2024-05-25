import os, base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


REPLY_TO_CC = 'wecare@rickos-m.com'

def get_credentials():
    creds = None
    if os.path.exists('samabialmuwahed.json'):
        creds = Credentials.from_authorized_user_file('samabialmuwahed.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('mohamedzahi33-python_email_sender_creds.json', ['https://www.googleapis.com/auth/gmail.send'])
            creds = flow.run_local_server(port=0)
        
        with open('samabialmuwahed.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_message(sender, to, cc, reply_to, subject, body):
  message = f"From: {sender}\nTo: {to}\ncc: {cc}\nReply-To: {reply_to}\nSubject: {subject}\nMIME-Version: 1.0\nContent-type: text/html\n\n{body}"
  return {'raw': base64.urlsafe_b64encode(message.encode()).decode()}


def send_message(api_service, sender, to, cc, reply_to, subject, body):
    try:
        message = create_message(sender, to, cc, reply_to, subject, body)
        email = api_service.users().messages().send(userId="me", body=message).execute()
        print(f"Email sent. Message Id: {email['id']}")
        return email
    except Exception as error:
        print(f"An error occurred: {error}")


def send_mail_func(to, service, name, date, time, address, hours, cancel_link, paid_or_deducted, how_to_enter, problem_details):
    api_service = build('gmail', 'v1', credentials=get_credentials())

    if time in ['09:00', '10:00', '11:00']:
        am_pm = ' am'
    elif time == '12:00':
        am_pm = ' pm'
    else:
        am_pm = ''

    html_body = f"""<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJqS1fJL0zTaz15nIA9epCtGKd6IoFAn5JxgCCS3KF81UqTG2B" crossorigin="anonymous">
    </head>
    <body style="font-family: sans-serif; font-size: 1.5em; background-color: #f5f5f5; margin: 0; padding: 0;">
      <div class="container" style="max-width: 100%; margin: 0; padding: 10px;">
        <div class="header" style="text-align: center; padding: 20px;">
          <img src="https://www.rickosm.com/static/img/logo.png" alt="Rickos Logo" style="max-width: 100%;">
        </div>
        <div class="greeting" style="color: #555; font-size: 1.3em; margin-top: 20px;">
          Greethings {name}
        </div>
        <div class="appointment-details" style="color: #2096ba; font-size: 1.8em; margin-top: 20px;">
          Appointment Details:
        </div>
        <ul style=padding: 0;">
          <li style="margin-bottom: 7px;"><strong>Date:</strong> {date},</li>
          <li style="margin-bottom: 7px;"><strong>Time:</strong> {time}{am_pm},</li>
          <li style="margin-bottom: 7px;"><strong>Location:</strong> {address},</li>
          <li style="margin-bottom: 7px;"><strong>Service:</strong> {service}</li>
          <li style="margin-bottom: 7px;"><strong>Number of hours:</strong> {hours} ({paid_or_deducted})</li>
          <li style="margin-bottom: 7px;"><strong>How to enter:</strong> {how_to_enter}</li>
          <li style="margin-bottom: 7px;"><strong>Problem details:</strong> {problem_details}</li>
        </ul>
        <div style="font-size: 0.8em; display: block; margin-left: 7px">Click <a href="{cancel_link}" style="text-decoration: none; color: #2096ba">here</a> if you want to cancel the appointment (Please note that the money will not be refunded if canceled less than 24 hours prior to the booking appointment)</div>
        <div style="text-align:center; margin-top:10px; font-size: 0.7em;">
          Rickos General Maintenance LLC
          <p style="text-decoration:none; color: #2096ba;">info@rickos-m.com</p>
          <p>+971-2-6222-540</p>
        </div>
      </div>
    </body>
    </html>"""
    send_message(api_service, "Rickos General Maintenance <info@rickos-m.com>", to, REPLY_TO_CC, REPLY_TO_CC, 'Your Appointment has been Booked Successfully!', html_body)


def send_cancel_mail(to, service, name, date, time, address, hours):
  api_service = build('gmail', 'v1', credentials=get_credentials())

  if time in ['09:00', '10:00', '11:00']:
    am_pm = ' am'
  elif time == '12:00':
    am_pm = ' pm'
  else:
    am_pm = ''
    
  html_body = f"""
  <!DOCTYPE html>
  <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    </head>
    <body style="font-family: sans-serif; font-size: 1.5em; background-color: white; margin: 0; padding: 0;">
      <div class="container">
        <div>
          <div class="row justify-content-center">
            <div class="col-md-6">
              <div class="container">
                <div class="row">
                  <div class="col-12 text-center shadow p-3 mb-5 bg-white rounded">
                    <img src="https://www.rickosm.com/static/img/logo.png" alt="Rickos Logo" class="img-fluid">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="justify-content-center">
          <p style="color: rgb(86, 93, 100); font-size: 1.3em">Greethings <span style="color: #2096ba;">{name}</span></p>

          <p style="color: rgb(86, 93, 100); font-size: 1.3em">Your <span style="color:#2096ba">{hours}</span> Hour(s) of <span style="color: #2096ba">{service}</span> appointment on <span style="color: #2096ba">{date}</span> at <span style="color:#2096ba">{time}{am_pm}</span> at <span style="color: #2096ba">{address}</span> has been cancelled!</p>
          <br>
          <p style="color: #2096ba">Rickos General Maintenance LLC</p>
          <a style="color: #2096ba; text-decoration: none">info@rickos-m.com</a>
          <a href="tel:+971-2-6222-540" style="color: #2096ba; text-decoration: none"><p>+971-2-6222-540</p></a>
        </div>
      </div>
    </body>
    </html>"""

  send_message(api_service, "Rickos General Maintenance <info@rickos-m.com>", to, REPLY_TO_CC, REPLY_TO_CC, 'Your Appointment has been Cancelled!', html_body)



if __name__ == '__main__':
  send_mail_func('mohamedzahi33@gmail.com', 'cleaning test', 'namee test', '01-04-2024', '09:00', 'address', 8, 'https://www.rickosm.com', 'paid_or_deducted_test', 'how_to_enter_test', 'problem_details_test')
  #send_cancel_mail('mohamedzahi33@gmail.com', 'cleaning test', 'name test', '01-04-2024', '09:00', 'address', 8)