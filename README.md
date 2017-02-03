## Mailer with Jinja2 templating support support
[![PyPI version](https://badge.fury.io/py/mailer-jinja2.svg)](https://badge.fury.io/py/mailer-jinja2)

```
from mailer_jinja2.mail import Mail
from smtplib import SMTP


from_address = 'sender@mail.com'
password = 'test1234'

to_address = 'receiver@mail.com

server = SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(from_address, password)

mail = Mail(from_address=from_address,
            to_address=to_address,
            subject='Test mail',
            template='test.html',
            server=server,
            fname='theo',
            sname='erik'
            )

mail.send_message()
```
