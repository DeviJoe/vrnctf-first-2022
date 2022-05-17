import pandas

flag = 'vrnctf{so_many_different_star_namings_to_choose}'

flag_coded = 'HR 8930/HR 3982/'
flag_ar = [
    ['v', 'HR 7001'],
    ['r', 'HR 3982'],
    ['n', 'HD 68988'],
    ['c', 'HR 4915'],
    ['t', 'HAT-P-40'],
    ['f', 'HR 5944'],
    ['{', '{'],
    ['s', 'HD 100777'],
    ['o', 'HD 149026'],
    ['_', '_'],
    ['m', 'HAT-P-29'],
    ['a', 'HR 936'],
    ['n', 'WASP-15'],
    ['y', 'HR 6075'],
    ['_', '_'],
    ['d', 'HR 7924'],
    ['i', 'WASP-38'],
    ['f', 'HD 100655'],
    ['f', 'HR 8773'],
    ['e', 'HR 5409'],
    ['r', 'HR 1713'],
    ['e', 'HR 8974'],
    ['n', 'HR 5602'],
    ['t', 'HD 23079'],
    ['_', '_'],
    ['s', 'HR 1481'],
    ['t', 'HR 4033'],
    ['a', 'WASP-64'],
    ['r', 'HR 7882'],
    ['_', '_'],
    ['n', 'HR 3165'],
    ['a', 'HR 7557'],
    ['m', 'HR 7254'],
    ['i', 'HR 5506'],
    ['n', 'HR 464'],
    ['g', 'HR 4700'],
    ['s', 'HR 6378'],
    ['_', '_'],
    ['t', 'WASP-22'],
    ['o', 'HR 7235'],
    ['_', '_'],
    ['c', 'HR 2891'],
    ['h', 'HD 28678'],
    ['o', 'HD 149026'],
    ['o', 'HR 7235'],
    ['s', 'HIP 79431'],
    ['e', 'HR 5744'],
    ['}', '}']
]

f = []
for i in range(len(flag_ar)):
    f.append(flag_ar[i][1])

f_en = '/'.join(f)
print(f_en)

f_to_dec = f_en.split('/')
f_dec = ''

df = pandas.read_json('catalog_data/IAU-CSN.json')
d = df[['Name/ASCII', 'Designation']]

for word in f_to_dec:
    w = d[d.Designation == word]
    if w.empty:
        f_dec += word
    else:
        w = w.iloc[0]['Name/ASCII']
        f_dec += w[0].lower()

print(f_dec)

