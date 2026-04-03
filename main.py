import modules.Clock as Clock
from tzlocal.windows_tz import win_tz

#
iana_tz = win_tz.get("Romance Standard Time")

#
clock = Clock.Clock(iana_tz)

#
clock.mainloop()