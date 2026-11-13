# Module 01: Introduction to AI & Python
**Beginner notes | Day 1–Day 4**

## 1. What is Artificial Intelligence (AI)?
Artificial Intelligence is a branch of computer science that focuses on building computer systems that can perform tasks that normally require human intelligence. Examples include understanding language, recognizing images, making recommendations, and helping people make decisions.

**Examples:** voice assistants, spam filters, navigation apps, recommendation systems, face recognition, and chatbots.

## 2. AI, Machine Learning, and Deep Learning
These terms are related, but they do not mean exactly the same thing.

- **Artificial Intelligence (AI):** The broad field of making machines perform intelligent tasks.
- **Machine Learning (ML):** A subset of AI in which a system learns patterns from data and uses them to make predictions or decisions, rather than relying only on explicitly written rules.
- **Deep Learning (DL):** A subset of ML that uses multi-layered neural networks. It is useful for complex data such as images, audio, and natural language.

**Relationship:** Deep Learning is part of Machine Learning, and Machine Learning is part of Artificial Intelligence.

**Simple example – email spam detection:**
- AI is the overall goal of making the email system act intelligently.
- ML learns patterns from examples of spam and non-spam emails.
- DL can use neural networks to learn more complex patterns from large amounts of email data.

## 3. How does Machine Learning work?
A simplified ML workflow:

1. **Collect data:** Gather examples relevant to the problem.
2. **Prepare data:** Correct errors, handle missing values, and format the data.
3. **Train a model:** Let an algorithm learn patterns from training data.
4. **Evaluate:** Test the model on data it has not trained on.
5. **Use the model:** Make predictions on new inputs.
6. **Monitor and improve:** Check performance and update the system when needed.

**Important terms**
- **Dataset:** A collection of data.
- **Feature:** An input property used by a model, such as house area or number of rooms.
- **Label:** The correct answer associated with an example, such as the house price.
- **Model:** A system learned from data that can make predictions.
- **Training:** The process of learning patterns from examples.
- **Prediction:** The model's output for a new input.

## 4. Common types of Machine Learning
- **Supervised learning:** Learns from labelled examples. Examples: predicting house prices and classifying emails as spam or not spam.
- **Unsupervised learning:** Finds patterns in data without provided labels. Example: grouping customers with similar behaviour.
- **Reinforcement learning:** Learns by trying actions and receiving rewards or penalties. Example: an agent learning to play a game.

## 5. Real-world applications of AI
- **Healthcare:** Supporting image analysis and helping organize medical information.
- **Education:** Personalized learning recommendations and learning assistants.
- **Banking:** Detecting unusual transactions and identifying possible fraud.
- **Transport:** Route suggestions, traffic prediction, and driver-assistance systems.
- **Agriculture:** Crop monitoring and identifying plant diseases from images.
- **Entertainment:** Music, movie, and video recommendations.
- **Customer support:** Chatbots that answer common questions.

AI systems can make mistakes and may reflect bias in their data. Important decisions should include human review, privacy protection, and careful testing.

## 6. Installing and running Python
Python is a beginner-friendly, general-purpose programming language used in web development, automation, data analysis, and AI.

1. Install Python from the official Python website: https://www.python.org/downloads/
2. During Windows installation, enable **Add Python to PATH** if that option is shown.
3. Open Command Prompt or a terminal and check:
   `python --version`
   If that command is not recognized on Windows, try:
   `py --version`
4. Create a file named `hello.py`.
5. Add `print("Hello, Python!")` and run it:
   `python hello.py` or `py hello.py`

You can write Python using IDLE, Visual Studio Code, or another code editor.

## 7. Python fundamentals

### 7.1 Output and comments
`print()` displays information. A comment begins with `#` and is ignored by Python.

```python
# This is a comment
print("Welcome to Python")
```

### 7.2 Variables and data types
A variable is a name used to refer to a value. Python determines the type from the assigned value.

```python
name = "Anu"       # str: text
age = 19           # int: whole number
height = 1.62      # float: decimal number
is_student = True  # bool: True or False

print(name, age, height, is_student)
print(type(age))
```

Common types:
- `int` – whole numbers, such as `10`
- `float` – decimal numbers, such as `3.14`
- `str` – text, such as `"Python"`
- `bool` – `True` or `False`

### 7.3 Taking input and type conversion
`input()` reads text from the user. Convert it when a number is needed.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name)
print("Next year you will be", age + 1)
```

### 7.4 Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`

Example:
```python
a = 10
b = 3
print(a + b)  # 13
print(a // b) # 3 (integer/floor division)
print(a % b)  # 1 (remainder)
```

### 7.5 Conditional statements
Use `if`, `elif`, and `else` to choose which block of code runs. Indentation is important in Python.

```python
mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
else:
    print("Keep practising")
```

### 7.6 Loops
A `for` loop is commonly used to iterate over a sequence or a range. A `while` loop repeats while its condition remains true.

```python
for number in range(1, 6):
    print(number)

count = 1
while count <= 3:
    print("Python")
    count += 1
```

`range(1, 6)` produces 1, 2, 3, 4, 5. The stop value 6 is not included.

### 7.7 Functions
A function is a reusable block of code. Define it using `def`. `return` sends a result back to the caller.

```python
def add(a, b):
    return a + b

answer = add(5, 7)
print("Sum:", answer)
```

### 7.8 Lists
A list stores multiple items in one variable. Lists are ordered and can be changed.

```python
subjects = ["Python", "Maths", "AI"]
print(subjects[0])       # Python (index starts at 0)
subjects.append("Java")
subjects[1] = "Science"
print(subjects)

for subject in subjects:
    print(subject)
```

Useful list operations: `append()`, `remove()`, `len()`, and indexing such as `items[0]`.

## 8. Beginner practice programs

### Program 1: Add two numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum =", a + b)
```

### Program 2: Check even or odd
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Program 3: Find the largest of three numbers
```python
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest =", largest)
```

### Program 4: Sum numbers from 1 to n
```python
n = int(input("Enter a positive number: "))
total = 0

for number in range(1, n + 1):
    total += number

print("Sum =", total)
```

### Program 5: Function to calculate square
```python
def square(number):
    return number * number

print(square(6))
```

### Program 6: Average of list values
```python
marks = [80, 75, 90, 85]
average = sum(marks) / len(marks)
print("Average =", average)
```

## 9. Four-day suggested learning plan
- **Day 1:** Understand AI, ML, DL, their relationship, and common applications.
- **Day 2:** Learn how ML works, its three common types, and install Python.
- **Day 3:** Practise variables, data types, input/output, operators, and conditions.
- **Day 4:** Practise loops, functions, lists, and the six beginner programs.

## 10. Quick revision
1. AI is the broad field; ML is a subset of AI; DL is a subset of ML.
2. Supervised learning uses labelled data; unsupervised learning finds patterns without labels; reinforcement learning learns using rewards.
3. `print()` displays output and `input()` accepts user input.
4. Python uses indentation to define code blocks.
5. A `for` or `while` loop repeats instructions.
6. A function is defined using `def`.
7. A list stores multiple values and uses zero-based indexing.

## 11. Self-check questions
1. What is Artificial Intelligence?
2. Explain the relationship between AI, ML, and DL.
3. Give two real-world applications of AI.
4. What is the difference between supervised and unsupervised learning?
5. What are a feature, label, and model?
6. What is the difference between `int`, `float`, `str`, and `bool`?
7. What is the purpose of an `if` statement?
8. What does `range(1, 5)` generate?
9. Why are functions useful?
10. How do you add an item to a list?

---
**Learning reminder:** Run every code example yourself, change the input values, and write a short explanation of what the output means. These notes are a starting point; add your own examples and screenshots as you learn.
