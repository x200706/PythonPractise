if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set_for_sort = set(arr)
    print(sorted(set_for_sort, reverse=True)[1])
