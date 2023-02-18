#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
    pattern = r"[\w\.-]+@" + domain + "$"
    if re.match(pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
    the received address."""

    address = re.sub(r"" + old_domain + "$", new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
    csv_file_location = '/home/student-02-1cc4ea81a704/data/user_emails.csv'
    report_file = '/home/student-02-1cc4ea81a704/data' + '/updated_user_emails.csv'
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [i[1].strip() for i in user_data_list[1:]]
        for i in user_email_list:
            if contains_domain(i, old_domain):
                old_domain_email_list.append(i)
                r = replace_domain(i, old_domain, new_domain)
                new_domain_email_list.append(r)
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain
        f.close()
    # print(user_data_list)
    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()


