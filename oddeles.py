...
Write a Python Program to put the even and odd elements in a list into two different lists.
...
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
...
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
...
Sample Input:
5
1
2
3
6
5
...
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
...
Solution : numbers = [5, 2, 9, 1, 5, 6, 8, 3, 10, 4]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  
    else:
        odd_numbers.append(number)    
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
...
O/p : Even numbers: [2, 6, 8, 10, 4]
Odd numbers: [5, 9, 1, 5, 3]

