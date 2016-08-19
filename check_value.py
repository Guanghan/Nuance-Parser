#! /usr/bin/env python 

import sys

def check_string(query, value):
    query = query.lower()
    value = value.lower()

    #print query
    #print value

    if query.count(value) > 0:
        return True
    else:
        return False


def test(query, value):
    print(check_string(query, value))


if __name__ == '__main__':
    test(sys.argv[1], sys.argv[2])


