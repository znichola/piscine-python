from datetime import datetime

now = datetime.now()
ts = now.timestamp()

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# https://docs.python.org/3/library/string.html#formatspec

print(f'Seconds since January 1, 1970: {format(ts, ",.14")} or {format(ts, ".3")} in scientific notation')
print(now.strftime("%b %d %Y"))