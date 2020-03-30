# Attendance Form
A python3 script to automatically filled out the attendance form. It works if you don't have two-factor authentication

do:
> pip install --user -r requirements.txt

Now edit form.py and fill out username and password with your info. If you like to change the time which the script fills out the form change fill_form_time. If you use chrome or want to get a copy of your responses, then uncomment the lines. The script is run using:

> python -u form.py

However, you probably don't want a terminal running with a foreground process. If you are on linux I recommend doing this:

> nohup python -u form.py &

This makes it a background process and allows the script to run as intended. Not test on mac, but as long as you have nohup it should work.



You could also do the following to allow the script to run. Make sure the script runs.

or

python -i form.py
> fill_form(user name, pass)


You might be wondering what is fill_form.py. Simply put it is the script running on [homer]( http://homer.stuy.edu/~chernandez10/email/get_link.py ). I included it so people can see what's appending.

Why did I have to create it? I was going to have everyone scrape the links from gmail, however, Stuy disable "Less secure apps" on gmail. So, it won't work. Currently, I just forward all Stuy emails to my extra account and create a filter to make sure the script works. Any questions, just ask.
