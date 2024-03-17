#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    # Set to keep track of opened boxes
    opened_boxes = {0}

    # Queue to perform BFS traversal of boxes
    queue = [0]

    # Perform BFS traversal
    while queue:
        box_idx = queue.pop(0)
        for key in boxes[box_idx]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
