str1="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tango=[""]
mozisu=[]
cnt1=0
cnt2=0
for i in range(len(str1)):
  if str1[i]=="," or str1[i]==".":
    continue
  elif str1[i]==" ":
    cnt1+=1
    tango.append("")
    mozisu.append(cnt2)
    cnt2=0
    continue
  else:
    tango[cnt1]+=str1[i]
    cnt2+=1
print(tango)
print(mozisu)



