import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(email_dict, resume_path):

    sender_email = "dhartipateloffice@gmail.com" 
    sender_password = "qvucqvppevqedhes" 

    for company_name, recipient_email in email_dict.items():
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = f"Application for Python Developer Role - Dharti Patel"

        body = f"""
Dear Hiring Team at {company_name},

I am writing to express my keen interest in the Python Developer position at {company_name}, as advertised on Linkedin. With 1.5 years of experience specializing in Python development, I possess a strong foundation in building robust and scalable applications.

My expertise encompasses a range of Python libraries and frameworks, including Django, FastAPI, and Flask, enabling me to develop both web applications and APIs efficiently. I am also familiar with integrating AI/Machine Learning models into Python-based applications, further enhancing their capabilities.

I am eager to contribute my skills and passion for Python development to {company_name}'s innovative projects.

For a detailed overview of my qualifications and projects, please find my resume attached. You can also explore my portfolio at https://dhartipatel.netlify.app/ to see examples of my work.

Thank you for your time and consideration. I would welcome the opportunity to discuss how my skills and experience can benefit {company_name}.

Sincerely,

Dharti Patel
+91 9512436804
dhartipateloffice@gmail.com
https://www.linkedin.com/in/dhartipatel44
        """

        message.attach(MIMEText(body, 'plain'))

        # Attach the resume
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {resume_path}",
        )
        message.attach(part)

        # Create a secure connection with the server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {company_name} at {recipient_email}")

email_dict = {
    "Unified Mentor": "info@unifiedmentor.com",
    "Doyenhub Software Solution": "hr@doyenhub.com",
    "MUNSOW": "admin@munsow.com",
}
resume_path = "Python_Developer_DhartiPatel.pdf"  

send_email(email_dict, resume_path)