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
    # if len(q) < 2:
    #     return 0
    # bribes = q[0] - q[1]
    # if bribes > 2:
    #     return 'Too chaotic'
    # if bribes < 0:
    #     return minimumBribes(q[1::])
    # return bribes + minimumBribes(q[1::])
    is_chaotic = False
    count = 0
    for idx, pos in enumerate(q):
        pn = pos - 1
        if pn - idx > 2:
            is_chaotic = True
            break
        for i in range(max(0, pn-1), idx):
            if q[i] > pos:
                count += 1
    print('Too chaotic' if is_chaotic else count)


def minimumSwaps(arr):
    # Minimum Swaps 2
    # Time Out!
    # swap = 0
    # for i, _ in enumerate(arr):
    #     while arr[i] != i+1:
    #         arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
    #         swap += 1
    #     i += 1
    # return swap
    sorted_arr = sorted(arr)
    idx_dic = {val: i for i, val in enumerate(arr)}
    swap = 0
    print(idx_dic)
    for i, val in enumerate(arr):
        correct_val = sorted_arr[i]
        if val != correct_val:
            idx = idx_dic[correct_val]
            # swap array
            arr[idx], arr[i] = arr[i], arr[idx]
            # swap dic
            idx_dic[val] = idx
            idx_dic[correct_val] = i
            swap += 1
            print(idx_dic)

    return swap


if __name__ == '__main__':
    print(minimumSwaps([2, 1, 5, 3, 4]))
    # nums = list(range(1, 6))
    # print(nums[0])
