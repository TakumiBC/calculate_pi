accuracy = 100

def calculate_pi(r):
    pixels = 0
    for x in range(r):
        for y in range(r):
            if x ** 2 + y ** 2 <= r ** 2:
                pixels += 1
    return pixels * 4 / r ** 2

def main():
    print(calculate_pi(accuracy))

if __name__ == "__main__":
    main()
