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
        self.members = {}       # key of char, value idx of last occurence

    def __str__(self):
        return "count=%d, members=%s" % (self.count, self.members)


class UniqueChars:
    def __init__(self):
        self.count = 0
        self.occurs = {}        # key of char, value idx of first occurrence
        self.repeated = set()   # indices of repeats

    def __str__(self):
        return "count=%d, occurs=%s, repeated=%s" % \
            (self.count, self.occurs, self.repeated)


def substringDistinct(s, distinctMax=0):
    current = [0, 0]    # start, end
    longest = (0, 0)    # start, end

    distinct = DistinctChars()

    while current[START] < len(s):
        underLimit = isUnderLimitOrNoLimitSet(distinct.count, distinctMax)
        longest = maxSubstringLimitedTo(longest, current, underLimit)

        if underLimit and current[END] < len(s):
            if s[current[END]] not in distinct.members:
                distinct.count += 1
            distinct.members[s[current[END]]] = current[END]
            current[END] += 1
        else:
            if distinct.members[s[current[START]]] == current[START]:
                distinct.count -= 1
                del distinct.members[s[current[START]]]

            current[START] += 1

    return s[longest[START]:longest[END]]


def substringUnique(s, uniqueMax=0):
    unique = getIndicesOfRepeated(s)

    longest = findLongestUniqueUsingRepeats(s, unique, uniqueMax)

    return s[longest[START]:longest[END]]


def getIndicesOfRepeated(s):
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


def findLongestUniqueUsingRepeats(s, unique, uniqueMax):
    current = [0, 0]
    longest = (0, 0)

    while current[START] < len(s):
        underLimit = isUnderLimitOrNoLimitSet(unique.count, uniqueMax)
        longest = maxSubstringLimitedTo(longest, current, underLimit)

        if (underLimit and current[END] < len(s) and
           current[END] not in unique.repeated):
            unique.count += 1
            current[END] += 1
        else:
            if current[START] in unique.repeated:
                unique.count = 0
                current[START] = current[END]
                current[END] += 1

            current[START] += 1

    return longest


def maxSubstringLimitedTo(longest, current, underLimit):
    if underLimit and \
       (current[END] - current[START] > longest[END] - longest[START]):
        return (current[START], current[END])
    else:
        return longest


def isUnderLimitOrNoLimitSet(count, limit):
    return not limit or (count <= limit)
