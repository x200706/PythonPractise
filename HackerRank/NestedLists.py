if __name__ == '__main__':
    arr = []  # 宣告一個空的清單儲存名字跟分數
    score_arr = []  # 這是排序所有出現過分數用的清單
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])  # 這邊具體而言就製作好了像[['mimi', 50.0], ['lala', 55.0]]這樣的嵌套清單
        score_arr.append(score)

    score_set = set(score_arr)
    second_score = sorted(score_set)[1]  # 這是上題Find the Runner-Up Score!找到第二高的分數的做法

    # 現在要找出那些人是第二高的人並裝起來
    name_arr = []
    for i in range(len(arr)):
        if arr[i][1] == second_score:
            name_arr.append(arr[i][0])
    name_arr.sort()

    for i in range(len(name_arr)):
        print(name_arr[i])
