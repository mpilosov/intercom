#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Intercom test. This script reads in a list of JSON-encoded customer records
# and outputs the names and IDs of all customers within 100km of Intercom's
# Dublin office.
#
# Tested using Python 3.6.3.
#
# Author: Darren Mulholland <dmulholl@tcd.ie>
# ------------------------------------------------------------------------------

import json
import dist


# Loads and returns a list of customer records from the specified file, where
# each line of the file is a JSON-encoded record.
def load_customer_list(filepath):
    customers = []
    with open(filepath) as file:
        for line in file:
            customers.append(json.loads(line))
    return customers


# Prints the name and ID of each customer in the specified list.
def print_customer_list(customers):
    print('  --     ----')
    print('  ID     NAME')
    print('  --     ----')
    for customer in customers:
        print('%4s  |  %s' % (customer['user_id'], customer['name']))


def main():
    office_pos = dist.Pos(53.339428, -6.257664)
    local_customers = []

    for customer in load_customer_list('customers.json'):
        latitude = float(customer['latitude'])
        longitude = float(customer['longitude'])
        customer_pos = dist.Pos(latitude, longitude)
        if dist.distance(office_pos, customer_pos) < 100:
            local_customers.append(customer)

    local_customers.sort(key=lambda c: c['user_id'])
    print_customer_list(local_customers)


if __name__ == '__main__':
    main()
