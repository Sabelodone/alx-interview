#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    for key in range(1, len(boxes)):
        found = False
        for idx, box in enumerate(boxes):
            if key in box and key != idx:
                found = True
                break
        if not found:
            return False
    return True
