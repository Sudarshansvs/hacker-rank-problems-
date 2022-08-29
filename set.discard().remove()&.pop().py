n = int(input())
s = set(map(int, input().split()))
no_of_commands =int(input())

for item in range(no_of_commands):
    cmd=input().split()
    if cmd[0]=="pop":
        s.pop()
    if cmd[0]=="remove":
        s.remove(int(cmd[1]))
    if cmd[0]=="discard":
        s.discard(int(cmd[1]))
          
total=0
for item in s:
    total=total+ item
print(total)
