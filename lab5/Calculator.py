def main():
    n = int(input())
    ans = 0
    d = len(str(n))
    for i in range(1, d + 1):
        l = 10**(i - 1)
        r = min(n, 10**i - 1)
        if l > n:
            break
        ans += (r - l + 1) * i
    print(ans + n)
main()