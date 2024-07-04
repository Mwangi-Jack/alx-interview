#!/usr/bin/python3
"""lockboxes"""

def canUnlockAll(boxes):
    """lockboxes"""
    unlocked = set()
    stack = [0]

    while stack:
        current_box = stack.pop()

        if current_box not in unlocked:
            unlocked.add(current_box)

            for key in boxes[current_box]:
                if key not in unlocked:
                    stack.append(key)

    return len(unlocked) == len(boxes)
