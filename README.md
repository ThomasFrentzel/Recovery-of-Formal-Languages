# Expression Processor

This Python script processes mathematical expressions from input files, performs calculations, and outputs the results. The script handles basic arithmetic operations (`+`, `-`, `*`, `/`), trigonometric functions (`sin`, `cos`), exponentiation, square roots, and validates parentheses.

## Functionality

The script reads input files named `test1.txt`, `test2.txt`, etc., processes the contents, and performs operations based on the parsed expressions that are given.

### Operations Supported:

- **Basic Arithmetic**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
- **Trigonometry**: Sine (`sin`), Cosine (`cos`).
- **Exponentiation**: Exponentiation (`exp`), `base^exponent`.
- **Square Root**: Square root (`rot`).

### Flow:

1. **File Reading**: The script reads the file content line by line.
2. **Token Parsing**: Each line is tokenized into individual components (numbers, operators, function names).
3. **Parentheses Validation**: It ensures that parentheses are properly matched.
4. **Mathematical Operations**: For valid operations, the script performs calculations and prints results.
5. **Handling Special Cases**: The script handles specific operations like trigonometric functions, exponentiation, and square roots, providing formatted output.

### Sample Input

File `test1.txt`:
```text
3 + 5
sin(90)
5 * (2 + 3)
exp(2, 3)
rot(16)
```

### Sample Output

```text
8
1.0
25
8
4
```

---

## Cloning the Repository

To get started with the project, clone the repository:

```bash
git clone https://github.com/ThomasFrentzel/Recovery-of-Formal-Languages
```

## Running the Script

1. Place input files (`test1.txt`, `test2.txt`, etc.) in the project directory.
2. Run the script in your Python environment.
3. Review the results printed to the console.
