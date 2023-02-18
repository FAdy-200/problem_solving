#!/usr/bin/env python3
import csv


def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    return [i for i in employee_file]


def process_data(employee_list):
    ans = dict()
    # ans.items()
    for i in employee_list:
        ans[i["Department"]] = ans.get(i["Department"], 0) + 1
    return ans


def write_report(dictionary, report_file):
    sor = sorted(dictionary)
    with open(report_file, "w+") as f:
        f.write("\n".join([f"{i}:{dictionary[i]}" for i in sor]))
    return


emp = read_employees("emp.csv")
lis = process_data(emp)
write_report(lis, "rep.txt")
