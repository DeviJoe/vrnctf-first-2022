import random


def set_seed(seed):
    if seed > 2 << 16:
        raise ArithmeticError
    random.seed(seed)


def encrypt(text):
    ans = ""
    for i in range(len(text)):
        d = random.randint(0, 255)
        ch = ord(text[i]) ^ d
        ans += chr(ch)
    return ans


if __name__ == '__main__':
    ans = "ÎÈ'óÇ½ºQù½ûÖô»ZÓW^[qK½ýy"
    for i in range((2 << 16) + 1):
        set_seed(i)
        res = encrypt(ans)
        if res.startswith('vrnctf'):
            print(res)
            print(i)