#!/usr/bin/env python3

result = []

if __name__ == "__main__":
  with open("flag.txt", 'r') as file:
    idx = 0
    for line in file.readlines():
      if (idx % 7 == 0):
        result.append(line.replace("a", "o"))
      else:
        result.append(line)
      idx += 1

  with open("flag.txt", 'w') as file:
    for string in result:
      file.write(f"{string}")
    file.flush()