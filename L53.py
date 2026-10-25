# Exception Handling

print("Resource Opened Successfully")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result is:", result)

except ZeroDivisionError as zde:
    print("An error occurred: Division by zero is not allowed.", zde)
except ValueError as ve:
    print("An error occurred: Invalid input. Please enter numeric values only.", ve)
except Exception as e:
    print("An unexpected error occurred: ", e)

finally:
    print("Resource closed.")
    
print("End of execution")