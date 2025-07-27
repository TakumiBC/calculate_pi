# calculate_pi

> [!IMPORTANT]
> This project is for educational purposes only and is not intended for production use.

I first came up with this method in Grade 6: draw the whole circle on a computer, count the pixels, and then divide by $r^2$ to calculate the value of $\pi$.  

$$
\pi = \frac{A}{r^2}
$$

Later I optimized the implementation, but the principle stayed the same. Let the x-coordinate of a point be $x$, and the y-coordinate be $y$. Then the way to determine whether a point is in the circle is:

$$
x^2 + y^2 \le r^2 \space (x, y \in \mathbb{N})
$$

In the first quadrant of the circle, for each integer pair $(x, y)$ which satisfies $x,y \in [0, r)$, we check whether it lies inside the circle. Let $P$ be the number of pixels that satisfy the inequality above.

$$
A = 4P
$$
$$
\Rightarrow
\pi = \frac{4P}{r^2}.
$$

## Code

```python
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
```

## Usage

1. Clone this repository:
```shell
git clone https://github.com/TakumiBC/calculate_pi.git
cd calculate_pi
```

2. Run the program:
```shell
python main.py
```
3. To change the accuracy, modify the variable `accuracy` at the first line:
```python
accuracy = 10000
```

## License

This project is licensed under the terms of the MIT License.
