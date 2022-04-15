#!/usr/bin/python3
"""
Code to unlock boxes, where the keys for the other boxes might be in a box.
The firs box is open
"""


def canUnlockAll(boxes):
    """ find every key to open all """
    size = len(boxes)
    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys and key < size:
                keys.append(key)
    if len(keys) == size:
        return True
    else:
        return False
