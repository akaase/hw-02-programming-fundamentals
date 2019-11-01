# Assignment: Programming Fundamentals

So, you've just installed Python! Let's put your skills to the test.

This assignment will walk through the fundamental features of the Python language using short, simplified code examples.

If you find yourself wondering "why would I ever write this code?" or "ok, but what is this thing _for_?", try not to panic! Today's assignment is about discovering **what** is possible in Python, not **why** those features are useful.

However, if you can start to envision how you might use these features in more complicated programming scenarios, that's great!

## Learning Goals

In this assignment, you'll practice:

* Creating local `.py` files and adding them to a repo
* Running local `.py` files from your terminal
* Declaring and using variables
* Input and Output with `input` and `print`
* Understanding Basic Data Types
* Converting between Basic Data Types
* Using mathematical operators

---

# Deliverables

1. **Fork** the assignment repo so that you have a copy of it that belongs to you, living on Github.

1. Open your Terminal and navigate to the folder for all of your development work with:

   ```bash
   cd $DEV
   ```

1. **Clone** your fork of the assignment repo onto your computer. Remember to clone _your_ fork of the repo, not the instructor's, so that you can make changes to it!

   ```bash
   git clone <git url to your fork of the assignment repo>
   ```

1. Open the assignment folder with your code editor

1. Write your code and solve the problems. Remember to **save** frequently

1. Run the program from the command line to check your work.

   Remember that to run a program from the command line, enter:

   ```bash
   python file.py
   ```

   > **Protip**: You may need to use the `cd` command to navigate to the location where the `file.py` is saved

1. Keep making changes to your code and run it again until you get the expected output. Repeat as needed!

   > **Hint**: Make sure you are printing something out with the `print` statement! Otherwise, you won't see any output from running your program!

1. **Commit** your changes regularly

1. Finally, **push** all of the changes to Github

---

# Exercise 1: Decoding R2D2

You are friends with a robot who communicates in a series of beeps and boops. You usually get the gist of what he means, but just once it would be nice to know what's really on his mind!

You've noticed a pattern in the beeps and boops, and it seems like the number of beeps and boops correspond to specific letters, according to this **key-value** chart:

| Code | Letter | Code | Letter |
| --- | --- | --- | --- |
| 1 | A | 14 | N |
| 2 | B | 15 | O |
| 3 | C | 16 | P |
| 4 | D | 17 | Q |
| 5 | E | 18 | R |
| 6 | F | 19 | S |
| 7 | G | 20 | T |
| 8 | H | 21 | U |
| 9 | I | 22 | V |
| 10 | J | 23 | W |
| 11 | K | 24 | X |
| 12 | L | 25 | Y |
| 13 | M | 26 | Z |

Here is the full list of beeps and boops you wrote down when you were having a "conversation" with R2D2 earlier...

```
2 beeps, 6 boops
0 beeps, 5 boops
9 beeps, 3 boops
4 beeps, 8 boops
10 beeps, 5 boops
BOP! (pretty sure this is a space!)
11 beeps, 12 boops
5 beeps, 10 boops
1 beep, 17 boops
5 beeps, 7 boops
4 beeps, 0 boops
```

Let's take the first part as an example. To decode it, you write the following Python code:

```python
beeps = 2
boops = 6
total = beeps + boops
print(total)
```

When you run it, the total that is printed is `8`. Now, look that up in the chart earlier.

According to the chart, the first letter (corresponding to `8`) is `H`! It's your job to figure out the rest of the message.

In the (already existing) `exercise1.py` file, write the code to print out the numerical total for each beep-boop combo as we did above. Note the letter that the number corresponds to in a comment.

### Starter Code

This is already inside `exercise1.py`:

```python
beeps = 2
boops = 6
total = beeps + boops
print(total) # 8 = H

# Continue the rest of your code here!
```

### Expected Output

After you finish writing all the code, this is what we expect to be output on the Terminal:

```
8
5
12
12
15
23
15
18
12
4
```

# Exercise 2

**Create a new file** called `exercise2.py`. Open it up in your code editor and enter the solutions for the problems below.

Try annotating your code by leaving comments (using the `#` symbol) in the file, before each of your answers to the following questions.

Be sure to **commit** after answering each question!

1. How would you calculate a good tip for a 55 dollar meal? Use `print` to print the numerical tip you would give.
    > Example Output: `8.25`

1. Now, print the tip with a `$` in front of it. You'll have to do **type conversion** to make this work.
    > Example Output: `$8.25`

1. Outputting the result of 45628 multiplied by 7839, in a sentence. You will have to use string **interpolation**.
    > Example Output: `The result of the mutiplication is XXXXXXXX`

1. Add a **string** and an **integer** together with the `+` operator. What happens? Find a way to convert the integer into a string before adding them together, and use `print` to print the result.

1. (**STRETCH**) What's the value of the expression `(10 < 20 and 30 < 20) or not (10 == 11)`? Try figuring it out on your own before typing it in. (This is a hard one, don't worry if you can't get it, but please try!)

# Exercise 3

Let's make a Python program that greets someone by name.

**Create a new file** called `exercise3.py` and open it up in your code editor.

Start with displaying a question:

```python
print('What is your name?')
```
Run your program to verify that it works so far. If it works, **commit** what you've got so far with a meaningful commit message.

The next step is to get input from your hypothetical user (for now the user is just you!).

We can do that with `input()`.

`input()` will pause the execution of your program and give your user the chance to type something into their terminal.  When the user finishes typing and hits "enter", the value that they typed in is **returned** by `input()` and your program resumes normal execution.

Try assigning `input()` to a variable in order to save your user's input.

```python
print('What is your name?')
user_name = input()
print(f'Hello, {user_name}')
```

Note that `input()` always gives back the user's input *as a string*.

Having that input string stored in a variable allows us to display it back to the user later on.

### Your Challenge

Ask the user how old they are, and have the program output what year **they were born in**.

For example, if the user enters `19`, the output should be something like `You were born in the year 2000`.

Don't forget to commit your work again!

---

# Submitting

To submit this assignment:

1. Go to the **assignment's main repo** (not your fork)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, copy and paste the URL to *your* assignment repo
1. Click **Submit new issue** and you're done!

---

# Yay! All done!

![](https://media.giphy.com/media/rl1aX0WUmGcKs/giphy.gif)

Now, if you want to know a little more about why that particular message was chosen, [read up here](https://blog.hackerrank.com/the-history-of-hello-world/)!
