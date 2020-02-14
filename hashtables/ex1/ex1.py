#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # INSERT ALL WEIGHTS INTO HASHTABLE
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    # CHECK IF LENGTH IS 1 AND RETURN NONE IF IT IS
    if length == 1:
        return None

    # FOR EACH WEIGHT, CHECK IF THE SUBTRACTING THE WEIGHT FROM LIMIT HAS A KEY IN HASHTABLE
    for i in range(length):
        first = weights[i]

        # IF THERE IS A VALID KEY, RETURN BOTH INDEXES
        if hash_table_retrieve(ht, limit - first) != None:
            first_weight_index = i
            second_weight_index = hash_table_retrieve(ht, limit - first)

            return (second_weight_index, first_weight_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
