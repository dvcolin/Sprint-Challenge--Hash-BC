#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # INSERT ALL TICKETS INTO HASHTABLE
    for item in tickets:
        hash_table_insert(hashtable, item.source, item.destination)

    # VALUE OF FIRST LOCATION IS NONE, SET LOCATION TO FIRST VALUE IN ROUTE ARRAY
    first = hash_table_retrieve(hashtable, 'NONE')
    route[0] = first

    # SET CURRENT INDEX TO 1, STARTING AT 2ND ITEM
    current_index = 1

    # WHILE CURRENT INDEX IS LESS THAN LENGTH OF ARRAY, USE PREVIOUS LOCATION AS PARAMETER IN HASHTABLE RETRIEVE
    for i in range(length):
        if hash_table_retrieve(hashtable, route[current_index - 1]) != 'NONE':
            next_location = hash_table_retrieve(
                hashtable, route[current_index - 1])

            # SET THE LOCATION TO BE THE NEXT ITEM IN ROUTE ARRAY
            route[current_index] = next_location
            current_index += 1
        else:

            # IF LOCATION VALUE IS NONE, SET THAT LOCATION TO BE THE LAST IN THE ARRAY
            route[length - 1] = route[current_index - 1]

    return route[:length - 1]
