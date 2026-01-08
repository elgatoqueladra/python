dic = {'Euro':'€','Dollar':'$','Yen':'¥'}
divisa=input("dime la divisa")
if divisa in dic:
    print (dic[divisa])
else:
    print("no existe")