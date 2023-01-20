#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys

j = 0
total_size = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
dict = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}

def printstatus(dict, total_size):
    """print status"""
    print("File size: {}".format(total_size))
    for item in status:
        if dict[item]:
            print("{}: {}".format(item, dict[item]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if j != 0 and j % 10 == 0:
                printstatus(dict, total_size)
            mylist = line.split(' ')
            if len(mylist) != 9:
                continue
            j += 1
            try:
                total_size += int(mylist[-1])
                stat = int(mylist[-2])
            except Exception:
                pass
            if stat in status:
                dict[stat] += 1
        printstatus(dict, total_size)
    except KeyboardInterrupt:
        printstatus(dict, total_size)
        raise
