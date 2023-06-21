points = [
    ["a", 13.5],
    ["b", 10.5],
    ["c", 8],
    ["d", 8],
    ["e", 7.5],
    ["f", 4],
    ["aa", 11.5],
    ["ab", 10.5],
    ["ac", 10],
    ["ad", 8],
    ["ae", 8],
    ["af", 7],
    ["ag", 6],
    ["ah", 4.5],
    ["ai", 4],
    ["aaa", 13.5],
    ["aab", 11],
    ["aac", 9.5],
    ["aad", 9],
    ["aae", 7],
    ["aaf", 5.5],
    ["aag", 4.5],
    ["aah", 4],
    ["aaaa", 14.5],
    ["aaab", 14],
    ["aaac", 13],
    ["aaad", 6.5],
    ["aaae", 6],
    ["aaaf", 6],
    ["aaag", 4.5],
    ["aaaaa", 16],
    ["aaaab", 12],
    ["aaaac", 11],
    ["aaaad", 9.5],
    ["aaaae", 7],
    ["aaaaf", 5],
    ["aaaag", 4],
]

# points.sort_values()
# sorted(points, key=lambda x: x[1])
points.sort(key=lambda x: x[1], reverse=True)
# print(points)

p = 0
for i in points:
    point = i[1]
    p = p + point
    if p > 100:
        break
    print(p)
