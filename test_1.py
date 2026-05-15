#
import argparse

# import the custom modules as Python modules
import tuto_clock_python.Clock as Clock
import tuto_clock_python.dt_management as dt_management

# import the custom exceptions as Python modules
import tuto_clock_python.TimeZoneException as TimeZoneException


#  Get the current timezone of the system
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
parser.add_argument('--width', action="store", dest='width', default=1500)

#
parser.add_argument('--height', action="store", dest='height', default=500)

#
parser.add_argument('--title', action="store", dest='title', default='Clock')

#
args = parser.parse_args()

#
if dt_management.get_datetime_for_particular_timezone(args.timezone) != None :

    #
    clock = Clock.Clock(args.timezone, args.dt_format, args.zoom_map, args.title, args.width, args.height)

#
else :
         
    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

#
clock.run()

