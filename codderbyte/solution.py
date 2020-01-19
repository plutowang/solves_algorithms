def LetterChanges(str):
    """Have the function LetterChanges(str) take the str
    parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the
    alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel
    in this new string (a, e, i, o, u) and finally return this modified string.

    """
    # code goes here
    vowels = ['a', 'i', 'o', 'e', 'u']
    result = ''
    for c in str:
        if c.isalpha():
            if c == 'z' or c == 'Z':
                c = 'A'
            else:
                c = chr(ord(c) + 1)
            if c in vowels:
                c = c.upper()
        result += c

    return result


def FirstReverse(str):
    # # opt1:
    # return str[::-1]
    # opt2:
    lst = list(str)
    lst.reverse()
    return ''.join(lst)


def FirstFactorial(num):

    # code goes here
    if num <= 1:
        return 1
    else:
        return num * (FirstFactorial(num - 1))

    return num


def LongestWord(sen):

    # code goes here
    word = ''
    for s in sen:
        if s.isalnum() or s.isalpha():
            word += s
        elif s.isspace():
            word += ' '

    return max(word.split(), key=len)


def SimpleAdding(num):
    """Have the function SimpleAdding(num) add up all the
    numbers from 1 to num. For example: if the input is 4
    then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    For the test cases, the parameter num will be any number from 1 to 1000.
    """

    # code goes here
    return sum([x for x in range(num+1)])


def TimeConvert(num):
    """Have the function TimeConvert(num) take the num parameter
    being passed and return the number of hours and minutes the
    parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    # code goes here
    m = num % 60
    h = (num - m) / 60
    return '{}:{}'.format(int(h), int(m))


def AlphabetSoup(str):

    # code goes here
    list_str = list(str)
    list_str.sort()
    return ''.join(list_str)


def CorrectPath(str):
    """??Have the function CorrectPath(str) read the str parameter
    being passed, which will represent the movements made in a 5x5
    grid of cells starting from the top left position. The characters
    in the input string will be entirely composed of: r, l, u, d, ?.
    Each of the characters stand for the direction to take within the grid,
    for example: r = right, l = left, u = up, d = down. Your goal is to
    determine what characters the question marks should be in order
    for a path to be created to go from the top left of the grid all
    the way to the bottom right without touching previously travelled
    on cells in the grid.

    For example: if str is "r?d?drdd" then your program should output
    the final correct string that will allow a path to be formed from the
    top left of a 5x5 grid to the bottom right. For this input, your program
    should therefore return the string rrdrdrdd. There will only ever be one
    correct path and there will always be at least one question mark within
    the input string.
    """
    # code goes here
    grid = []
    x = 0
    y = 4
    i = 0
    for move in str:
        if move == '?':
            for m in 'lurd':
                path = CorrectPath(str.replace('?', m, 1))
                i += 1
                if path:
                    return path
        else:
            if move == 'r':
                x += 1
            elif move == 'l':
                x -= 1
            elif move == 'u':
                y += 1
            elif move == 'd':
                y -= 1
            if (x, y) in grid:
                return
            grid.append((x, y))

            if x < 0 or y < 0 or x > 4 or y > 4:
                return

            if x == 4 and y == 0:
                return str


def ScaleBalancing(strArr):
    """Have the function ScaleBalancing(strArr) read
    strArr which will contain two elements, the first being
    the two positive integer weights on a balance scale (left and right sides)
    and the second element being a list of available weights
    as positive integers.
    Your goal is to determine if you can balance the scale by using the least
    amount of weights from the list, but using at most only 2 weights.
    For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means
    there is a balance scale with a weight of 5 on the left side and 9 on
    the right side.
    It is in fact possible to balance this scale by adding a 6 to the left
    side from the list of weights and adding a 2 to the right side.
    Both scales will now equal 11 and they are perfectly balanced.
    Your program should return a comma separated string of the weights
    that were used from the list in ascending order, so for this example
    your program should return the string 2,6

    There will only ever be one unique solution and the list of available
    weights will not be empty. It is also possible to add two weights to only
    one side of the scale to balance it. If it is not possible to balance the
    scale then your program should return the string not possible.
    """
    # code goes here
    def add_two(ws, key):
        for i, _ in enumerate(ws):
            if key + ws[i] in ws[i+1::]:
                return "{},{}".format(ws[i], key + ws[i])
            if key - ws[i] in ws[i+1::]:
                return "{},{}".format(ws[i], key - ws[i])

    target = abs(eval(strArr[0])[0] - eval(strArr[0])[1])
    ws = eval(strArr[1])
    if target in ws:
        return str(target)

    bal = add_two(ws, target)
    if bal:
        return bal
    return "not possible"


def VowelSquare(strArr):
    """Have the function VowelSquare(strArr) take the strArr parameter being
    passed which will be a 2D matrix of some arbitrary size filled with
    letters from the alphabet, and determine if a 2x2 square composed entirely
    of vowels exists in the matrix. For example: strArr is
    ["abcd", "eikr", "oufj"]
    then this matrix looks like the following:

    a b c d
    e i k r
    o u f j

    Within this matrix there is a 2x2 square of vowels starting in the second
    row and first column, namely, ei, ou. If a 2x2 square of vowels is found
    your program should return the top-left position (row-column) of
    the square, so for this example your program should return 1-0.
    If no 2x2 square of vowels exists, then return the string not found.
    If there are multiple squares of vowels, return the one that
    is at the most top-left position in the whole matrix. The input matrix will
    at least be of size 2x2.
    """
    # code goes here
    vowels = 'aeiou'
    for i in range(len(strArr) - 1):
        for j in range(len(strArr[0]) - 1):
            if strArr[i][j] in vowels \
                    and strArr[i][j+1] in vowels \
                    and strArr[i+1][j] in vowels \
                    and strArr[i+1][j+1] in vowels:
                return str(i)+'-'+str(j)
    return 'not found'


def ClosestEnemyII(strArr):
    """Have the function ClosestEnemyII(strArr) read the matrix of numbers
    stored in strArr which will be a 2D matrix that contains only the integers
    1, 0, or 2. Then from the position in the matrix where a 1 is,
    return the number of spaces either left, right, down, or up you
    must move to reach an enemy which is represented by a 2.
    You are able to wrap around one side of the matrix to the other as well.
    For example: if strArr is ["0000", "1000", "0002", "0002"]
    then this looks like the following:

    0 0 0 0
    1 0 0 0
    0 0 0 2
    0 0 0 2

    For this input your program should return 2 because the closest enemy (2)
    is 2 spaces away from the 1 by moving left to wrap to the other side
    and then moving down once. The array will contain any number of 0's
    and 2's, but only a single 1. It may not contain any 2's at all as well,
    where in that case your program should return a 0.
    """
    # code goes here
    enemies = []
    moves = []
    width = len(strArr)
    hight = len(strArr[0])
    for i, i_val in enumerate(strArr):
        for j, j_val in enumerate(i_val):
            if j_val == '1':
                px, py = (i, j)
            if j_val == '2':
                enemies.append((i, j))
    if not enemies:
        return 0
    for x, y in enemies:
        diff_x = abs(x - px)
        diff_y = abs(y - py)
        moves.append(min(diff_x, width - diff_x) + min(diff_y, hight - diff_y))
    return min(moves)


def QuestionsMarks(str):
    """Have the function QuestionsMarks(str) take the str string parameter,
    which will contain single digit numbers, letters, and question marks,
    and check if there are exactly 3 question marks between every pair of
    two numbers that add up to 10. If so, then your program should return
    the string true, otherwise it should return the string false.
    If there aren't any two numbers that add up to 10 in the string,
    then your program should return false as well.

    For example: if str is "arrb6???4xxbl5???eee5" then your program should
    return true because there are exactly 3 question marks between 6 and 4,
    and 3 question marks between 5 and 5 at the end of the string.
    """
    # code goes here
    dig_idxs = [idx for idx, _ in enumerate(str) if str[idx].isdigit()]
    has_ten = False
    if len(dig_idxs) <= 1:
        return 'false'
    for i in range(len(dig_idxs) - 1):
        d_x = dig_idxs[i]
        d_y = dig_idxs[i+1]
        if int(str[d_x]) + int(str[d_y]) == 10:
            has_ten = True
            if str[d_x:d_y:].count('?') != 3:
                return 'false'
    return 'true' if has_ten else 'false'


def FindIntersection(strArr):
    """Have the function FindIntersection(strArr) read the array of strings
    stored in strArr which will contain 2 elements: the first element will
    represent a list of comma-separated numbers sorted in ascending order,
    the second element will represent a second list of comma-separated numbers
    (also sorted). Your goal is to return a comma-separated string containing
    the numbers that occur in elements of strArr in sorted order.
    If there is no intersection, return the string false.

    For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    the output should return "1,4,13" because those numbers appear
    in both strings. The array given will not be empty,
    and each string inside the array will be of numbers sorted in ascending
    order and may contain negative numbers.
    """
    # code goes here
    i_nums = [int(i_nums) for i_nums in strArr[0].split(', ')]
    j_nums = [int(j_nums) for j_nums in strArr[1].split(', ')]
    i = 0
    j = 0
    common = []
    while(i < len(i_nums) and j < len(j_nums)):
        if i_nums[i] == j_nums[j]:
            common.append(str(i_nums[i]))
            i += 1
            j += 1
        elif i_nums[i] < j_nums[j]:
            i += 1
        else:
            j += 1
    return ','.join(common) if len(common) > 0 else 'false'


def EquivalentKeypresses(strArr):
    """Have the function EquivalentKeypresses(strArr) read the array of
    strings stored in strArr which will contain 2 strings representing
    two comma separated lists of keypresses. Your goal is to return the
    string true if the keypresses produce the same printable string and
    the string false if they do not. A keypress can be either a printable
    character or a backspace represented by -B. You can produce a
    printable string from such a string of keypresses by having backspaces
    erase one preceding character.

    For example: if strArr contains ["a,b,c,d", "a,b,c,c,-B,d"]
    the output should return true because those keypresses produce
    the same printable string. The array given will not be empty.
    The keypresses will only contain letters from the alphabet and backspaces.
    """
    # code goes here
    def backspace(ls: list):
        new = []
        for i, _ in enumerate(ls):
            if '-B' == ls[i]:
                if i > 0:
                    new = new[0:len(new) - 1]
                else:
                    continue
            else:
                new.append(ls[i])
        return new

    i_strs = [x for x in strArr[0].split(',') if x != '']
    j_strs = [y for y in strArr[1].split(',') if y != '']
    if '-B' in i_strs:
        i_strs = backspace(i_strs)
    if '-B' in j_strs:
        j_strs = backspace(j_strs)
    return 'true' if j_strs == i_strs else 'false'


def KaprekarsConstant(num):
    """Have the function KaprekarsConstant(num) take the num parameter
    being passed which will be a 4-digit number with at least two distinct
    digits. Your program should perform the following routine on the
    number: Arrange the digits in descending order and in ascending
    order (adding zeroes to fit it to a 4-digit number), and subtract
    the smaller number from the bigger number. Then repeat the previous
    step. Performing this routine will always cause you to reach a fixed
    number: 6174. Then performing the routine on 6174 will always give you
    6174 (7641 - 1467 = 6174). Your program should return the number of times
    this routine must be performed until 6174 is reached.
    For example: if num is 3524 your program should return 3 because of
    the following steps:
    (1) 5432 - 2345 = 3087,
    (2) 8730 - 0378 = 8352,
    (3) 8532 - 2358 = 6174.
    """
    # code goes here

    def kaprekars_helper(num, count):
        num = [num for num in str(num)]
        while len(num) < 4:
            num.append('0')
        num.sort()
        x = int(''.join(num))
        y = int(''.join(num[::-1]))
        diff = abs(x-y)
        if diff != 6174:
            return kaprekars_helper(diff, count+1)
        return count
    return kaprekars_helper(num, 1)


# def KaprekarsConstant(num):
#     # code goes here
#     counter = 0
#     k = num
#     while k != 6174:
#         str_num = [i for i in str(k)]
#         while len(str_num) < 4:
#             str_num.append("0")
#         ascend = int("".join(sorted(str_num)))
#         descend = int("".join(sorted(str_num, reverse=True)))
#         if ascend > descend:
#             k = ascend-descend
#         else:
#             k = descend-ascend
#         counter += 1
#     return counter


def ChessboardTraveling(str):
    """Have the function ChessboardTraveling(str) read str
    which will be a string consisting of the location of
    a space on a standard 8x8 chess board with no pieces on
    the board along with another space on the chess board.
    The structure of str will be the following: "(x y)(a b)"
    where (x y) represents the position you are currently on
    with x and y ranging from 1 to 8 and (a b) represents some
    other space on the chess board with a and b also ranging
    from 1 to 8 where a > x and b > y. Your program should
    determine how many ways there are of traveling from (x y)
    on the board to (a b) moving only up and to the right.
    For example: if str is (1 1)(2 2) then your program should
    output 2 because there are only two possible ways to travel from
    space (1 1) on a chessboard to space (2 2) while making only
    moves up and to the right.
    """
    # code goes here
    import math

    def show(p, n):
        board = ''
        (px, py) = p
        (a, b) = n
        for i in reversed(range(8)):
            for j in range(8):
                if i+1 == px and j+1 == py:
                    board += 'I '
                elif i+1 == a and j+1 == b:
                    board += 'E '
                else:
                    board += '- '
                if j == 7:
                    board += '\n'
        print(board)
    px, py, a, b = [int(x) for x in str if x.isnumeric()]
    assert(a > px and b > py)
    # show((px, py), (a, b))

    num_r = a - px
    num_u = b - py

    return int(math.factorial(num_u + num_r) /
               (math.factorial(num_u)*math.factorial(num_r)))


def MaximalSquare(strArr):
    """Have the function MaximalSquare(strArr) take the strArr parameter
    being passed which will be a 2D matrix of 0 and 1's, and determine the
    area of the largest square submatrix that contains all 1's. A square
    submatrix is one of equal width and height, and your program should return
    the area of the largest submatrix that contains only 1's. For example:
    if strArr is ["10100", "10111", "11111", "10010"] then this looks like the
    following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    For the input above, you can see the bolded 1's create the largest square
    submatrix of size 2x2, so your program should return the area which is 4.
    You can assume the input will not be empty.
    """
    # code goes here
    # opt 1
    # rows = len(strArr)
    # columns = len(strArr[0]) if rows > 0 else 0

    # dp = [[0 for j in range(columns)] for i in range(rows)]
    # maxlen = 0

    # for i in range(rows):
    #     for j in range(columns):
    #         if i == 0 or j == 0:
    #             dp[i][j] = int(strArr[i][j])
    #         if i > 0 and j > 0 and int(strArr[i][j]) == 1:
    #             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    #             maxlen = max(dp[i][j], maxlen)

    # return maxlen * maxlen
    # opt 2
    rows = len(strArr)
    columns = len(strArr[0]) if rows > 0 else 0
    dp = [0 for j in range(columns)]
    maxlen = 0
    prev = 0

    for i in range(rows):
        for j in range(columns):
            temp = dp[j]
            if i > 0 and j > 0 and int(strArr[i][j]) == 1:
                dp[j] = min(dp[j], dp[j-1], prev) + 1
                maxlen = max(dp[j], maxlen)
            else:
                dp[j] = int(strArr[i][j])
            prev = temp

    return maxlen * maxlen


# keep this function call here
if __name__ == '__main__':
    print(MaximalSquare(["0111", "1101", "0111"]))
