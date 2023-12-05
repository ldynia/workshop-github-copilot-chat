# Implement fibonacci sequence

def fib_algo(n):
    if n == 0:
        return 0

    if n in {1,2}:
        return 1

    return fib_algo(n-1) + fib_algo(n-2)


def fib(n):
    number = fib_algo(abs(n))

    negative_and_even = (n < 0) and (n % 2 == 0)
    if negative_and_even:
        return -number

    return number

sequence = ""
numbers = ""
for n in range(-10, 11):
    sequence += f"{n}, "
    numbers += f"{fib(n)}, "

print("Sequence:", sequence.strip(", "))
print("Numbers:", numbers.strip(", "))