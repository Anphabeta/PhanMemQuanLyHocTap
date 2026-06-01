import time
from datetime import datetime
import inspect

DEBUG = False

def curTime():
	now = datetime.now()
	return now.strftime("%H:%M:%S.%f")


def log(*args):
	if not DEBUG:
		return

	frame = inspect.currentframe().f_back
	func = frame.f_code.co_name

	print(f"[{curTime()}] <in {func}>", *args)

def plainLog(text):
	if not DEBUG:
		return

	print(f"--- {text.strip().upper()} ---")

def log_view(*args):
	if not DEBUG:
		return

	frame = inspect.currentframe().f_back
	func = frame.f_code.co_name

	print(f"[{curTime()}] [VIEW] <in {func}>", *args)

def log_controller(*args):
	if not DEBUG:
		return

	frame = inspect.currentframe().f_back
	func = frame.f_code.co_name

	print(f"[{curTime()}] [CTRL] <in {func}>", *args)

def log_model(*args):
	if not DEBUG:
		return

	frame = inspect.currentframe().f_back
	func = frame.f_code.co_name

	print(f"[{curTime()}] [MODEL] <in {func}>", *args)

# def log(*args):
# 	if not DEBUG:
# 		return
# 	print(f"[{time.strftime('%H:%M:%S')}]", *args)


if __name__ == '__main__':
	log("Hello")