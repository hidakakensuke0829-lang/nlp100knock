str1="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
tango=[""]
cnt1=0
genso={}
for i in range(len(str1)):
  if str1[i]=="," or str1[i]==".":
    continue
  elif str1[i]==" ":
    cnt1+=1
    tango.append("")
    continue
  else:
    tango[cnt1]+=str1[i]
print(tango)

for i in range(len(tango)):
  if i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18:
    genso[tango[i][0]] = i + 1
  else:
    genso[tango[i][0] + tango[i][1]] = i + 1

print(genso)