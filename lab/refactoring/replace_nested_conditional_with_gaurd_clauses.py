# by Kami Bigdely
# Replace nested conditional with gaurd clauses


def has_position(line):
    "Check if the line has a position in it marked by x:"
    return 'x:' in line


def no_positon_found(line):
    "We didn't recive a line of we found something denoting it won't have a position, i.e debug or error"
    return not line or (('debug') or ('error') in line)


def extract_position(line):
    if has_position(line):
        start_index = line.find('x:') + 2
        pos = line[start_index:]  # from start_index to the end.
    elif no_positon_found(line):
        pos = None
    return pos


if __name__ == "__main__":
    result1 = extract_position(
        '|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
