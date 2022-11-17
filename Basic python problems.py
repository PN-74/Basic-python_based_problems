#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1 Calculate the multiplication and sum of two numbers

2 Print the sum of the current number and the previous number

3 Print characters from a string that are present at an even index number

4 Remove first n characters from a string

5 Check if the first and last number of a list is the same

6 numbers divisible by 5 from a list


# In[7]:


# Calculate the multiplication and sum of two numbers


first_number = int(input("Enter your first number : "))
second_number = int(input("Enter your second number : "))

mul = first_number * second_number
summ = first_number + second_number

print("multiplication of two numbers: ",mul)
print("summation of two numbers: ",summ)


# In[22]:


# Print the sum of the current number and the previous numbers

numbers = [3, 4, 5, 9, 2, 12, 7]

for i in range(len(numbers)):
    if i == 0:
        print(numbers[i],end=" ")
    else:
        print(numbers[i - 1] + numbers[i],end=" ")
      
        
   



# In[29]:


# Print characters from a string that are present at an even index number
   
my_string = str(input("Enter the string: "))
print("characters from a string that are present at even index :")

for i in my_string[0::2]:
   print(i)


# In[46]:


#Remove first n characters from a string
x = "Pooja"
for i in x[0:4:]: 
    print(i,end="")
    
                


# In[51]:


# Check if the first and last number of a list is the same

my_list=[12, 13, 14, 15, 16, 17, 12]
print("The string is :",my_list)
result = my_list[0] == my_list[-1]
print("The first and last number of list is same:",result)
        
        
        


# In[53]:


#numbers divisible by 5 from a list
my_list=[12, 10, 5, 90, 15, 98, 34, 27, 56, 76]
result = list(filter(lambda x:(x % 5 == 0), my_list))
print("numbers divisible by 5 are:",result)


# In[ ]:




