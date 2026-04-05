# import the needed Python modules
import pytz
import datetime
import argparse
import TimeZoneException as TimeZoneException

#
def get_countrycode_of_timezone(wished_timezone):

     #
     for countrycode in pytz.country_timezones:

          timezones = pytz.country_timezones[countrycode]

          #
          for timezone in timezones:
 
               #
               if timezone == wished_timezone :

                    #
                    return countrycode

#
def get_all_timezones():

    #
    return pytz.all_timezones

#
def get_all_common_timezones():

     #
     return pytz.common_timezones
	
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
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=0)
    
    #
    args = parser.parse_args()

    #
    print(get_all_timezones())

    #
    print(get_countrycode_of_timezone("Europe/Paris"))

    #
    print(get_all_common_timezones())
    
    #
    if get_datetime_for_particular_timezone(args.timezone) != -1 :
    
         #
         print(args.timezone + " : " + get_datetime_for_particular_timezone(args.timezone).strftime("%Y:%m:%d %H:%M:%S"))

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)