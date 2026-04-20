from functions.get_file_content import get_file_content


def main():
    # Test 1: lorem.txt truncation
    result = get_file_content("calculator", "lorem.txt")
    print('get_file_content("calculator", "lorem.txt"):')
    print(f"  Length: {len(result)} characters")
    print(f"  Ends with: ...{result[-60:]}")
    print()

    # Test 2: main.py
    result = get_file_content("calculator", "main.py")
    print('get_file_content("calculator", "main.py"):')
    print(result)
    print()

    # Test 3: pkg/calculator.py
    result = get_file_content("calculator", "pkg/calculator.py")
    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(result)
    print()

    # Test 4: outside working directory
    result = get_file_content("calculator", "/bin/cat")
    print('get_file_content("calculator", "/bin/cat"):')
    print(f"  {result}")
    print()

    # Test 5: non-existent file
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(f"  {result}")


if __name__ == "__main__":
    main()
