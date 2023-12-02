def multiply_digits(n):
    result = 1
    while n > 0:
        result *= n % 10
        n //= 10
    return result

def multiplication_persistence(num):
    persistence = 0
    while num >= 10:
        num = multiply_digits(num)
        persistence += 1
    return persistence

# Example usage:
num = int(input("Enter a number: "))
result = multiplication_persistence(num)
print(f"Multiplication persistence of {num} is {result}.")
