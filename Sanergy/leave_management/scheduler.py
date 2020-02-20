'''
schedule.every().hour.do(job)

This executes the job() function every hour

schedule.every().day.at("12:25").do(job)

This executes the job() function every day at 12:25 PM
By default schedule uses 24 hr format.

schedule.every().wednesday.at("13:15").do(job)

Do job() every Wednesday at 1:15 PM.
You can also specify day-names to run a particular job.
See the list of available ones.

schedule.every(2).to(5).minutes.do(job3)

This one executes job3() every 2 to 5 minutes ;)
'''
import time

import schedule

# from views import (employee_leave_request, leave_entitlement_types,
#                     populate_leaveAccruals, populate_sanergy_calender,
#                     post_leave_to_salesforce, refresh_sanergy_calender)


def job():
    print("I'm working...")

def job2():
    print("yo boiss..")

def job3():
    print("Hello")

schedule.every(2).seconds.do(job)
schedule.every(3).seconds.do(job2)
schedule.every(4).seconds.do(job3)
some other variations
schedule.every().hour.do(job)
schedule.every().day.at("12:25").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().thursday.at("19:15").do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
