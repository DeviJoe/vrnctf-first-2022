import base64


# Под киберповаром имелся ввиду сайт:
# https://gchq.github.io/CyberChef/
if __name__ == '__main__':
  cipher_text = "dnJuY3Rme2I0NTNfNjRfMTVfbjA3XzdoM19iMTY2MzU3fQ=="
  print(base64.b64decode(cipher_text).decode())