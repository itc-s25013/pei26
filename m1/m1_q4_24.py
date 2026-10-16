animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
    else:
        total += len(animal)
print(total)


"""メモ
startswith()メソッドは文字列が指定した文字で始まるかどうかを判定する
find('b')メソッドはbが最初に見つかったインデックスを返す。見つからなければ-1を返す

"""
"""計算
animal   from_D   is_long   処理
Dog      True     False     total += len(Dog) = 3
Cat      False    False     total += len(Cat) = 3
Rabbit   False    True      total += Rabbit.find('b') = 2
Horse    False    False     total += len(Horse) = 5
Dolphin  True     True      break
total = 3 + 3 + 2 + 5 = 13

"""