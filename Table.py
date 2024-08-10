def table(n):
    for i in range (1,10+1):
        print(f"{n} x {i} = {n*i}")


# Example usage
num = int(input("Enter a number to print its multiplication table: "))
table(num)
