a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1])
all_num = [a, b, dm[0], dm[1], p]
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)
print(f'{min_all}, {max_all}, {sum_all}')


"""ノート欄
divmod()関数:商と余りをタプルで返す関数
pow()関数:べき乗(xのy乗)を返す関数
min()関数:リスト内の最小値を返す関数
max()関数:リスト内の最大値を返す関数
sum()関数:リスト内の要素の合計を返す関数

"""