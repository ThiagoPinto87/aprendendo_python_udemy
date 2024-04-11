a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={}, c={:.2f}'
formato = string.format(a, b, c)

print(formato)


d = 'A'
e = 'B'
f = 1.1
string_1 = 'a={1} b={0}, b={0}, c={nome2:.2f}'
formato_1 = string_1.format(d, e, nome2=f)

print(formato_1)