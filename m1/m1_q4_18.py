phrase = "PythonProgramming"
list_p = [] #空のリストを作成
for p in phrase: # phrseの中の文字を一つずつ取り出す
    if p not in list_p: # もしlist_pの中にpが含まれていなければ
        list_p.append(p) #list_pにpを追加する
print(len(phrase) - len(list_p)) # 異なる文字の数を出力する

"""
.append()について調べておきましょう
    リストの末尾に要素を1つだけ追加するための関数
len()関数について調べておきましょう
    リストや文字列などのオブジェクトの長さ（要素の数）を返す関数
"""