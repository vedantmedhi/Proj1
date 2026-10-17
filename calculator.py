
import logging

# Configure logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculator():
    print("\n===== ADVANCED PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == "7":
                logging.info("Calculator closed by user")
                print("Calculator closed. Bye bhai!")
                break

            if choice not in {"1", "2", "3", "4", "5", "6"}:
                print("Invalid choice! Select 1 to 7.")
                logging.warning("Invalid menu choice: %s", choice)
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operation = "Addition"

            elif choice == "2":
                result = num1 - num2
                operation = "Subtraction"

            elif choice == "3":
                result = num1 * num2
                operation = "Multiplication"

            elif choice == "4":
                if num2 == 0:
                    raise ZeroDivisionError(
                        "Cannot divide by zero!"
                    )
                result = num1 / num2
                operation = "Division"

            elif choice == "5":
                result = num1 ** num2
                operation = "Power"

            elif choice == "6":
                if num2 == 0:
                    raise ZeroDivisionError(
                        "Modulus by zero is not allowed!"
                    )
                result = num1 % num2
                operation = "Modulus"

            print(f"\nResult: {result}")
            logging.info(
                "%s: %s and %s = %s",
                operation, num1, num2, result
            )

        except ValueError:
            print("Error: Please enter valid numbers.")
            logging.exception("Invalid numeric input")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
            logging.warning("Invalid zero division operation")

        except OverflowError:
            print("Error: Number is too large.")
            logging.exception("Calculation overflow")

        except Exception as e:
            print(f"Unexpected error: {e}")
            logging.exception("Unexpected calculator error")


if __name__ == "__main__":
    calculator()
