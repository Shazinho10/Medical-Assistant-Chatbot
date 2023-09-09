import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def appointment(username, email):
    sender_email = "haider@treatmentgps.com"
    sender_password = "uzklwgrqmjprkpqu"
    receiver_email = email
    subject = f"Update on Your Catheter Request"
    message = f'''
                   Dear {username},

                    I hope this message finds you well. We would like to inform you that your request for a catheter has been received and is now in the process of being reviewed and processed by our team.

                    Our dedicated team is committed to ensuring the highest quality of care and assistance for our customers. We understand the importance of timely and accurate support, especially when it comes to medical equipment like catheters.

                    Rest assured that we are working diligently to move forward with your request. Our team will carefully assess your needs to ensure that the catheter provided is tailored to your requirements and preferences.

                    We understand that this process may be a matter of urgency for you, and we want to assure you that we are making every effort to expedite the process without compromising on quality. Our goal is to ensure your comfort and satisfaction throughout this journey.

                    We appreciate your patience during this time. We will be in touch shortly to provide you with further updates on the progress of your catheter request. If you have any questions or concerns in the meantime, please do not hesitate to reach out to our customer support team at [customer support email or phone number].

                    Thank you for choosing us as your trusted partner for your medical needs. We look forward to assisting you and providing you with the best possible care.

                    Best regards,
                    Team TreatmentGPS
                '''

    # Create the MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server
    smtp_server = "smtp.gmail.com"  # Example for Gmail. Change for other providers.
    smtp_port = 587  # Use 465 for secure SSL connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Encrypt the connection

    # Login to the email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Quit the server
    server.quit()

if __name__ == "__main__":
    appointment(" bro", "haider.dftml@gmail.com")
    print("Done ............")