#ひらがな1文字を受け取り、hiragana_hyou内の位置を（横、縦）のタプルで返す関数
#（横、縦）=　（外側リストのインデックス,内側リストのインデックス）例）'い'　ー＞　（0,１）
#見つからなかったらNoneを返す
def searxh_kana_idx(kana):
    idx_1 = 0
    for gyou in hiragana_hyou:
        idx_2 = 0
        for ka in gyou:
            if ka == kana:
                return (idx_1, idx_2)
            else:
                idx_2 += 1
        idx_1 += 1
    return None

hiragana_hyou = [['あ', 'い', 'う', 'え', 'お'], 
                 ['か', 'き', 'く', 'け', 'こ'],
                 ['さ', 'し', 'す', 'せ', 'そ'],     
                 ['た', 'ち', 'つ', 'て', 'と'],
                 ['な', 'に', 'ぬ', 'ね', 'の'], 
                 ['は', 'ひ', 'ふ', 'へ', 'ほ'],
                 ['ま', 'み', 'む', 'め', 'も'],
                 ['や', '゛', 'ゆ', '゜', 'よ'],
                 ['ら', 'り', 'る', 'れ', 'ろ'], 
                 ['わ', 'っ', 'を', 'ー', 'ん']]

hirabun = input('ひらがなの文を入力してください：')
codes = ''
for kana in hirabun:
    idxs = searxh_kana_idx(kana)
    codes += '？' if idxs is None else f'{idxs[0]}{idxs[1]}'
print(codes)

ango = input('暗号を入力してください：')
kanas = ''
if len(ango) % 2 == 0:
    for i in range(len(ango) // 2):
        index_1 = int(ango[2 * i])
        index_2 = int(ango[2 * i + 1])
        kanas += '？'if index_2 > 4 else hiragana_hyou[index_1][index_2]
    print(kanas)
else:
    print('暗号の文字数は偶数でなければなりません')

'''補足欄（必要に応じてノートしましょう）
・条件式（三項演算子）について
codes += '？' if idxs is None else f'{idxs[0]}{idxs[1]}'
この処理は、以下のif/else文と同じ処理です。関連して抑えておきましょう。
if idxs is None: # idxsがNoneなら
    codes += '？' # '？'を連結する
else:
    codes += f'{idxs[0]}{idxs[1]}' # idxs[0]とidxs[1]を文字列にして、続けてcodesに連結する

kanas += '？' if index_2 > 4 else hiragana_hyou[index_1][index_2]
について、
index_2は内側のリストのインデックスで、有効なのは0から4まで。
index_2が5以上だと範囲外になりエラーとなるので、その場合は'？'を連結する
このときelse側のhiragana_hyou[index_1][index_2]は表示されないのでエラーにならない。
(index_1は1桁の数字なので0〜9で、リストの行数10に収まる。そのため確認は不要)

'''