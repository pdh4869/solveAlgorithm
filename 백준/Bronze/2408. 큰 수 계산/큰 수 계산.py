if __name__ == '__main__':
    n = int(input())
    eq = ''
    for i in range(2 * n - 1):
        eq += input()
    eq = eq.replace('/', '//')
    print(eval(eq))