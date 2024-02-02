#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:14:55 2024

@author: josedam
"""

import pandas as pd
#file = pd.read_csv("data_01/country_data.csv")
#print(file)
#print(file.info())

#file = pd.read_csv("data_01/country_data.csv")
#print(file)
#print(file.describe())


file = pd.read_csv("data_01/housing_data.csv")
print(file)
print(file.info())
print(file.describe())

#Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)
print(age[5])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)



# Storing Text
C2 = "M"
C3 = "M"
C4 = "F"
print(C2)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])


# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))
# View a certain range of items:
print(my_list[0:3])

my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])


# Dictionaries
person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name'])
print(person.get('age'))

import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)


# Accessing specific columns
print(df['age'])
print(df['gender'])

# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())


# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4]) 
# Select rows 1 to 3 and all columns
 
# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)
