#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)
    queue = [0]


    while queue:
        current_box = queue.pop(0)
        # Get all the keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in opened_boxes:
                # If the key corresponds to a box number and hasn't been opened, open it
                opened_boxes.add(key)
                queue.append(key)
    
    # Check if we have opened all the boxes
    return len(opened_boxes) == n
