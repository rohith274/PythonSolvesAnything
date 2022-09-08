# A node in LinkedList is a dictionary. It is value + next(address)
head = {
    "value": 11,
    "next": {
        "value": 12,
        "next": {
            "value": 3,
            "next": {"value": 11,
                     "next": None

                     }
        }
    }
}

print(head['next']['next']['value'])
# so a linked list is nothing but a dictionary.
