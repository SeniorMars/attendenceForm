import helium

def fill_form(username, password):
    start_firefox(
        'https://docs.google.com/forms/d/e/1FAIpQLScSW4ZPkJZN_i84epira40_ndrlsMz-avMcXoGUz7JYsJY2Gg/viewform?vc=0&c=0&w=1',
    headless=True)
    write(username, into='Email')
    click('Next')
    write(password, into='Enter')
    click('Next')
    click('Yes')
    write('None', into="Questions")
    click('Submit')
    kill_browser()

# fill_form(#yourusername@stuy.edu, password)
