import subprocess
import re

def test_main_file():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.strip().lower()

        with open("main.py", "r") as f:
            code = f.read().lower()

        if result.returncode != 0:
            print("❌ Your program crashed.")
            print("🔧 Error message:\n" + result.stderr.strip())
            return

        passed = 0
        total = 3

        # Find all print statements
        print_lines = re.findall(r"print\s*\((.*?)\)", code)

        def uses_variable(line):
            return "+" in line or "," in line

        # --- Favourite App ---
        if "my favourite app is" in output:
            if any("favourite app" in line and uses_variable(line) for line in print_lines):
                print("✅ Favourite app: correct output and variable used.")
                passed += 1
            else:
                print("⚠️ Favourite app output is correct but no variable was used.")
        else:
            print("❌ Missing or incorrect output: 'My favourite app is ...'")

        # --- Year of Birth ---
        if "my year of birth is" in output:
            if any("year of birth" in line and uses_variable(line) for line in print_lines):
                print("✅ Year of birth: correct output and variable used.")
                passed += 1
            else:
                print("⚠️ Year output is correct but no variable was used.")
        else:
            print("❌ Missing or incorrect output: 'My year of birth is ...'")

        # --- Favourite Food ---
        if "my favourite food is" in output:
            if any("favourite food" in line and uses_variable(line) for line in print_lines):
                print("✅ Favourite food: correct output and variable used.")
                passed += 1
            else:
                print("⚠️ Favourite food output is correct but no variable was used.")
        else:
            print("❌ Missing or incorrect output: 'My favourite food is ...'")

        print(f"\n🎯 You got {passed} out of {total} correct and using variables.")

        if passed == total:
            print("🎉 Excellent work! Your program prints everything and uses variables properly.")
        elif passed == 0:
            print("💡 Hint: use `+` or `,` inside print() to include variables.")

    except Exception as e:
        print("❌ Something went wrong while running your code:")
        print(e)

if __name__ == "__main__":
    test_main_file()
