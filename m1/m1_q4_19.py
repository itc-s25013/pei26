a = [1, 2, 3, 4]
id_a = id(a) #リストaのIDを取得
b = a.copy() #リストaをコピーしてbに代入
id_b = id(b) #リストbのIDを取得
if id_a == id_b: #リストaとリストbのIDが同じかどうかを判定
    result ='A'
elif id(a) ==id(b):
    result ='B'
elif id_a == id(a):
    result ='C'
else:
    result ='D'
print(result) #リストaとリストbのIDが同じかどうか


"""ノート
Pythonのid()関数は、オブジェクトを識別するための整数値(int)を返す


"""