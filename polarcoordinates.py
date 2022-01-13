# A single line containing the complex number z. Convert it to polar coordinates.

import cmath

if __name__ == "__main__":
    z = complex(input("Enter a complex equation: "))
    polar = cmath.polar(z)
    r = polar[0]
    phi = polar[1]
    print(r)
    print(phi)