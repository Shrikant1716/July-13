try:
    odd=[]
    even=[]
    for i in range(1,21):
        if i%2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
        else:
            pass
    print(odd)
    print(even)
except:
    print('Wrong List')

