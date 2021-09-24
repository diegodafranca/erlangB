#Erlang B Calculator
from math import ceil

def probabilidade(p,c):
  if(p == 0):
    return 0.0
  s= 0.0
  for i in range(1,c):
    s = (1.0 + s)*(i/p)
  pc = 1.0/(1.0 + s)
  return pc

def Canais(p,prob):
  l,r = 0,ceil(p)
  fR = probabilidade(p,r)
  while(fR > prob):
    l = r
    r = r + 32
    fR = probabilidade(p,r)
  while(r-l)>1:
    mid = ceil((l+r)/2)
    fMid = probabilidade(p,mid)
    if fMid > prob:
      l = mid
    else:
      r = mid
  return r - 1


while(True):
  Ch = int(input("Insira número de chamadas no HMM:"))
  TMA = float(input("Insira TMA em segundos: "))
  TMA = TMA/3600
  #Canais = int(input("Insira Número de Canais: "))
  p = Ch*TMA*1.01
  prob = 0.01
  #prob precisa estar entre 0 e 1
  print("Para a volumetria de",p,"erlangs serão necessários",Canais(p,prob), "canais para atender essa volumetria")
  break

  

