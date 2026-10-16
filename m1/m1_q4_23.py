ip_address = '192.168.3.1'
ip_spl = ip_address.split('.') #["192", "168", "3", "1"]これは文字列
bin_exp = ''
for num in ip_spl:
    bin_exp += bin(int(num))[2:] + '.'
print(bin_exp[:-1])
print(type(bin_exp))
"""メモ
splitメゾットは引数で指定された文字で分割しリストを作る
bin()関数は引数の整数を2進数の文字列に変換する
int()関数は引数の文字列を整数に変換する
スライスについて[2:]は文字列の2文字目以降を取得する
スライスについて[:-1]は文字列の最後の1文字を除いた文字列を取得する

"""