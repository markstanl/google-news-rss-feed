# RSS Email Feed

RSS Email Feed is a simple Python script that sends an email with the latest RSS feed entries from a given URL (to be
determined what exactly it does).

## About

To practice for my new role as Software Technical Lead with Wisconsin Messenger, I thought it smart to create a dummy python
script that parses RSS code and sends a sort of newsletter to a given email.

## Usage

To use this, fork the project, clone it to your local machine, and install dependencies from the requirements.txt file.
Add a pass.json file with your email and password, following this format:

```json
{
  "user_email": "youremail@email.com",
  "user_pass": "password123"
}
```

This project uses yagmail, which is a wrapper around smtplib, so you can use any email provider that uses SMTP.
Then, in main.py, change the URL to the RSS feed you want to use, and include the email recipient and subject line.