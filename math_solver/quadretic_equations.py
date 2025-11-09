import cmath

def quadretic():
    a =float (input ("enter a:"))
    b = float (input ("enter b:"))
    c = float (input ("enter c:"))
    d = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)

    return root1,",", root2
print(quadretic())

