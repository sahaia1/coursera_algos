# Uses python3
import sys
import random

def sortStartEnd(starts, ends):
    ranges = [(a,b) for a, b in zip(starts, ends)]
    ranges.sort(key=lambda x: x[0])
    return ranges

def binSearch(ranges, point):
    low = 0
    high = len(ranges) - 1
    while low <= high:
        mid = (low + high) // 2
        if ranges[mid][0] <= point and ranges[mid][1] >= point:
            return mid
        elif ranges[mid][0] > point:
            high = mid - 1
        else:
            low = mid + 1 
    return -1

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    ranges = sortStartEnd(starts, ends)
    print(ranges)
    l_ranges = len(ranges)
    for i, point in enumerate(points):
        s = binSearch(ranges, point)
        if s != -1:
            for j in range(s, l_ranges):
                if ranges[j][0] >= point:
                    break
                else:
                    cnt[i] += 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def test_sort():
    starts = reversed([1,2,3,4,5,6])
    ends = reversed([2,3,4,5,6,7])
    print(sortStartEnd(starts, ends))

def test():
    num_lines = random.randint(1, 50)
    num_points = random.randint(1, 50)
    starts = []
    ends = []
    points = []
    for _ in range(num_lines):
        ends.append(random.randint(-1000, 1000))
        starts.append(random.randint(-1000, ends[-1]))
    points = [random.randint(-1000, 1000) for _ in range(num_points)]
    cnt = naive_count_segments(starts, ends, points)
    cnt2 = fast_count_segments(starts, ends, points)
    if cnt != cnt2:
        print("didn't match")
        print(starts)
        print(ends)
        print(points)

def test_break():
    starts = [49, -753, -678, -829]
    ends = [727, -750, 495, -339]
    points = [968, 193, -239, 943, 64, 679, -192, 746, -499, 450, -414, 774, 760, 794, 5, -39, -871, -235, 700, 474, 596, -114, 835, 708, 667, 529, -955, -77, 661, 843, -813, 760, -508, -843, 291, 797, -262, 709, -637, 808, 411, -459, 605, -905, -826, 904, 33, 851, -757]

    cnt = naive_count_segments(starts, ends, points)
    cnt2 = fast_count_segments(starts, ends, points)
    for i, point in enumerate(points):
        if cnt[i] != cnt2[i]:
            print(point, cnt[i], cnt2[i])


def main():
    # for _ in range(100):
    #     test()
    test_break()

if __name__ == '__main__':
    main()
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
