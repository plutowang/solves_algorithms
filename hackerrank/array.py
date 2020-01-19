def hourglassSum(arr):
    # 2D Array - DS
    max_n = -9 * 7
    for i in range(4):
        for j in range(4):
            if i + 2 < 6 and j + 2 < 6:
                top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                mid = arr[i+1][j+1]
                bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                max_n = max((top+mid+bot), max_n)
    return max_n


def rotLeft(a: list, d: int):
    # Left Rotation
    n_pos = d % len(a)
    return a[n_pos::] + a[:n_pos:]

def minimumBribes(q):
    # New Year Chaos
    


if __name__ == '__main__':
    print(minimumBribes([1, 2, 3, 4, 5]))
    # nums = list(range(1, 6))
    # print(nums[0])
