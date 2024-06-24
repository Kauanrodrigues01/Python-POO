h = int(input())
m = int(input()) 
s = int(input())
t = int(input())

total_s = (h*3600) + (m*60) + t + s

h = ((total_s // 3600) % 24)
m = ((total_s // 60) % 60)
s = ((total_s) % 60)
print(h)
print(m)
print(s)