def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def getword(text, cur):
    while cur < len(text) and text[cur] != ' ':
        cur += 1
    return cur


def stegget(text):
    k = 8
    cur = 0
    ans = ""
    while (True):
        t = 0
        for i in range(k):
            cur = getword(text, cur)
            if cur > len(text):
                break
            if text[cur] == ' ' and text[cur + 1] == ' ':
                t += 1 << i
                cur += 1
            cur += 1
        if t == 0:
            break
        ans += chr(t)
    return ans


if __name__ == "__main__":
    res = read_file("stego.txt")
    print(stegget(res))
