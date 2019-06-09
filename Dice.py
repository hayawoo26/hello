import sys
import random

print('ダイスだよ！！')

args = sys.argv

print(args)

print(args[1])

men = args[1]

print('ダイス' , men)

# deme = random.randint(1, int(men))
# print(f'{men}面ダイスの結果は{deme}だよ！')


dice_hairetu = men.split('d')


print(random.randint(1, int(dice_hairetu[1])))

renzoku = int(dice_hairetu[0])

kekka_hairetu = []
print(kekka_hairetu)
for i in range(renzoku):
    print('iは', i)
    n = (random.randint(1, int(dice_hairetu[1])))
    kekka_hairetu.append(n)


print('for 終わり')
print(kekka_hairetu)
