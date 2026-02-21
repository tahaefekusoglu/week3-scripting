from ff import *
counter = 0
for i in ertug:
    print(type(i))
    lasti=str(i)
    print(type(lasti))
    try:
        x=i['status']
        print(type(x))
        if x.starswith('big'):
            counter+=1
            with open("efe.txt", "a" , endcoding = 'utf-8') as f:
                f.write(lasti+'\n')
            print(i)
        else:
            pass


        counter += 1
    except:
        pass
        print(counter)

