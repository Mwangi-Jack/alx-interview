#!/usr/bin/python3
"""lockboxes"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    This function takes in a list 'boxes' which contains lists of
    integer values
    """
    def dfs(box: int, unlocked: set) -> None:
        if box in unlocked:
            return

        unlocked.add(box)

        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                dfs(key, unlocked)

    unlocked = set()

    dfs(0, unlocked)

    return len(unlocked) == len(boxes)
