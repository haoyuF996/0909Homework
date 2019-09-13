EDF = open("EmailDetails.txt",'r')
NEDF = open("NewEmailDetails.txt",'w')
ED = EDF.readline()
while ED!='':
    NEDF.write('00'+ED)
    ED = EDF.readline()
EDF.close()
NEDF.close()


print('Ounces  Grams')
for Ounces in range(1,31):
    Grams = round(Ounces*28.35)
    print(Ounces+' '+Grams)

IDL = list(input("UserID"))
Valid = False
if len(IDL)==4:
    UC = 0
    for i in IDL:
        if ord(i)<91:
            UC+=1
    if UC==3:
        Valid = True
if Valid:
    print('UserID is valid')
else:
    print('UserID is not valid')

Tally = [0 for i in range(5)]

TL = TitleList = ['Reading books','Play computer games','Sport','Programing','Watching TV']

Choice = input('Choice')
while Choice!=0:
    Tally[Choice]+=1

Data = open('Data.txt','w')

for i in range(5):
    print(TL[i])
    print(Tally[i])
    Data.write(Tally[i])

Data.close()

Data = open('Data.txt','r')

Tally = [0 for i in range(5)]
for i in range(5):
    Tally[i] = Data.readline()
