import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail_func(to, service, name, date, time, address, hours, cancel_link, paid_or_deducted, how_to_enter, problem_details):
    reply_to_cc = 'wecare@miramar-uae.com'

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
          <img src="https://www.miramar-pm.com/static/img/logo.png" alt="Miramar Logo" style="max-width: 100%;">
        </div>
        <div class="greeting" style="color: #555; font-size: 1.3em; margin-top: 20px;">
          Greethings {name}
        </div>
        <div class="appointment-details" style="color: #dd5269; font-size: 1.8em; margin-top: 20px;">
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
        <div style="font-size: 0.8em; display: block; margin-left: 7px">Click <a href="{cancel_link}" style="text-decoration: none; color: #dd5269">here</a> if you want to cancel the appointment (Please note that the money will not be refunded if canceled less than 24 hours prior to the booking appointment)</div>
        <div style="text-align:center; margin-top:10px; font-size: 0.7em;">
          Miramar General Maintenance LLC
          <p style="text-decoration:none; color: #dd5269;">maintenance@miramar-uae.com</p>
          <p>+971-2-6222-540</p>
        </div>
      </div>
    </body>
    </html>
    """



    msg = MIMEMultipart()
    msg['From'] = 'Miramar General Maintenance <wecare@miramar-uae.com>'
    msg["To"] = to
    msg['Subject'] = 'Your Appointment has been Booked Successfully!'
    msg['cc'] = reply_to_cc
    msg['Reply-To'] = reply_to_cc
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
      server.starttls()
      server.login('services@property-technology.llc', '2fYB1NKtT6syZz3g')
      server.sendmail('wecare@miramar-uae.com', to, msg.as_string())



def send_cancel_mail(to, service, name, date, time, address, hours):
    reply_to_cc = 'wecare@miramar-uae.com'

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
                    <img src="https://www.miramar-pm.com/static/img/logo.png" alt="Miramar Logo" class="img-fluid">
                  </div>
                </div>
              </div>
            </div>
          </div>  

        <div class="justify-content-center">
          <p style="color: rgb(86, 93, 100); font-size: 1.3em">Greethings {name}</p>

          <p style="color: rgb(86, 93, 100); font-size: 1.3em">Your <span style="color: rgb(208,77,97)">{hours}</span> Hour(s) of <span style="color: rgb(208,77,97)">{service}</span> appointment on <span style="color: rgb(208,77,97)">{date}</span> at <span style="color: rgb(208,77,97)">{time}{am_pm}</span> at <span style="color: rgb(208,77,97)">{address}</span> has been cancelled!</p>
          <br>
          <p style="color: #dd5269">Miramar General Maintenance LLC</p>
          <a style="color: #dd5269; text-decoration: none" href="mailto:maintenance@miramar-uae.com">maintenance@miramar-uae.com</a>
          <a href="tel:+971-2-6222-540" style="color: #dd5269; text-decoration: none"><p>+971-2-6222-540</p></a>
        </div>
      </div>
    </body>
    </html>"""

    msg = MIMEMultipart()
    msg['From'] = 'Miramar General Maintenance <wecare@miramar-uae.com>'
    msg["To"] = to
    msg['Subject'] = 'Your Appointment has been Cancelled!'
    msg['cc'] = reply_to_cc
    msg['Reply-To'] = reply_to_cc
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
        server.starttls()
        server.login('services@property-technology.llc', '2fYB1NKtT6syZz3g')
        server.sendmail('wecare@miramar-uae.com', to, msg.as_string())


if __name__ == '__main__':
  send_mail_func('mohamedzahi33@gmail.com', 'cleaning test', 'test', '01-04-2024', '09:00', 'address', 8, 'www.miramar-pm.com', 'paid_or_deducted_test', 'how_to_enter_test', 'problem_details_test')