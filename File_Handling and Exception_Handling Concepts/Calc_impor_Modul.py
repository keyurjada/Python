import Calc_modul

print(Calc_modul.add(5, 3))

from Calc_modul import sub
print(sub(10, 4))

from Calc_modul import *
print(mul(2, 6))