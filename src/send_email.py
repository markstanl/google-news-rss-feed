import yagmail
import json


def send_email(recipient: str, subject: str, html_contents: str):
    """
    Sends an email to the recipient with the given subject and HTML contents
    :param recipient: the email address of the recipient
    :param subject: the subject of the email
    :param html_contents: the HTML contents of the email
    :return: none
    """

    with open('pass.json') as file:
        # MAKE SURE TO CREATE A pass.json FILE WITH YOUR EMAIL AND
        # if using gmail, use an app password
        email_config = json.load(file)
    yag = yagmail.SMTP(email_config["email_user"], email_config["email_pass"])
    yag.send(
        to=recipient,
        subject=subject,
        contents=html_contents
    )
