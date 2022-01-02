import math
def f(n):
  if n == 0:return 1
  return math.prod([i for i in range(1,n+1)])

def choose(n,r):
  #print(n,r,f(n),f(r), f(r) * f(n - r), f(n) / (f(r) * f(n - r)))
  return f(n) / (f(r) * f(n - r))

def main():
  lst = []
  for n in range(1,101):
    for r in range(1,n+1):
      c = choose(n,r)
      #print(c)
      if c > 10 ** 6:lst.append(c)
  print(len(lst))