import math
from itertools import combinations
import json

prime_list = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
available_pairs = list(combinations(prime_list,2))

def register_keys():
  data = {}
  try:
    with open('used_keys.json','r') as file:
      data = json.load(file)
  except:
    print("Something went wront")
  if abs(data['pointer']) > len(available_pairs):
    return False
  keys = available_pairs[data['pointer']]
  data['pointer']-=1
  try:
    with open('used_keys.json','w') as file:
      json.dump(data,file,indent=2)
  except:
    print("Something went wrong")
  return keys

def public_key(p,q):
  e = 3
  n = p*q
  phi_n = (p-1)*(q-1)
  while True:
    if math.gcd(e,phi_n)==1:
      break
    e+=1
  return (e,n)

def private_key(p,q):
  pu_k = public_key(p,q)
  x =1
  y = 0
  e = pu_k[0]
  org_phi_n = (p-1)*(q-1)
  phi_n = org_phi_n
  while e!=0 and phi_n!=0:
    if phi_n>e:
      y = y-(x*(phi_n//e))
      phi_n= phi_n%e
    else:
      x = x-(y*(e//phi_n))
      e = e%phi_n
  return [pu_k,(y%org_phi_n if y%org_phi_n!=0 else x%org_phi_n,p*q)]

def generate_keys():
  key = register_keys()
  if not key:
    return "Sorry user we don't have any keys left"
  return private_key(key[0],key[1])
  
print(generate_keys())

