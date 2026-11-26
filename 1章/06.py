def bigram(str1):
  mozi=[]
  for i in range(len(str1)-1):
    mozi.append(str1[i]+str1[i+1])
  return mozi
str1="paraparaparadise"
str2="paragraph"
str3="se"
bigram1=bigram(str1)
bigram2=bigram(str2)
wa=[]
seki=[]
sa=[]
for i in range(len(bigram1)):
  if bigram1[i] not in wa:
    wa.append(bigram1[i])
  if bigram1[i] in bigram2:
    if bigram1[i] not in seki:
      seki.append(bigram1[i])
  if bigram1[i] not in bigram2:
    if bigram1[i] not in sa:
      sa.append(bigram1[i])

if str3 in seki:
    print(f"XとYに{str3}が含まれます")
elif str3 in bigram1:
    print(f"Xに{str3}が含まれます")
elif str3 in bigram2:
    print(f"Yに{str3}が含まれます")
else:
    print(f"XとYのどちらにも{str3}が含まれません")


print(wa)
print(seki)
print(sa)