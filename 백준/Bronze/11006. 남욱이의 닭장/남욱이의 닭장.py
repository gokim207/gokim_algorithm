for i in range(int(input())):
    x,y = map(int,input().split())
    good = x//2
    bad = x%2
    
    if good + bad != y:
        while True:
            good -= 1
            bad += 2
            if good + bad == y:
                break
    
    print(bad, good)