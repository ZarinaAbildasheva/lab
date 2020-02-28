n = int(input())
 
q="+___ "
w="|a / "
e="|__\ "
r="|    "

print(n*q)
res = ""
for i in range(n):
    res=res+"|{} / ".format(i+1)
print(res)    
print(n*e)
print(n*r)

    