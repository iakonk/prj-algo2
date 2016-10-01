def count_matches(line_x, line_y):
    """
    receives two lines,
    calculates counter of matches
    :param line_x: world
    :param line_y: wolf
    :return: two dementia array of match counters
                  0  1     2     3     4
           0 [    0, 0(w), 0(o), 0(l), 0(f)],
           1 [(w) 0, 1,    1,    1,    1],
           2 [(o) 0, 1,    2,    2,    2],
           3 [(r) 0, 1,    2,    2,    2],
           4 [(l) 0, 1,    2,    3,    3],
           5 [(d) 0, 1,    2,    3,    3]]
    len of the longest match would be elem from the result array[5][4] (3) for string X[:4 + 1] = wolf, Y[: 5 + 1] = world
    """
    line_x = (' %s' % line_x, line_x)[line_x[0].isspace()]
    line_y = (' %s' % line_y, line_y)[line_y[0].isspace()]
    len_x = len(line_x)
    len_y = len(line_y)
    matches_table = [[0] * (len_y) for i in range(len_x)]

    for ind_x in range(1, len_x):
        for ind_y in range(1, len_y):
            if line_x[ind_x] == line_y[ind_y]:
                matches_table[ind_x][ind_y] = matches_table[ind_x - 1][ind_y - 1] + 1
            else:
                matches_table[ind_x][ind_y] = max(matches_table[ind_x][ind_y - 1], matches_table[ind_x - 1][ind_y])

    return matches_table

def get_longest_subst(line_x, line_y, matches_table, ind_x, ind_y):
    if matches_table[ind_x][ind_y] == 0:
        return ' '
    if line_x[ind_x].strip() == line_y[ind_y].strip():
        return '%s%s' % (get_longest_subst(line_x, line_y, matches_table, ind_x - 1, ind_y - 1), line_x[ind_x])
    elif line_x[ind_x].strip() != line_y[ind_y].strip() and matches_table[ind_x][ind_y - 1] > matches_table[ind_x - 1][ind_y]:
        return get_longest_subst(line_x, line_y, matches_table, ind_x, ind_y - 1)
    elif line_x[ind_x] != line_y[ind_y] and matches_table[ind_x][ind_y - 1 ] < matches_table[ind_x - 1][ind_y]:
        return get_longest_subst(line_x, line_y, matches_table, ind_x - 1, ind_y)
    return ''

line_x = ' world'
line_y = ' wolf'
matches = count_matches(line_x, line_y)

l=''
for x in reversed(range(0, len(line_x))):
    for y in reversed(range(0, len(line_y))):
        print(x, y)
        l += get_longest_subst(line_x, line_y, matches, x, y)

print(l)
