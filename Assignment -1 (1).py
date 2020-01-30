#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 

# In[1]:


list=[]
i=2000
while(i<=3200):
	if(i%7==0 and i%5!= 0): list.append(i)
	i=i+1

	
print(list)


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name

# In[4]:


firstname = input()[::-1]

secondname = input()[::-1]
firstname +" "+ secondname
secondname+" "+firstname


# 3.Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[5]:


d=12
V = (4/3)*(22/7)*pow((d/2),3)
print("Volume of sphere is: ",V)


# 4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[8]:


val= input("Enter few numbers: ")
list = val.split(",")
print(list)

5. Create the below pattern using nested for loop in Python. 
 
 
*  
* *  
* * * 
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
 
 
# In[18]:


n=5
for i in range(1,n+1,1):
            print("* "*i)
for j in range(i-1,0,-1):
    print("* "*j)


# 6. Write a Python program to reverse a word after accepting the input from the user. 
#  
# Sample Output: 
#  
# Input word: iNeuron 
#  
# Output: norueNi

# In[19]:


var=input()[::-1]
print(var)


# 7. Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 
#  
# Sample Output: 
#  
# WE, THE PEOPLE OF INDIA,   having solemnly resolved to constitute India into a SOVEREIGN, !  SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC    and to secure to all its citizens 

# In[51]:


str="WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
str2= str.split()

for i in str2:
   if i == 'SOCIALIST,':
        str1 = str[:str.index('SOCIALIST')]+" ! "+str[str.index('SOCIALIST'):]
        print(str1)
      


# Note : - NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source code​ ​used​ ​ and​  ​the​ ​output

# In[ ]:





# In[ ]:




