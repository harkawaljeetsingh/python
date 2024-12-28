n = int(input("Enter the number of terms: "))
first, second = 0, 1

print("Fibonacci Series:", end=" ")
for i in range(n):
    if i == 0:
        print(first, end=" ")
    elif i == 1:
        print(second, end=" ")
    else:
        next_term = first + second
        first = second
        second = next_term
        print(next_term, end=" ")
print()
