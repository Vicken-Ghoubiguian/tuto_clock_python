import modules.Clock as Clock
import platform
import subprocess
from tzlocal.windows_tz import win_tz

#
if platform.system() == "Windows" :
    
    #
    iana_tz = win_tz.get("Romance Standard Time")

#
elif platform.system() == "Linux" :
         
    #
    iana_tz = subprocess.check_output("cat /etc/timezone", shell=True, text=True).replace("\n", "")

#
elif platform.system() == "Darwin" :

    #
    iana_tz = subprocess.check_output("readlink /etc/localtime | sed 's#/var/db/timezone/zoneinfo/##g'", shell=True, text=True).replace("\n", "") 

#
else :
         
    #
    iana_tz = "Etc/UTC"