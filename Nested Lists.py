if __name__ == '__main__':
    dic={}
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in s:
            s.append(score)
    minimum=min(s)
    s.remove(minimum)
    m=min(s)
    
    dic[m].sort()
    for i in dic[m]:
        
        print(i)
    
