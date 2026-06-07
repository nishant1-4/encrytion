import random

session_key = random.choice([i for i in range(20,51)])
base64_list = [chr(i) for i in range(65,91)]
base64_list.extend([chr(i) for i in range(97,123)]+[str(i) for i in range(0,10)]+['+','/'])
base64_dict = {char:index for index,char in enumerate(base64_list)}

def bin_num(decimal:list,min_length=8):
  pointer = 0
  arr = []
  for i in range(len(decimal)):
    if decimal[i] == 0:
      arr.append(0)
    else:
      while decimal[i]>0:
        arr.append(decimal[i]%2)
        decimal[i]//=2
    if len(arr)<min_length*(i+1):
      pad = min_length*(i+1)-len(arr)
      arr.extend([0]*pad)
    j = len(arr)-1
    while pointer<j:
      arr[pointer],arr[j] = arr[j],arr[pointer]
      pointer+=1
      j-=1
    pointer+=(min_length//2)
  return arr

def decimal(binary:list):
  i = 0
  j = len(binary)-1
  while i<j:
    binary[i],binary[j] = binary[j],binary[i]
    i+=1
    j-=1
  power = 0
  num = 0 
  for i in binary:
    num+= i*pow(2,power)
    power+=1
  return num