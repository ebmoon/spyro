def find_linenum_starts_with(lines, target, start=0):
    for i, line in enumerate(lines[start:]):
        if 0 == line.find(target):
            return start+i

    return -1