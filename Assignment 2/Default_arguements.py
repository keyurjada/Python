def simi(p, t, r=5):
    si = (p * t * r) / 100
    return si

p = float(input("Enter Principal: "))
t = float(input("Enter Time: "))

print("Simple Interest =", simi(p, t))