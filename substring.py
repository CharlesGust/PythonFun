#
#   This package illustrates the difference between "unique" and "distinct"
#   The are some folks who use these terms interchangeably, however:
#
#       unique refers to something that there is only one of
#       distinct refers to something that is different from another
#
# Find the longest substring that contains only N distinct characters
#
#       "abbbbbccdef"
#           should return "abbbbbcc" for N == 3
#
# Find the longest substring that contains only N unique characters
#
#       "abbbbbccdef"
#           should return "def" for N == 3
#

# SYMBOLIC CONSTANTS IN UPPERCASE
START = 0
END = 1


class DistinctChars:
    def __init__(self):
        self.count = 0          # count of series of distinct chars
        self.continue_char_index = {} # key of char, value idx of last occurence

    def __str__(self):
        return "count=%d, continue_char_index=%s" % (self.count, self.continue_char_index)


class UniqueChars:
    def __init__(self):
        self.count = 0
        self.occurs = {}        # key of char, value idx of first occurrence
        self.repeated = set()   # indices of repeats

    def __str__(self):
        return "count=%d, occurs=%s, repeated=%s" % \
            (self.count, self.occurs, self.repeated)


def substring_distinct(s, distinct_max=0):
    if distinct_max == 0:
        return s

    current = [0, 0]    # start, end
    longest = (0, 0)    # start, end

    distinct = DistinctChars()

    while current[START] < len(s):
        under_limit = under_limit_or_no_limit(distinct.count, distinct_max)
        longest = max_substring_limited_to(longest, current, under_limit)

        current, distinct = advance_start_or_end_for_distinct(current,
                                                              distinct,
                                                              s,
                                                              under_limit
                                                              )

    return s[longest[START]:longest[END]]


def advance_start_or_end_for_distinct(current, distinct, s, under_limit):
    if under_limit and current[END] < len(s):
        if s[current[END]] not in distinct.continue_char_index:
            distinct.count += 1
        distinct.continue_char_index[s[current[END]]] = current[END]
        current[END] += 1
    else:
        if distinct.continue_char_index[s[current[START]]] == current[START]:
            distinct.count -= 1
            del distinct.continue_char_index[s[current[START]]]

        current[START] += 1

    return current, distinct


def substring_unique(s, unique_max=0):
    unique = build_repeated_positions(s)

    longest = find_longest_unique_using_repeats(s, unique, unique_max)

    return s[longest[START]:longest[END]]


def build_repeated_positions(s):
    current = [0, 0]

    unique = UniqueChars()

    while current[START] < len(s):
        if s[current[START]] not in unique.occurs:
            unique.occurs[s[current[START]]] = current[START]
        else:
            unique.repeated.add(current[START])
            unique.repeated.add(unique.occurs[s[current[START]]])

        current[START] += 1

    return unique


def find_longest_unique_using_repeats(s, unique, unique_max):
    current = [0, 0]
    longest = (0, 0)

    while current[START] < len(s):
        under_limit = under_limit_or_no_limit(unique.count, unique_max)
        longest = max_substring_limited_to(longest, current, under_limit)

        current, unique = advance_start_or_end_for_unique(current,
                                                          unique,
                                                          s,
                                                          under_limit
                                                          )

    return longest


def advance_start_or_end_for_unique(current, unique, s, under_limit):
    if (under_limit and current[END] < len(s) and
       current[END] not in unique.repeated):
        unique.count += 1
        current[END] += 1
    else:
        if current[START] in unique.repeated:
            unique.count = 0
            current[START] = current[END]
            current[END] += 1

        current[START] += 1

    return current, unique


def max_substring_limited_to(longest, current, under_limit):
    if under_limit and \
       (current[END] - current[START] > longest[END] - longest[START]):
        return (current[START], current[END])
    else:
        return longest


def under_limit_or_no_limit(count, limit):
    return not limit or (count <= limit)
