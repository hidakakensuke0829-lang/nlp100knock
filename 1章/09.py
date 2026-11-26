import random
def mozirandom(str1):
  str1_list = list(str1)
  random.shuffle(str1_list)
  return "".join(str1_list)

str1="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
cnt1=0
tango=""
result=""
for i in range(len(str1)):
  if str1[i]==" ":
    if cnt1<=4:
      result+=tango
    else:
      result+=tango[0]+mozirandom(tango[1:len(tango)-1])+tango[len(tango)-1]
    tango=""
    result+=" "
    cnt1=0
  else:
    tango+=str1[i]
    cnt1+=1

if cnt1 <= 4:
    result += tango
else:
    result += tango[0] + mozirandom(tango[1:len(tango)-1]) + tango[len(tango)-1]

print(result)