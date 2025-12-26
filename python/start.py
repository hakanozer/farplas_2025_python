from action import Yap

# tek satırlı açıklama

print('hello python')

# değişkenler
# String değişken
name = "Ali"
surname = 'Bilmem'

# tam sayı
age = 30
number1 = 14.5
bigNumber = 2342342.34534534534

# boolean type
status = True

# tür tanımlama
print(type(name), type(age), type(number1), type(status))

count = len(name)
print('Count', count)

# tür dönüşümleri
# string to int
strNumber = "123"
intNumber = int(strNumber)
print(type(intNumber))

n1 = 12.5
n2 = 17.8
nSum = int(n1 + n2)
print('Sum:', nSum)

# int to string
varData = str(n1)
print('Var Data:', type(varData))

# String işlemleri
stData = 'Python güzel bir dildir'
print(stData.lower())
print(stData.upper())
# stData replace
replaceData = stData.replace('güzel', 'harika')
print(replaceData)
# stData split
splitData = stData.split(' ')
print(splitData)
# trim
trimData = '  ali@mail.com   '
print(trimData.strip())
# find data
findData = stData.find('güzel')
print('Find Data:', findData)

# substing
subString = stData[1:4]
print('Substring:', subString)

# replace index
if findData != -1:
    newStringData = stData.replace('güzel', '***')
    print('New String Data:', newStringData)

# listeler
users = ['Ali', 'Zehra', 'Mehmet']
# diziye eleman ekle
users.append('Ahmet')
users.append('Ayşe')
print('Users List:', users)

# elemana ulaşma
firstUser = users[0]
print('First User:', firstUser)

# loop ile listeleme
for item in users:
    print('User:', item)
    if item == 'Mehmet':
        print('Mehmet bulundu!')
        break


yasakliKullancilar = ['Zehra', 'Ayşe']
# continue kullanımı
for item in users:
    for yasakli in yasakliKullancilar:
        if item == yasakli:
            # print('Yasaklı kullanıcı:', item)
            continue
print('------------------------------')
endUser = users.copy()
for yasakli in yasakliKullancilar:
    endUser.remove(yasakli)
print('End User List:', endUser)

for user in endUser:
    print('End User:', user)

print('------------------------------')
# sözlükler - dictionaries
userDict = {
    'name': 'Ali',
    'surname': 'Bilmem',
    'age': 30,
    'email': 'ali@mail.com',
    'status': True
}
# ekleme
userDict['city'] = 'İstanbul'
newDic = {'job': 'developer', 'salary': 5000}
userDict['job'] = newDic
userDict['city'] = 'Ankara'
print('User Dictionary:', userDict)

# dic - keys
keys = userDict.keys()
print('Dictionary Keys:', keys)
# dic - values
values = userDict.values()
print('Dictionary Values:', values)

#dic - items
for key in keys:
    print('key:', key, 'value:', userDict[key])

print('-------------------')
dicArr = [userDict, userDict, userDict]
for itemDic in dicArr:
    dicItemKeys = itemDic.keys()
    for key in dicItemKeys:
        print('type', type(itemDic[key]))
        print('key:', key, 'value:', itemDic[key])
    print('-------------------')

stAge = '30'
# hata yönetimi - try except
try: 
    intAge = int(stAge) + 10
    print('Type of intAge:', intAge)
    numberI = 1 / 0
except Exception as e:
    if isinstance(e, ValueError):
        print('Age dönüşüm hatası - Sadece sayısal giriniz!')
    elif isinstance(e, ZeroDivisionError):
        print('Sıfıra bölme hatası!')

print('Her durumda çalışır')


yapInstance = Yap('MyYap')
twoNumberSumResult = yapInstance.twoNumberSum(12, 18)
print('Two Number Sum Result:', twoNumberSumResult)

newSum = yapInstance.twoNumberSum(100, 250)
print('New Sum Result:', newSum)


