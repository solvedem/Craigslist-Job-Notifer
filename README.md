# Craigslist-Job-Notifier

Necessary libraries: urllib2, smtplib, BeautifulSoup

Instructions:

Fill out the custom information at the top of the file. 
It is a good idea to make a blank gmail account to act as the email account for this bot. 
Storing passwords with any sort of importance in plaintext is a bad idea.

The queries variable should be list of keywords you want the bot to search for.
Queries with spaces or symbols need to be treated appropriately.

For example:

"Computer Science" should be written as "Computer+Science"

"C++" should be written as "c%2B%2B"

If you are unsure about a query, search it on the craigslist jobs section. 
If you search the string "!@#$%^&*()", this is the resulting url. 
The query is everything after the "="

https://grandrapids.craigslist.org/search/jjj?query=%21%40%23%24%25%5E%26*%28%29

The location section should be the first section of the craigslist url.
Note that it's not always the name of the city you want searched.

https://losangeles.craigslist.org/

https://newyork.craigslist.org/

https://sfbay.craigslist.org/

https://miami.craigslist.org/

[![bot2.jpg](https://s17.postimg.org/hnpm4txj3/bot2.jpg)](https://postimg.org/image/fj593qvwb/)

Set up the bot to run daily (or whenever) via a task scheduler. 
This is the resulting email.

[![bot.jpg](https://s17.postimg.org/3u19fqf7j/bot.jpg)](https://postimg.org/image/akhqp62d7/)

You can also set up the bot to text you by sending an email to your phone.
This is done by putting the domain of your carrier after your phone number.

For example:

1119999999@text.att.net

1119999999@vtext.com

Note that emails over a certain size won't fit in a text message.
