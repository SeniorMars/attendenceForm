#!/usr/bin/python3
import requests
import schedule
import time
from bs4 import BeautifulSoup
from helium import click, kill_browser, start_chrome, start_firefox, write

username = "user@stuy.edu"  # change
password = "pssd"  # change
fill_form_time = "08:30"  # the time the script runs. 24-hour time to change.
form_supplier = "http://homer.stuy.edu/~chernandez10/email/get_link.py"


def fill_form():
    response = requests.get(form_supplier)
    soup = BeautifulSoup(response.text, "html.parser")
    attendence_form_url = soup.find('p').contents[0]
    start_firefox(attendence_form_url, headless=True)
    # start_chrome(attendence_form_url, headless=True) #if you have chrome
    write(username, into='Email')
    click('Next')
    write(password, into='Enter')
    click('Next')
    click('Yes')
    write('None', into="Questions")
    # click("Send me a copy") #optional
    click('Submit')
    kill_browser()


def schedule_weekedays():  # schedule doesn't have a weekday option :(
    # will run accoring to fill_form_time
    schedule.every().monday.at(fill_form_time).do(fill_form)
    schedule.every().tuesday.at(fill_form_time).do(fill_form)
    schedule.every().wednesday.at(fill_form_time).do(fill_form)
    schedule.every().thursday.at(fill_form_time).do(fill_form)
    schedule.every().friday.at(fill_form_time).do(fill_form)

    while True:
        schedule.run_pending()
        time.sleep(60)


schedule_weekedays()
