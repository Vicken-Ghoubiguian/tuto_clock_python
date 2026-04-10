# import the needed Python modules
import pytz
import datetime
import argparse
import TimeZoneException as TimeZoneException

# from the needed Python modules import needed components
from tzlocal.windows_tz import win_tz

#
def get_countrycode_of_timezone(wished_timezone):

     #
     foundCountryCode = None

     #
     for countrycode in pytz.country_timezones:

          timezones = pytz.country_timezones[countrycode]

          #
          for timezone in timezones:
 
               #
               if timezone == wished_timezone :

                    #
                    foundCountryCode = countrycode

                    #
                    break
               
     #
     return foundCountryCode

# Definition of a function to get all timezones
def get_all_timezones():

    # Returning a list of all timezones
    return pytz.all_timezones

# Definition of a function to get all common timezones
def get_all_common_timezones():

     # Returning a list of all common timezones
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
         return None
    
#
if __name__ == "__main__":
    
    #
    iana_tz = win_tz.get("Romance Standard Time")

    #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)

    #
    parser.add_argument('--dt_format', action="store", dest='dt_format', default='%Y:%m:%d %H:%M:%S')
    
    #
    args = parser.parse_args()

    #
    print(get_all_timezones())

    #
    print(get_all_common_timezones())
    
    #
    if get_datetime_for_particular_timezone(args.timezone) != None :
         
         #
         if get_countrycode_of_timezone(args.timezone) != None :
              
              #
              print(args.timezone + " (" + get_countrycode_of_timezone(args.timezone) + ") : " + get_datetime_for_particular_timezone(args.timezone).strftime(args.dt_format))
         #
         else :

              #
              print(args.timezone + " : " + get_datetime_for_particular_timezone(args.timezone).strftime(args.dt_format))

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)