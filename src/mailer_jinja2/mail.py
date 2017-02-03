from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from .template import generate_template


class Mail:
    to_address: str
    from_address: str
    server: SMTP
    msg: str
    subject: str

    def __init__(self, from_address: str, to_address: str, subject: str, template: str, server: SMTP, **kwargs):
        """
        Initialize mail object
        :param from_address: sender email
        :param to_address: to which address email
        :param msg: the message which will be send. generate with template.generate_template
        :param server: a smtplib.SMTP object
        """
        self.to_address = to_address
        self.from_address = from_address
        self.server = server
        self.subject = subject
        self.msg = generate_template(template_name=template, **kwargs)

    def send_message(self) -> None:
        """
        send the actual message
        """
        message = MIMEMultipart('alternative')
        message['subject'] = self.subject
        message['To'] = self.to_address
        message['From'] = self.from_address
        message.preamble = """
        Your mail reader does not support the report format.
        Please visit us."""
        html_body = MIMEText(self.msg, 'html')
        message.attach(html_body)

        self.server.sendmail(self.from_address, self.to_address, message.as_string())
