while True:
    try:
        y = input().split()
        order = set()
        for i in y:
            order.add(int(i))
        print(len(order))
    except:
        break