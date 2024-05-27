import yagmail

def send_email(recipient: str, subject: str, html_contents: str):
    """
    Sends an email to the recipient with the given subject and HTML contents
    :param recipient: the email address of the recipient
    :param subject: the subject of the email
    :param html_contents: the HTML contents of the email
    :return: none
    """
    yag = yagmail.SMTP("markgstanley1@gmail.com", "")