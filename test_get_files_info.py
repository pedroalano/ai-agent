from functions.get_files_info import get_files_info


def main():
    result = get_files_info("calculator", ".")
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    for line in result.split("\n"):
        print(f"  {line}")
    print()

    result = get_files_info("calculator", "pkg")
    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    for line in result.split("\n"):
        print(f"  {line}")
    print()

    result = get_files_info("calculator", "/bin")
    print('get_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    print(f"    {result}")
    print()

    result = get_files_info("calculator", "../")
    print('get_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    print(f"    {result}")


if __name__ == "__main__":
    main()
