import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from fastmcp import FastMCP
from decouple import config

mcp = FastMCP(
    name="Email sending MCP Server.."
)

def _send(email:str, subject:str, body:str) -> str:
    receiver_email = email
   
    message = MIMEMultipart("alternative")

    message["From"] = config("SENDER_EMAIL")
    message["To"] = receiver_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(config("SENDER_EMAIL"), config("PASSWORD"))
        server.send_message(message)


    return "Email sent successfully!"

@mcp.too
def send_mail(email:str, subject:str, body:str) -> str:
    """Can end email to any email address, just required Email address, Subject and Body

    Args:
        email : email address
        subject : one line subject of email
        body : complete formated plain email

    """
    return  _send(email, subject, body)

mcp.run(transport="streamable-http")
