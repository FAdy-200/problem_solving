##!/usr/bin/env python3

import sys
import os
import re


def error_search(log_file):
    error = input().split()
    file = open(log_file, "r")
    of = open("errors_found.txt", "w")
    nerror = rf".+".join(f"{i}" for i in error)
    for log in file.readlines():
        if re.search(nerror, log):
            of.write(log)
    file.close()
    of.close()


(error_search("data.log"))
