#!/usr/bin/env python

import subprocess
from multiprocessing import Pool
import os


def run(data):
    src, dest = data
    # Do something with task here
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":

    tasks = []
    src = "/home/student-02-a1aa15682ca5/data/prod/"
    dest = "/home/student-02-a1aa15682ca5/data/prod_backup/"
    for root, dirs, files in os.walk(src, topdown=False):
        for name in dirs:
            path = os.path.join(root, name)
            npath = path.replace("prod/","prod/data/prod_backup/")
            tasks.append((path,npath))
    # Create a pool of specific number of CPUs
    p = Pool(len(tasks))
    # Start each task within the pool
    p.map(run, tasks)
