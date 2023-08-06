#!/usr/bin/python3
def canUnlockAll(boxes):
        num_boxes = len(boxes)
        unlocked_boxes = set()
        unlocked_boxes.add(0)  # First box is unlocked by default

        # Start with the keys in the first box
        keys = boxes[0]

        while keys:
            new_keys = []

            for key in keys:
                if key < num_boxes and key not in unlocked_boxes:
                    unlocked_boxes.add(key)
                    new_keys.extend(boxes[key])

            keys = new_keys

        return len(unlocked_boxes) == num_boxes
