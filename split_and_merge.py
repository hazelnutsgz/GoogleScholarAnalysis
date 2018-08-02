import multiprocessing
import sys
import subprocess

cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)
split_number = int(sys.argv[1])


def call_sub(index):
    instruction = "python " + "citation_preprocess_new.py " + str(index) + " " + split_number
    subprocess.call(instruction, shell=True)


pool.map(call_sub, [i for i in range(split_number)])