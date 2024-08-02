#!/usr/bin/python3
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list where each element is a list containing keys
                           (represented as integers) that can open other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

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
                #key corresponds to box number and hasn't been opened, open it
                opened_boxes.add(key)
                queue.append(key)

    # Check if we have opened all the boxes
    return len(opened_boxes) == n
