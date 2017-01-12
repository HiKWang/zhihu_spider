import os
filename = 'cookies'
try:
	os.remove(filename)
except Exception as e:
	raise e