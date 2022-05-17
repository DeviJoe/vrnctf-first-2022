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
    secret_seed = 00000000000
    secret_text = '*************'
    set_seed(secret_seed)
    print(encrypt(secret_text))

