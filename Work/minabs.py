import sys
s=[42, -5, 12, 21, 5, 24]
m=9e9
for n in s:
 if abs(n)<m:m=n
 elif abs(m)==n and n>0:m=n 
print(s,m, file=sys.stderr)
print(m)
