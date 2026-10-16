num = 12
list_s = []
s = 2
while s <= num:
    if num % s == 0:
        num //= s
        if s not in list_s:
            list_s.append(s)
    else:
        s += 1
    print(num)
print(list_s)


"""課題
numの値がどのように変化するかprint関数で出力し、
最後にlist_sの内容を表示するプログラムにアレンジしてください
実行・確認できたらコードのURLをClassroomに提出しましょう


【出力例】
6
3
3
1
[2, 3]
"""