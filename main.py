if __name__ == "__main__":
    range_maximum = 1000
    for i in range(1, range_maximum):
        number = i
        print_path = f'{str(i).ljust(len(str(range_maximum)))} : '
        while number != 1:
            if (number % 2) == 0:
                number = int(number/2)
                print_path += f'➜  {number} '
            else:
                number = int((number*3)+1)
                print_path += f'➜  {number} '
        number = int(number/2)
        print_path += f'➜  {number} '
        print(print_path)