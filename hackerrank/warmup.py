def sockMerchant(n, ar):
    socks = []
    count = 0
    for a in ar:
        if a not in socks:
            socks.append(a)
    for s in socks:
        count += ar.count(s) // 2
    return count


if __name__ == '__main__':
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
