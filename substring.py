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


class DistinctChars:
    def __init__(self):
        self.count = 0
        self.members = {}


class UniqueChars:
    def __init__(self):
        self.count = 0
        self.occurs = {}        # key of character, value of first occurrence
        self.repeated = set()   # indices of repeats

    def __str__(self):
        return "count=%d, occurs=%s, repeated=%s" % \
            (self.count, self.occurs, self.repeated)


class SubstringIndices:
    def __init__(self):
        self.start = 0
        self.end = 0

    def __str__(self):
        return "start=%d, end=%d" % (self.start, self.end)


def substringDistinct(s, distinctMax):
    stringLength = len(s)
    current = SubstringIndices()
    longest = SubstringIndices()

    distinct = DistinctChars()

    while current.start < stringLength:
        if current.end - current.start > longest.end - longest.start:
            if distinct.count <= distinctMax:
                # longest = current  in Python copies only the reference
                longest.end = current.end
                longest.start = current.start

        if distinct.count <= distinctMax and current.end < stringLength:
            if not s[current.end] in distinct.members:
                distinct.count += 1
            distinct.members[s[current.end]] = current.end
            current.end += 1
        else:
            if distinct.members[s[current.start]] == current.start:
                del distinct.members[s[current.start]]
                distinct.count -= 1
            current.start += 1

    return s[longest.start:longest.end]


def substringUnique(s, uniqueMax):
    stringLength = len(s)

    current = SubstringIndices()
    longest = SubstringIndices()

    unique = UniqueChars()

    while current.start < stringLength:
        if s[current.start] not in unique.occurs:
            unique.occurs[s[current.start]] = current.start
        else:
            unique.repeated.add(current.start)
            unique.repeated.add(unique.occurs[s[current.start]])

        current.start += 1

    current = SubstringIndices()

    while current.start < stringLength:
        if current.end - current.start > longest.end - longest.start:
            if unique.count <= uniqueMax:
                # longest = current  in Python copies only the reference
                longest.end = current.end
                longest.start = current.start

        if (unique.count <= uniqueMax and current.end < stringLength and
           current.end not in unique.repeated):
            unique.count += 1
            current.end += 1
        else:
            if current.start in unique.repeated:
                unique.count = 0
                current.start = current.end
                current.end += 1

            current.start += 1

    return s[longest.start:longest.end]


def maxSubstring(longest, current):
    if current.end - current.start > longest.end - longest.start:
        return current
    else:
        return longest


