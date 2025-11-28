# 1. Write a recursive function to print numbers from 1 to n.
def print_numbers(x,y=1):
    if y > x:
        return
    else:
        print(y)
        print_numbers(x,y + 1)
print_numbers(10)

# 2. Write a recursive function to find the sum of first n natural numbers.
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)
print(sum_n(10))

# 3. Write a recursive function to calculate the sum of digits of a number. (e.g., 123 → 6)
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n%10)+sum_of_digits(n//10)
print(sum_of_digits(1245))

# 4. Write a recursive function to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))
print(reverse_string("Saikumar"))

# 5. Write a recursive function to count how many digits a number has.

def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
print(count_digits(12345))

# 6. Write a recursive function to print elements of a list one by one.
def print_list_elements(lst, index=0):
    if index == len(lst):
        return
    else:
        print(lst[index])
        print_list_elements(lst, index + 1)
print_list_elements([10, 20, 30, 40, 50])

# 7. Write a recursive function to find the maximum element in a list.

def maxi(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], maxi(lst[1:]))
print("the largest element from list is : ",maxi([7,5,4,32,8,9]))

# 8. Write a recursive function to find the minimum element in a list.
def maxi(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], maxi(lst[1:]))
print("the smallest element from list is : ",maxi([7,5,4,32,8,9]))

# 9. Write a recursive function to check if a string is palindrome.
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
print(palindrome("sai"))
print(palindrome("madam"))

# 10. Write a recursive function to find power(a, b). Eg: 2⁵ = 32
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)
print(power(2, 5))
print(power(3, 4))


# 11. Write a recursive function that prints even numbers from n to 2.
def print_even(n):
    if n < 2:
        return
    if n % 2 == 0:
        print(n)
    print_even(n-1)
print_even(10)

# 12. Write a recursive function that prints odd numbers from n to 1.
def print_odd(n):
    if n<1:
        return
    if n%2!=0:
        print(n)
    print_odd(n-1)
print_odd(10)

# 13. Write a recursive function to multiply two numbers (only + allowed).
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b-1)

print(multiply(5, 2))

# 14. Write a recursive function to find GCD of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(2,3))

# 15. Write a recursive function to convert a decimal number to binary.
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
print(decimal_to_binary(2))

# 16. Write a recursive function to count vowels in a string.
def count_vowel(s):
    if len(s) == 0:
        return 0
    if s[0]  in "aeiou":
        return 1 + count_vowel(s[1:])
    else:
        return count_vowel(s[1:])
print(count_vowel("sai"))

# 17. Write a recursive function to print characters of a string in reverse order.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:])+s[0]
print(reverse_string("hello"))

# 18. Write a recursive function to remove all spaces from a string.
def remove_spaces_recursive(s):
    if len(s)==0:
        return " "
    if s[0].isspace():
        return remove_spaces_recursive(s[1:])
    else:
        return s[0] + remove_spaces_recursive(s[1:])
print(remove_spaces_recursive("s a i k u m a r"))

# 19. Write a recursive function to print elements of a nested list.
# (Example: [1, [2,3], 4])
def print_nested(lst):
    if len(lst) == 0:
        return
    x = lst[0]
    y = lst[1:]
    if type(x) == list:
        print_nested(x)
    else:
        print(x)
    print_nested(y)
print_nested([1, [2,3], 4])

# 20. Write a recursive function to get product of list elements.
def product_of_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] * product_of_list(lst[1:])

numbers = [2, 3, 4, 5]
print("Product of list elements:", product_of_list(numbers))

# ✅ B. FACTORIAL & FIBONACCI TASKS (21–30)
# 21. Write a recursive function that prints factorial values from 1! to n!.
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# 22. Write a recursive function that returns double factorial (n!!). Example: 7!! = 7×5×3×1
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-2)
print(fact(7))

# 23. Write a recursive function that finds sum of factorials from 1! to n!.
def sum_fact(n):
    if n == 1:
        return 1
    return n * sum_fact(n - 1) + sum_fact(n - 1)
print(sum_fact(5))

# 24. Write a recursive program that prints first n Fibonacci numbers.
def fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
         return fibonacci(n-1)+fibonacci(n-2)
for i in range(8):
    print(f'fibonacci({i}) = {fibonacci(i)}')

# 25. Write a recursive function to return the index of a Fibonacci number.

def fibonacci(num, a=0, b=1, index=0):
    if a == num:
        return index
    if a > num:
        return -1
    return fibonacci(num, b, a + b, index + 1)
print(fibonacci(10))

# 26. Write a recursive function to generate Fibonacci series in reverse order.
def fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(8, -1, -1):
    print(fibonacci(i), end=" ")

# 27. Write a recursive function to find the nth Lucas number. (Similar to Fibonacci)
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)
for i in range(8):
    print(f'lucas({i}) = {lucas(i)}')

# 29. Write a recursion task to count how many Fibonacci numbers are ≤ n.
def fiba(n, a=0, b=1):
    if a<=n:
        return 1 + fiba(n, b, a + b)
    else:
        return 0
print(fiba(12))

# 30. Write a recursive function to print Fibonacci pairs like (F(n), F(n+1)).

def fibonacci_pairs(n, a=0, b=1):
    if a > n:
        return 0
    else:
        print(f"({a}, {b})")
        fibonacci_pairs(n, b, a + b)
fibonacci_pairs(12)

# ✅ C. LAMBDA FUNCTION TASKS (31–40)
# 31. Create a lambda function to find the square root of a number.
s=lambda x:x**0.5
print("square root is : ",s(5))

# 32. Create a lambda function to check if a number is positive or negative.
p=lambda x:"positive" if x>0 else "negative"
print("the number is : ",p(-1))

# 33. Lambda to return length of a string.
l=lambda x:len(x)
print("lenght of string is : ",l("saikumar"))

# 34. Lambda to return True if number is divisible by 7.
t=lambda x:True if x%7==0 else False
print(t(8))

# 35. Lambda to extract last character of a string.
last=lambda x:x[-1]
print("last character of a string is : ",last("saikumar"))

# 36. Lambda to check if a string starts with ‘A’.
s=lambda x:x.startswith("a")
print(s("apple"))

# 37. Lambda to compare two strings and return the longer one.
# Lambda to compare two strings and return the longer one
longer = lambda a, b: a if len(a) > len(b) else b
print(longer("Apple", "Banana"))
print(longer("Hello", "Hi"))

# 38. Lambda to convert Celsius to Fahrenheit.
f=lambda x:x*9/5+32
print(f(23))

# 39. Lambda that takes three numbers and returns the largest.
# Lambda to return the largest of three numbers
largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)
print(largest(10, 20, 30))

# 40. Lambda that adds 10 to each number in a list using map().
n=[1,2,3,4,5]
print("before adding : ",n)
a=list(map(lambda x:x+10,n))
print("after adding : ",a)

# ✅ D. TASKS USING map(), filter(), sorted(), reduce() (41–50)
# 41. Use map() to convert a list of words into uppercase.
srings=["sai","kumar","ky"]
print("before : ",srings)
l=list(map(lambda x:x.upper(),srings))
print("after uppercase : ",l)

# 42. Use map() to add 5 to each element in a list.
n=[1,2,3,4,5]
print("before adding : ",n)
a=list(map(lambda x:x+5,n))
print("after adding : ",a)

# 43. Use map() to extract lengths of each string in a list.
strings = ["sai", "kumar", "ky"]
lengths = list(map(len, strings))
print(lengths)

# 44. Use filter() to keep only odd numbers from a list.
list1=[11,2,34,6,8,9]
odd=list(filter(lambda x:x%2!=0,list1))
print(odd)

# 45. Use filter() to keep only names that have more than 5 letters.
names = ["sai", "kumar", "ky", "srinivas", "pavan kumar"]
long_names = list(filter(lambda x: len(x) > 5, names))
print(long_names)

# 46. Use filter() to keep only strings that contain the letter 'a'
names = ["sai", "kumar", "ky", "srinivas", "pavan kumar"]
long_names = list(filter(lambda x:"a" in x,names))
print(long_names)

# 47. Use sorted() with lambda to sort list of tuples by second value.
# Example:
# [(3, 1), (2, 5), (1, 4)] → sort by 2nd element
l1=[(3, 1), (2, 5), (1, 4)]
s=list(sorted(l1,key=lambda x:x[1]))
print(s)

# 48. Use sorted() with lambda to sort a list of strings by their length.
names = ["sai", "kumar", "ky", "saikumar", "pavan kumar"]
le=sorted(names,key=lambda x: len(x))
print(le)

# 49. Use reduce() to find the sum of squares of list numbers.
# (Use lambda + reduce)

from functools import reduce
x=[2,3,4,5,6]
y=reduce(lambda x,y:x+y**2,x,0)
print(y)


# 50. Use reduce() to concatenate a list of strings into one single string
names = ["sai", "kumar", "ky", "srinivas", "pavan kumar"]
result = reduce(lambda a, b: a + b,names)
print(result)

