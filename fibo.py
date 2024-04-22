def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    n = int(input("Zadejte kolik prvku Fibonacciho prvku vas zajima: "))
    seq = [recursive_nth_fibo(num) for num in range(0, n)]
    print(seq)
    pass


if __name__ == "__main__":
    main()
