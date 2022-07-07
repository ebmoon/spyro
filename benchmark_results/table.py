import sys

with open("median_opt.csv", "r") as f:
    lines = f.readlines()
    datas = [line.split(",") for line in lines]

filename = sys.argv[1]

for data in datas:
    if filename in data[0]:
        start = 23
        interval = 15
        offset = 4
        
        l = [data[start], str(float(data[start + offset]) + float(data[start + interval + offset]))]
        l += [data[start + 2 * interval], data[start + 2 * interval + offset]]
        l += [data[start + 3 * interval], data[start + 3 * interval + offset]]
        l += [data[-2], data[3]]

        print (" & ".join(l))