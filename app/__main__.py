from app.calculator import Calculator

class App:
    def __init__(self):
        self.calculator = Calculator()
        self.commands = {
            "help": self._show_help,
            "history": self._show_history,
            "exit": self._exit_app
        }

    def _show_help(self):
        """Displays help information."""
        print("\nAvailable commands:")
        print("  add, subtract, multiply, divide - perform a calculation")
        print("  history - view past calculations")
        print("  help - show this help message")
        print("  exit - exit the application\n")

    def _show_history(self):
        history = self.calculator.get_calculation_history()
        if not history:
            print("\nNo calculations in history yet.\n")
            return
        print("\nCalculation History:")
        for record in history:
            print(f"  {record}")
        print()

    def _exit_app(self):
        print("Exiting calculator. Goodbye!")
        raise SystemExit

    def _get_operands(self) -> tuple[float, float]:
        while True:
            try:
                operand_a = float(input("Enter the first number: "))
                operand_b = float(input("Enter the second number: "))
                return operand_a, operand_b
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def start(self):
        print("Welcome to the Professional Command-Line Calculator!")
        self._show_help()
        
        while True:
            try:
                command = input(">>> Enter command: ").strip().lower()

                if command in self.calculator.operations:
                    a, b = self._get_operands()
                    try:
                        result = self.calculator.perform_calculation(command, a, b)
                        print(f"Result: {result}")
                    except ValueError as e:
                        print(e)
                elif command in self.commands:
                    self.commands[command]()
                else:
                    print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")
            except SystemExit:
                break
            except KeyboardInterrupt:
                print("\nExiting calculator. Goodbye!")
                break
            except Exception as e: 
                print(f"An unexpected error occurred: {e}")
                break

def main(): # pragma: no cover
    app = App()
    app.start()

if __name__ == "__main__":
    main()