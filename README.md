# Recovery-of-Formal-Languages

A program, that validates and execute programs by issuing a lexical analysis report made in Python.

Link of the code running in <a href="https://replit.com/@ThomasFrentzel/Recovery-of-formal-languages?v=1">Replit.</a>

##

To obtain the points related to this work, you must make a program, capable of validating and executing programs written in
language proposed below by issuing a lexical analysis report, the classification as valid or
invalidates for each declaration of the language and the result of the program.
Language description
Identifiers: composed only of lowercase letters and numbers;
Special symbols: ?, ), (;
Operations: addition (+), subtraction (-), multiplication (*), division (/), sine (sin), cosine (cos),
exponentiation (exp), root (rot) according to the following examples:
(3 4 +) represents the sum of 3 and 4 and returns 7,000;
   (3.4 2.5 -) represents the subtraction between 3.6 and 2.5 and returns 1,100;
(2.5 3 *) is the product of 2.5 times 3 and returns 7,500;
(2.6 2 /) represents the division of 2.6 by 2 and returns 1,300;
    (sin 30) represents the sine of 30 degrees and returns 0.500;
    (cos 30) represents the cosine of 30 degrees and returns 0.866;
    (exp 3 2) represents 3 to the power of 2 and returns 9,000;
    (rot 81 2) represents the square root of 81 and returns 9000;
Note that all numbers are double precision reals and all results will be
truncated to the third place after the decimal point.
The special symbol will be used to pass the result of one line to the next line. Like this,
a file containing the following declarations:
(3 4 +)
(two ? *)
You should return 14 as an answer in addition to validating all lexemes and validating the
statements. For the example above, the output should be:
Line 1: lexemes: (, 3, 4, +,) all valid
Line 1: syntax: correct
Line 2: lexemes: (, 2, ?, ) all valid
Line 2: syntax: correct
In addition, we will be able to use identifiers and alignment. So to create a variable and
store a value we will use the sentence:
  
(test(2 3*))
In this example, the test variable was created and this variable will store the value 6,000.
A complete program could be written as:
  
(op1 15)
(op2 2)
(sin (op1 op2 *) )
(3 ? *)
In this example the result will be 1,500.
Important considerations: To test your program, you must upload three files
containing programs with 6 or more statements that use all the operations described with at least
least two nesting operations in each test file and with at least one variable in
each test file.
The tests must be able to indicate the behavior of your program if the code created
contains lexical or syntactic errors.
To carry out the lexical validation, you must simulate, in code, a state machine
finite and cannot use any regular expression.
To perform the syntactic validation you can use an LL1 parser or create your own.
claim validation code.
