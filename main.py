#
import pytz
import datetime

#
def get_all_timezones():

    #
    return pytz.all_timezones
	
#
def get_datetime_for_particular_timezone(destination_timezone):

    #
    if destination_timezone in pytz.all_timezones :
    
         #
         dtz = pytz.timezone(destination_timezone)
         
         #
         return datetime.datetime.now(dtz)
    
    #
    else :
    
         #
         return -1
    
#
if __name__ == "__main__":

    #
    print(get_all_timezones())
    print("Pacific/Auckland" + " : " + get_datetime_for_particular_timezone("Pacific/Auckland").strftime("%Y:%m:%d %H:%M:%S"))