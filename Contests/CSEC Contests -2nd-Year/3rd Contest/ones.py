while True:
    try:
        n = int(input())

        if n % 2 == 0 or n % 5 == 0:
            continue

        i = "1"
        while True:
            if int(i) % n == 0:
                break
            else:
                i += "1"

        print(len(i))
    except:
        break
