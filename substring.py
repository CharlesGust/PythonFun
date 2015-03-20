#
# Find the longest substring that contains only N distinct characters
#
#     "abbbbbccdef"
#           should return "abbbbbcc" for N == 3
#
# (This is different from finding the longest substring that contains
#   only N unique characters. There are some computer programmers
#   who cannot distinguish between "distinct" and "unique". The
#   longest substring that contains only 3 unique characters is "def" )
#
#   unique refers to something that there is only one of
#   distinct refers to something that is different from another
#


class DistinctChars:
    def __init__(self):
        self.count = 0
        self.members = {}


class SubstringIndices:
    def __init__(self):
        self.start = 0
        self.end = 0


def substringDistinct(s, distinctMax):
    stringLength = len(s)
    current = SubstringIndices()
    longest = SubstringIndices()

    distinct = DistinctChars()

    while current.start < stringLength:
        if current.end - current.start > longest.end - longest.start:
            if distinct.count <= distinctMax:
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


