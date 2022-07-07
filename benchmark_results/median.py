import os
import statistics
import numpy as np

files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./") for f in fn if ('opt' in f) and ('median' not in f)]


benchmarks = {}

for path in files:
    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        data = [s.strip() for s in line.split(',')]

        name = data[0]
        stat = data[1:]

        if name in benchmarks.keys():
            benchmarks[name].append(stat)
        else:
            benchmarks[name] = [stat]


medians = {}
for name, stat in benchmarks.items():
    data = []
    stat = np.array(stat).T.tolist()

    for column in stat:
        if len(column) == 3:
            data.append(statistics.median(column))

    if len(data) == 0:
        continue

    medians[name] = data

with open('median_opt.csv', 'w') as f:
    for name in benchmarks.keys():
        for stat in benchmarks[name]:
            if stat[2] == medians[name][2]:
                f.write(','.join([name] + stat) + '\n')
