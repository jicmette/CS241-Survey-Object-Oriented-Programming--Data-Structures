ed_level_counts = dict()

with open("census.csv", "r") as i_file:
    for line in i_file:
        column = line.split(", ")
        degree = column[3]
        if degree in ed_level_counts:
            ed_level_counts[degree] += 1
        else:
            ed_level_counts = 1

    for degree, count in ed_level_counts.items():
        print("{:5} -- {}".format(count, ed_level_counts))