class EmailTool:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        import smtplib
        from email.mime.text import MIMEText

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, [to_email], msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f'Failed to send email: {e}')