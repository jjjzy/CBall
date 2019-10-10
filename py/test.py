import Vector
#########################################################


a = Vector.Vector3D(1, 2, 3)
b = Vector.Vector3D(4, 5, 6)

def print_a_b():
    print("a is ", a.x, a.y, a.z)
    print("b is ", b.x, b.y, b.z)

print_a_b()
print(" ")

print("assigning 3 values to a (5 6 7):")
a.assign_val(5, 6, 7)
print_a_b()

print("is a and b equal?????")
print(a == b)
print(" ")

print("now letting a equal to b:")
a.assign_vec(b)
print_a_b()
print(" ")

print("is a and b equal?")
print(a == b)
print(" ")

print("a += b")
a += b
print_a_b()
print(" ")

print("a -= b")
a -= b
print_a_b()
print(" ")

print("a *= 2")
a *= 2
print_a_b()
print(" ")

print("a /= 2")
a /= 2
print_a_b()
print(" ")

print("c = -a")
c = -a
print(c.print_vec())
print(" ")

print("now give a a smaller value for easy testing")
a.assign_val(1, 2, 3)
print_a_b()
print(" ")

print("a ^= b")
a ^= b
print_a_b()
print(" ")

print("now give a a smaller value for easy testing")
a.assign_val(1, 2, 3)
print_a_b()
print(" ")

print("a %= b")
a %= b
print_a_b()
print(" ")

print("now give a a smaller value for easy testing")
a.assign_val(1, 2, 3)
print_a_b()
print(" ")

print("c = a + b")
c = a + b
c.print_vec()
print(" ")

print("c = a - b")
c = a - b
c.print_vec()
print(" ")

print("c = a * 2")
c = a * 2
c.print_vec()
print(" ")

print("c = a / 2")
c = a / 2
c.print_vec()
print(" ")

print("c = a ^ b")
c = a ^ b
c.print_vec()
print(" ")

print("c = a % b")
c = a % b
c.print_vec()
print(" ")

print("c = a * b")
c = a * b
print(c)
print(" ")

print("normsqr(a)")
print(a.normsqr())
print(" ")

print("norm(a)")
print(a.norm())
print(" ")

print("a.selfNormalize()")
a.selfNormalize()
a.print_vec()
print(" ")

print("now give a a smaller value for easy testing")
a.assign_val(1, 2, 3)
print_a_b()
print(" ")

print("c = a.normalize()")
c = a.normalize()
c.print_vec()
print(" ")

print("c = a.comp(b)")
c = a.comp(b)
print(c)
print(" ")

print("a.self_scale(5)")
a.self_scale(5)
a.print_vec()
print(" ")

print("now give a a smaller value for easy testing")
a.assign_val(1, 2, 3)
print_a_b()
print(" ")

print("c = a.scale(5)")
c = a.scale(5)
c.print_vec()
print(" ")

print("c = a.rotateXd(180)")
c = a.rotateXd(180)
c.print_vec()
print(" ")

print("c = a.rotateYd(180)")
c = a.rotateYd(180)
c.print_vec()
print(" ")

print("c = a.rotateZd(180)")
c = a.rotateZd(180)
c.print_vec()
print(" ")