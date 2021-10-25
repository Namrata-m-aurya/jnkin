import os
import time
import datetime
def count_words(fname):
    num_words = 0
 
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    return num_words
path_to_watch = "/../../../docker_host/"
before = dict ([(f, count_words("/../../../docker_host/"+f)) for f in os.listdir (path_to_watch)])
print(before)
while 1:
        time.sleep(10)
        after = dict ([(f,count_words("/../../../docker_host/"+f)) for f in os.listdir (path_to_watch)])
        print(datetime.datetime.now(),':',after)
