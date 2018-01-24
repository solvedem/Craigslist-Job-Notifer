import urllib2
import smtplib
from bs4 import BeautifulSoup

yourEmail = ""
yourPw = ""
recipientEmail = ""

queries = ["Python","Java","Javascript","HTML","CSS","Computer+Science","c%2B%2B"]
loc = "sfbay"


def get_jobs(query, location):
    jobs = []
    url = "https://" + location + ".craigslist.org/d/jobs/search/jjj?query=" + query
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all("a", class_="result-title hdrlnk"):
        try:
            jobs.append(" ".join(str(i.text).split()))
        except:
            continue
    return jobs

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # "Successfully sent email"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    except:
        # "Email not sent"
        pass

msg = ""
for q in queries:
    msg += q + " - " + str(len(get_jobs(q,loc))) + "\n"
    
send_email(yourEmail, yourPw, recipientEmail, "", msg)
