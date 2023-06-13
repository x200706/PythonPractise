if __name__ == '__main__':
    n = int(input())
    student_marks = {}  # 這個大括號的數據結構叫做字典，可以有映射關係
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr = student_marks[query_name]
    ans = sum(arr) / len(arr)
    print('%.2f' % ans)
