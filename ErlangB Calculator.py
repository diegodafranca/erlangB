#Erlang B Calculator
from math import ceil

def probability(p,c):
  #this function returns the probability of not answering a call given the BHC Volume in Erlangs and c the number of phone lines 
  if(p == 0):
    return 0.0
  s= 0.0
  for i in range(1,c):
    s = (1.0 + s)*(i/p)
  pc = 1.0/(1.0 + s)
  return pc

def lines(p,prob):
  #this function returns the number of lines given certain values of p and prob, where p is the BHC Volume in Erlangs and prob the probability of not answering a call 
  l,r = 0,ceil(p)
  fR = probability(p,r)
  while(fR > prob):
    l = r
    r = r + 32
    fR = probability(p,r)
  while(r-l)>1:
    mid = ceil((l+r)/2)
    fMid = probability(p,mid)
    if fMid > prob:
      l = mid
    else:
      r = mid
  return r - 1

Ch = int(input("Insert BHC:"))
AvgCallDuration = float(input("Insert call duration in seconds: "))
AvgCallDuration = AvgCallDuration/3600 #convert from seconds to hour
p = Ch*AvgCallDuration
prob = 0.01
#prob is the probability of a call being rejected given the BHC and average call duration. It needs to be > 0 and <=1.
print("For the volume of",p,"erlangs there will be a need for",lines(p,prob), "lines in order to attend the grade of service of",int(prob*100), "% blocking probability.")
