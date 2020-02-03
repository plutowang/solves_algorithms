def checkMagazine(magazine: list, note: list):
    # Hash Tables: Ransom Note
    # for word in note:
    #     if word not in magazine:
    #         print('No')
    #         return
    #     magazine.remove(word)
    # print('Yes')
    from collections import Counter
    if Counter(note) - Counter(magazine) == {}:
        print('Yes')
    else:
        print('No')


def twoStrings(s1, s2):
    # Two Strings
    return 'YES' if set(s1) & set(s2) else 'NO'


def sherlockAndAnagrams(s):
    # Sherlock and Anagrams
    n = 0
    sub_dict = {}
    length = len(s)
    for i in range(length):
        for j in range(n-i):
            sub = ''.join(sorted(s[j:j+i+1]))
            try:
                sub_dict[sub] += 1
            except:
                sub_dict[sub] = 1
    for string in sub_dict:
        n += sub_dict[string]*(sub_dict[i]-1) // 2
    return int(n)


if __name__ == '__main__':
    import ast
    import os
    with open(os.path.basename(__file__)) as f:
        TREE = ast.parse(f.read())
        COUNT = sum(isinstance(exp, ast.FunctionDef) for exp in TREE.body)
        print('\nThere are {} functions in {}\n{}'.format(
            COUNT, os.path.basename(__file__), '='*70))

    # print(twoStrings("hi", 'world'))
    print(sherlockAndAnagrams("abba"))
