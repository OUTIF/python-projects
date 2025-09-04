##################### Extra Hard Starting Project ######################

import random
import pandas
import datetime as dt
import smtplib

my_email = 'yusu1f.work@gmail.com'
my_password = 'fnnxcbdlsdyvkzpk'

dates = pandas.read_csv('birthdays.csv')
dates_dict = dates.to_dict()

today = dt.datetime.now()
month = today.month
day = today.day

for index in range(len(dates_dict['name'])):

    if dates_dict['month'][index] == month and dates_dict['day'][index] == day:
        name = dates_dict['name'][index]
        r = random.randint(1, 3)
        with open(f'letter_templates/letter_{r}.txt') as letters:
            letter = letters.read()
            message = letter.replace('[NAME]', str(name))

        email_to_send = dates_dict['email'][index]
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email_to_send,
                                msg=f'subject:Happy birthday\n\n{message}')
            connection.close()



