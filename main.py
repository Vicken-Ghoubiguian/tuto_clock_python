#
import argparse

#
import modules.clock as Clock
import modules.dt_management as dt_management

# import the custom exceptions as Python modules
import modules.custom_Exceptions.TimeZoneException as TimeZoneException


#
iana_tz = dt_management.return_iana_timezone()

#
parser = argparse.ArgumentParser(description="Simple app with timezones")

#
parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)

#
parser.add_argument('--dt_format', action="store", dest='dt_format', default='%Y-%m-%d %H:%M:%S')

#
parser.add_argument('--zoom_map', action="store", dest='zoom_map', default=12)

#
args = parser.parse_args()

#
if dt_management.get_datetime_for_particular_timezone(args.timezone) != None :

    #
    clock = Clock(args.timezone, args.dt_format, args.zoom_map)

#
else :
         
    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

#
clock.mainloop()

