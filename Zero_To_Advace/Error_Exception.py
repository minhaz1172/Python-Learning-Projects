class Solution:
    def divide(self, x, y):
        try:
            # Check if x and y are numbers
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise ValueError("Both inputs must be numbers.")
            if y == 0:  # Check for division by zero
                raise ZeroDivisionError("Cannot divide by zero.")
            result = x / y
            print("The result is:", result)
        except (ZeroDivisionError, ValueError) as e:
            print("An error occurred:", e)

        finally:
           print("The division operation has completed.")    

# Create an instance of Solution and call the method
solution = Solution()
solution.divide(0, 2)  # Correctly passes a zero for testing
solution.divide(3, 0)  # Division by zero
solution.divide(4, 2)  # Non-numeric input to trigger ValueError
