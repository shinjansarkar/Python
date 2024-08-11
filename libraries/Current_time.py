import time

seconds = time.time()
localtime = time.localtime(seconds)
years=localtime.tm_year
months = localtime.tm_mon   # For months this (mon)
day=localtime.tm_mday       # For Day this (mday)

print("Years:",years)
print("Date:",day)
print("Month:",months)
