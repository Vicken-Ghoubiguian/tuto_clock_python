#
import pytz

#
def get_all_timezones():

    #
    return pytz.all_timezones
	
#
def get_datetime_for_particular_timezone(destination_timezone):

    #
    if destination_timezone in pytz.all_timezones :
    
         #
         return 0
    
    #
    else :
    
         #
         return -1
    
#
if __name__ == "__main__":

    #
    print(get_all_timezones())
    print(get_datetime_for_particular_timezone("Europe/Berlin"))