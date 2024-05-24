#!/usr/bin/env python
# coding: utf-8

# ## Task 01:

# In[6]:


Total_sum = 0
for number in range (1,11):
    Total_sum  += number


# In[7]:


print("The sum of numbers from 1 to 10 is:", Total_sum)


# In[10]:


items = ["Python", "Numpy", "Pandas"]
print(items)


# In[12]:


for reversed_items in items[::-1]:
    print(reversed_items)


# ## Task 02:

# In[17]:


correct_number = 99
guess = None
while guess != correct_number:
    guess = int(input("Guess the number: "))

    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Incorrect guess. Try again.")



# In[21]:


user_inputs = []
while True:
    user_input = input("Enter something (or type 'done' to finish): ")
      
    if user_input.lower() == 'done':
        break 
    user_inputs.append(user_input)

print("You entered:", user_inputs)


# ## Task 03:

# In[27]:


def even_numbers():
    for numbers in range(2, 21, 2):
        print(numbers)

even_numbers()


# In[29]:


def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"


# In[35]:


def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is undefined."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"


# In[36]:


result = calculator(54, 33, "add")  
print("Result:", result)


# In[39]:


result = calculator(17, 24,"subtract")
print ("Result:", result)


# In[40]:


result = calculator(7, 0, "divide") 
print("Result:", result)


# In[42]:


def find_max(numbers):
    if not numbers:
        return "The list is empty :( "  
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number


# In[44]:


numbers_list = [35, 92, 12, 133, 1987]
max_num = find_max(numbers_list)
print("Maximum number:", max_num)


# In[45]:


numbers_list = []
max_num = find_max(numbers_list)
print("Maximum number:", max_num)


# In[47]:


product = lambda x , y: x * y


# In[48]:


result = product(413, 5)
print("Product:", result)


# In[52]:


def filter_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers


# In[55]:


original_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
even_numbers_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List of even numbers:", even_numbers_list)


# In[ ]:




