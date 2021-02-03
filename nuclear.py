print('Part A:') # Program to calculate and print binding energy of an atom
A = 58
Z = 28

if (A % 2) != 0:
    a5 = 0
elif (A % 2) == 0:
    a5 = 12.0
elif(Z % 2) != 0:
    a5 = -12.0
else:
    print('Invalid.')

def binding(A, Z):
    t1 = 15.8 * A
    t2 = 18.3 * A**(2/3)
    t3 = 0.714 * (Z**(2) / (A**(1/3)))
    t4 = 23.2 * ((A - 2*Z)**2 / (A) )
    t5 = a5 / (A**(1/2))
    return t1 - t2 - t3 - t4 + t5
    
print('This is the binding energy of an atom of A = 58 and Z = 28 is', binding(A, Z))

print('\n')

print('Part B:')

EpN = binding(A , Z) / A
print('This is the binding energy per nucleon is', EpN)

print('\n')

print('Part C:')
Z = input('Enter a value for Z (atomic number): ')
print('Z =', Z)

print('\n')

Bond = []
b = binding(A, Z = A)
b = binding(A, Z = 2*A)
b = binding(A, Z = 3*A)
Bond.append([b])

EpN = []
e = b / A
e = b / (2*A)
e = b / (3*A)
EpN.append([e])

print('For your input of', Z)
print('The largest binding energy is', max(Bond))
print('With a binding energy of', max(EpN), 'MeV per nucleon')
print('\n')

print('Part D:')

if (A % 2) != 0:
    a5 = 0
elif (A % 2) == 0:
    a5 = 12.0
elif(Z % 2) != 0:
    a5 = -12.0
else:
    print('Invalid.')

def binding(A, Z):
    t1 = 15.8 * A
    t2 = 18.3 * A**(2/3)
    t3 = 0.714 * (Z**(2) / (A**(1/3)))
    t4 = 23.2 * ((A - 2*Z)**2 / (A) )
    t5 = a5 / (A**(1/2))
    return t1 - t2 - t3 - t4 + t5


