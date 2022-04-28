from datetime import datetime, timedelta
#import time

# current date and time
FirstStartTime = datetime.now()
# format:  YYYY-MM-DD hh:mm:ss.msm like 2016-10-04 10:09:35.699
mydate = FirstStartTime.strftime("%Y") + "-" + FirstStartTime.strftime("%m") + "-" + FirstStartTime.strftime("%d")
print(mydate)