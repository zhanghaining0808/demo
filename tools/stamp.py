import time

def generate_stamp():
    return int(time.time())

def convert_stamp(stamp):
    timeArray = time.localtime(stamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)