import pytz
import datetime

# country = 'Asia/Kolkata'
# tz_to = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to)
# print("the time in {0} is {1}".format(country,local_time))
def print_list(list_of_strings):
    for s in list_of_strings:
        print(s)
#help(pytz.country_timezones)
print_list(pytz.country_timezones['RS'])

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x, " : ", pytz.country_names[x])