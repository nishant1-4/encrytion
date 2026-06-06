import random

base64_list = [chr(i) for i in range(65,91)]
base64_list.extend([chr(i) for i in range(97,123)]+[str(i) for i in range(0,10)]+['+','/'])

def bin_num(decimal:list):
  pointer = 0
  arr = []
  for i in range(len(decimal)):
    if decimal[i] == 0:
      arr.append(0)
    else:
      while decimal[i]>0:
        arr.append(decimal[i]%2)
        decimal[i]//=2
    if len(arr)<8*(i+1):
      pad = 8*(i+1)-len(arr)
      arr.extend([0]*pad)
    j = len(arr)-1
    while pointer<j:
      arr[pointer],arr[j] = arr[j],arr[pointer]
      pointer+=1
      j-=1
    pointer+=4
  return arr

def convertobase(binary:list):
  enc_hash = ""
  i = 0
  if len(binary)>24:
    while i<24:
      enc_hash+=base64_list[decimal(binary[i:i+6])]
      i+=6
    enc_hash+=convertobase(binary[24:])
  else:
    org_length = len(binary)
    binary.extend([0]*(24-len(binary)))
    i = 0
    while i < 24:
      enc_hash+=base64_list[decimal(binary[i:i+6])]
      i+=6
    enc_hash = list(enc_hash)
    j = -1
    for i in range((24-org_length)//8):
       enc_hash[j] = '='
       j-=1
    enc_hash = ''.join(enc_hash)
  return enc_hash

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



msg = 'Do you think that is right?'
session_key = random.choice([i for i in range(20,51)])
enc_msg = []
for i in msg:
  enc_msg.append(ord(i)^session_key)
enc_hash = convertobase(bin_num(enc_msg))
print(enc_hash) 