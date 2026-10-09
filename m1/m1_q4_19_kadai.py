a = [1, 2, 3, 4]
id_a = id(a) 
b = a.copy() 
id_b = id(b) 
if id_a == id_b:
    result ='A'
elif id(a) ==id(b):
    result ='B'
elif id_a == id(a):
    result ='C'
else:
    result ='D'
print(result) 

print(id(a))
print(id_a)
print(type(id_a))


"""課題
実際に変数aに対してid()関数を使った結果と、変数id_aの内容を出力し、
同じ値になっていることを確認してみてください。
また、変数id_aがどのtypeかを、type()関数を使って調べてみてください。

【出力例】※idの値は環境によって変わります。同じ値になっていることだけ確認してください。
C
4300900736
4300900736
<class 'int'>
"""