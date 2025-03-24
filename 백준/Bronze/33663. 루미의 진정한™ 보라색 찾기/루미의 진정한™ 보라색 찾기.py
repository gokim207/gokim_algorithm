h0,h1 = map(int,input().split())
s0,s1 = map(int,input().split())
u0,u1 = map(int,input().split())
r,g,b = map(int,input().split())

v = max(r,g,b)
m = min(r,g,b)

s = 255 * ((v-m)/v)

if v == r:
    h = (60*(g-b))/(v-m)
elif v == g:
    h = 120 + ((60*(b-r))/(v-m))
else:
    h = 240 + ((60*(r-g))/(v-m))

if h < 0:
    h += 360
if (h >= h0 and h <= h1) and (s >= s0 and s <= s1) and (v >= u0 and v <= u1):
    print('Lumi will like it.')
    exit()
print('Lumi will not like it.')