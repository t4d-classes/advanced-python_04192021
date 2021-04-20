""" time delta demo module """

from datetime import datetime, timedelta

start = datetime.now()

end = start + timedelta(days=20)

print(start)
print(end)
