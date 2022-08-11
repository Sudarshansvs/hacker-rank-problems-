
def print_rangoli(size):
    import string
    alphabets = string.ascii_lowercase
    l=[]
    for i in range(size):
        s='-'.join(alphabets[i:size])
        l.append(s[::-1]+s[1:])
        
        
    for i in l[::-1]:
        print(i.center(4*size-3,'-'))

        
    for i in l[1:] :
        print(i.center(4*size-3,'-'))

    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
