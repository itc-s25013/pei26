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
print(list_s)


"""計算欄
1回目のループ後：num=6, list_s=[2], s=2
2回目のループ後：num=3, list_s=[2], s=2
3回目のループ後：num=3, list_s=[2, 3], s=3
4回目のループ後：num=1, list_s=[2, 3], s=3
ループ終了  
"""