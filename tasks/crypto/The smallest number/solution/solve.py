# брутфорс
if __name__ == '__main__':
    x = 0
    while True:
        if x & 87 == 17 and x | 139 == 187 and (x & 240) | 85 == 245:
            print(x)
            break
        x += 1
