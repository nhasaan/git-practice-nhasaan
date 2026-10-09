from datetime import date
from utils import add, subtract, multiply

print("Md. Nazmul Hasan Sarkar")
print(date.today())

try:
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("Invalid call:", add("x", 3))
except TypeError as e:
    print("Error:", e)
