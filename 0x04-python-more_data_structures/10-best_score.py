#!/usr/bin/python3
def best_score(a_dictionary):
    final_key = ""
    init_val = 0
    if a_dictionary:
        for key, val in a_dictionary.items():
            if val > init_val:
                init_val = val
                final_key = key
        return final_key