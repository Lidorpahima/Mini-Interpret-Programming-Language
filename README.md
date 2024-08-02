<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<div class="container">
    <h1>Mini-Interpreter for a Simple Programming Language</h1>
    <p>This project is designed to help students create a mini-interpreter for a simple, custom programming language using Python. This project will enable students to apply principles learned in the course, including syntax, semantics, and basic interpreter design.</p>
    <h2>Project Description</h2>
    <p>The project involves the following steps and requirements:</p>
    <ol>
        <li><strong>Define the Language:</strong>
            <p>Students should design a simple programming language. The language should include:</p>
            <ul>
                <li>Basic arithmetic operations (addition, subtraction, multiplication, division)</li>
                <li>Variable assignments</li>
                <li>Conditional statements (if-else)</li>
                <li>Loop constructs (while or for loops)</li>
                <li>Functions (optional for more advanced students)</li>
            </ul>
        </li>
        <li><strong>Lexical Analysis:</strong>
            <p>Implement a lexer to tokenize the input code. This involves breaking down the code into meaningful tokens such as keywords, operators, identifiers, and literals.</p>
        </li>
        <li><strong>Syntax Analysis:</strong>
            <p>Create a parser to process the tokens and generate an abstract syntax tree (AST). The parser should follow the grammar rules defined for the language.</p>
        </li>
        <li><strong>Semantic Analysis:</strong>
            <p>Implement semantic checks to ensure the code is logically correct. This includes type checking and verifying that variables are declared before use.</p>
        </li>
        <li><strong>Interpreter Implementation:</strong>
            <p>Develop the interpreter to execute the code represented by the AST. The interpreter should be able to handle the basic constructs defined in the language and implement runtime error handling for common errors such as division by zero and syntax errors.</p>
        </li>
        <li><strong>Testing:</strong>
            <p>Write test cases to validate the correctness of the lexer, parser, and interpreter. Provide sample programs written in the custom language to demonstrate its features.</p>
        </li>
        <li><strong>Documentation:</strong>
            <p>Provide clear documentation that includes:</p>
            <ul>
                <li>A language specification detailing the syntax and semantics</li>
                <li>Instructions on how to run the interpreter</li>
                <li>Example programs and expected outputs</li>
            </ul>
        </li>
        <li><strong>Project Report:</strong>
            <p>Write a report discussing the design choices, implementation challenges, and how the principles learned in the course were applied. Include a section on potential future extensions of the interpreter.</p>
        </li>
        <li><strong>Presentation:</strong>
            <p>Prepare a brief presentation to demonstrate the interpreter, showcasing its features and explaining the design and implementation process. Include live examples if possible.</p>
        </li>
    </ol>
    <h2>Evaluation Criteria</h2>
    <ul>
        <li><strong>Correctness and Completeness:</strong> The interpreter should correctly execute programs written in the custom language and handle errors gracefully.</li>
        <li><strong>Design and Implementation:</strong> The design of the language and the quality of the code should reflect good programming practices.</li>
        <li><strong>Documentation and Testing:</strong> Thorough documentation and a comprehensive set of test cases should be provided.</li>
        <li><strong>Presentation and Report:</strong> The presentation and report should clearly explain the project, highlighting the application of course principles and reflecting on the learning experience.</li>
    </ul>
    <h2>Available Functions</h2>
    <p>The interpreter supports the following functions and constructs:</p>
    <ul>
        <li><strong>Math:</strong> Add, Subtract, Multiply, Divide, Power, Square, Min, Max</li>
        <li><strong>String Operations:</strong> Assign, Equal, Not Equal, Greater, Smaller, Or, And, Split, Replace, isUpper, isLower, Concat</li>
        <li><strong>Loops:</strong> While, For</li>
        <li><strong>Arrays:</strong> Array, Length, Index, Add, Remove, Append</li>
        <li><strong>Tuples:</strong> Tuple, Sequence, Sort, Tuple+Tuple to new Tuple, GetItem, Index, Length</li>
        <li><strong>Conditions:</strong> If-else</li>
    </ul>
    <h2>Example Usage</h2>
    <div class="code-container">
        <pre><code>from list_operations import Append, GetElementByIndex, RemoveNegativeValues
# Append example
my_list = [1, 2, 3]
Append(my_list, 4)
print(my_list)  # Output: [1, 2, 3, 4]

# GetElementByIndex example
print(GetElementByIndex(my_list, 2))  # Output: 3

# RemoveNegativeValues example
RemoveNegativeValues(my_list)
print(my_list)  # Output: [1, 2, 3, 4]  # Since there are no negative values, the list remains the same
</code></pre>
    </div>
    <h2>Contributing</h2>
    <p>Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a Pull Request.</p>
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
</div>

</body>
</html>
