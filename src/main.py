from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Safi")
print("Today's Date:", date.today())

try:
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
except (TypeError, ValueError) as error:
    print("Error:", error)