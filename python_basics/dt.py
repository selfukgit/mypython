import time
import calendar 

ticks = time.time()

print "Number of ticks since 12:00am, January 1, 1970:", ticks

print "###########################"

localtime = time.localtime(time.time())
print "Local current time :", localtime

print "###############"


t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)
print "#####################################"
cal = calendar.month(2015, 3)
print "Here is the calendar:"
print cal;
