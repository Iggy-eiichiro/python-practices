
import logging

logging.basicConfig(
    filename=r"c:\Users\bro\OneDrive\デスクトップ\python Rikai\app log", level = logging.ERROR
)
# it means logging.ERROR to record logs at a level above
try:
    A = int(input("Please enter the denominator number:"))
    B = int(input("Please enter the numerator number:"))
    result = A/B
    print(result)

except ZeroDivisionError:# it runs if a number divided by 0
    logging.exception("Division by zero occured")# log the details current exception(errors)
    print("Saved")