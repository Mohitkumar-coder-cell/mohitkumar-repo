'''-------------Mohit kumar-----------

Install python
python -n pip install jupyter  -- on cmd
jupyter notebook  -- on cmd
create folder
!pip install numpy
import numpy as np
print(np.__version__)

# Chapter -1 creating arrays

numpy.org -- website document & more

arr_list1=np.array([1,2,3])
print(arr_list1)
print(type(arr_list1))
print(arr_list_3.ndim)

list1 = [1,2,3]
list2=[4,5,6]
arr_list_2=np.array([list1,list2])
print(arr_list_2)
print(arr_list_3.ndim)

list1 = [1,2,3]
list2=[4,5,6]
list3=[7,8,9]
arr_list_3=np.array([[list1,list2,list3]])
print(arr_list_3)
print(arr_list_3.ndim)

# Chapter -2 numpy array attributes

arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)

# Attributes of Array (properties of array)
print("Shape", arr1.shape)  # share= rows, columns and height of array
print("Size", arr1.size)    # number of elements in array
print("dType", arr1.dtype)  # data type of elements in array
print("n_dim", arr1.ndim)   # dimension of array

# Chapter -3 Array initialization methods

# zeros array : all elements are 0
zero_arr = np.zeros((2,3))
print(zero_arr)

# ones array : all elements are 1
one_arr = np.ones((2,3))
print(one_arr)

# Full array : all elements are same based on given value
full_arr = np.full((3,2), 9)
print(full_arr)

# Identity Matrix : diagonal elements are ones and all other elements are zeros
id_arr = np.eye(3)
print(id_arr)

# empty array
print(np.empty(2))

# evenly spaced array : elements are evenly spaced based on step value
print(np.arange(2,10,2))

# specific number of eqaully spaced values between a range : elements are equally spaced based on step value
print(np.linspace(1,10,4))

# random values array - float
r_arr = np.random.rand(3,2)
print(r_arr)

# random values array - int
rint_arr = np.random.randint(1,100,(3,3))
print(rint_arr)

# Chapter -4 Array Indexing and Slicing

a = np.array([1,3,5,7,9])
print(a)
print(a[0])     # first element of array
print(a[4])     # fifth element of array
print(a[-1])      # last element of array

# Slicing :
# array[start:stop:step]
# stop - index, that is not included in output

print(a[0:3]) # First 3 elements
print(a[-3:]) # Last 3 elements
print(a[1:4]) # Middle 3 elements
print(a[0::3]) # Middle 3 elements with steps
print(a[0::2]) # All alternative elements with steps

# Indexing on 2 Dimensional Array
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)

# 2D Array: [rows, columns]                   # 2D Array takes 2 values - rows and columns for indexing
# 3D Array: [layers/height, rows, columns]    # 3D Array takes 3 values - height, rows and columns for indexing

print(arr2[0]) # first row
print(arr2[1]) # second row

print(arr2[0][0]) # element of first row and first column
print(arr2[0][1]) # element of first row and second column
print(arr2[1][2]) # element of second row and third column

# Slicing on 2D array
print(arr2[1]) # specific element - 1D
print(arr2[1:]) # slicing part - 2D

print(arr2)

# 2D Array: [rows, columns]  |  eg: arr2[0][1]     # 2D Array takes 2 values - rows and columns for indexing

print(arr2[:, 0])       # First column of an array
print(arr2[:, 1])       # Second column of an array
print(arr2[:, 2])       # Third column of an array

# 3D Array: [layers/height, rows, columns]        # 3D Array takes 3 values - height, rows and columns for indexing

arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr3)

print(arr3[0])
print(arr3[1])
print(arr3[2])

print(arr3[0][2])
print(arr3[2][2])


print(arr3[:, 0]) # 1st col value
print(arr3[:, 1]) # 2nd col value
print(arr3[:, 2]) # 3rd col value

print(arr3[::, 1:2])  #slicing on columns
print(arr3[2::, 1:2]) #slicing on rows and columns

# Chapter -5 Array Reshaping and Flattening

# Reshape Array: changing its dimensions (e.g., rows and columns) without altering the actual data
# Flatten Array: transforming a multi-dimensional array into a single-dimensional array

arr1 = np.array([1,2,3,4,5,6])      # shape = (1,6) - 1 row and 6 columns
print(arr1)

reshaped = arr1.reshape((6,1))      # shape = (6,1) - 6 rows and 1 column
print(reshaped)

reshaped2 = arr1.reshape((2,3))     # re-shaped array from (1,6) to (2,3)
print(reshaped2)

print(reshaped2.flatten())          # flattened array from higher (2D) dimensional (2,3) to (1,6) (1D)

# Chapter -6 Array Stacking and Splitting

# Array Stacking:  combining multiple arrays along a new axis, resulting in an array with a higher dimension than the input arrays
# Array Splitting:

# stacking
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b))) # vertical stacking - row wise          -> output array is 2D
print(np.hstack((a,b))) # horizontal stacking - column wise     -> output array is 1D

# splitting
c = np.array([[1,2,3], [4,5,6]])
print(c)

hsplit = np.hsplit(c,3) # horizontal split -> input and output array are same dimention

for s in hsplit:
    print(s)

vsplit = np.vsplit(c,2) # vertical split -> input and output array are same dimention

for s in vsplit:
    print(s)

# Chapter -7 Mathematical Operations on Array

# FYI: list vs Array
# one of the reason we array instead of list : time taken by an operation on list is more >>>>> than array
%%time
numbers = list(range(1, 100000001))
result = [x+5 for x in numbers]

%%time
numbers = np.arange(1,100000001)
result = numbers+5

a = np.array([10,20,40,-30])
print(a)

print(a+10) # add a value in array
print(a-30) # subs a value in array
print(a*2) # multiply by a value in array
print(a/10) # divide by a value in array

b = np.array([1,4,9])
print(b)

print(np.square(b)) # square of all array elements
print(np.sqrt(b))   # square root of all array elements

# Chapter -8 Mathematical Operations on Muliple Arrays

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)

print(np.add(a,b))          # add two arrays
print(np.subtract(a,b))     # subtract two arrays
print(np.multiply(a,b))     # multiply two arrays
print(np.divide(a,b))       # divide two arrays

# Dot product: computes the inner product of the two vectors and sum the results
print(np.dot(a,b)) # dot product

print(a.T) # Transpose: Returns an array with axes transposed

t = np.array([[1,2,3],
              [4,5,6]])

print(t)    # initial shape: 2,3
print(t.T)  # shape after transpose: 3,2

# Chapter -9 Statistical Functions

a = np.array([[1,2,3], [4,5,6]])
print(a)

print(np.sum(a))    # sum of all elements of an array

print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))'''













'''Chapter 1 — Pandas Introduction & Installation
Chapter 2 — Series
Chapter 3 — DataFrame
Chapter 4 — DataFrame Attributes
Chapter 5 — Creating DataFrame
Chapter 6 — Reading CSV/Excel Files
Chapter 7 — Selecting Rows & Columns
Chapter 8 — Filtering Data
Chapter 9 — Adding/Updating/Deleting Data
Chapter 10 — Sorting
Chapter 11 — GroupBy & Aggregation
Chapter 12 — Missing/NULL Values
Chapter 13 — Duplicates
Chapter 14 — String Operations
Chapter 15 — Date & Time
Chapter 16 — Merge, Join & Concatenate
Chapter 17 — Pivot Tables
Chapter 18 — Basic Data Analysis
Example: Chapter 1
!pip install pandas

import pandas as pd

print(pd.__version__)
Chapter 2 — Series
import pandas as pd

a = [10, 20, 30, 40, 50]

s = pd.Series(a)

print(s)

Output:

0    10
1    20
2    30
3    40
4    50
dtype: int64

Yahan:

pd.Series() → 1D data banata hai
0,1,2,3,4 → index
10,20,30... → values

Custom index:

s = pd.Series([10,20,30], index=["a","b","c"])

print(s)

Output:

a    10
b    20
c    30
dtype: int64

Access:

print(s["a"])

Output:
10

Chapter 3 — DataFrame

data = {
    "name": ["Aman", "Rohit", "Mohit"],
    "age": [20, 21, 19],
    "marks": [80, 75, 90]
}

df = pd.DataFrame(data)

print(df)

Output:

    name  age  marks
0   Aman   20     80
1  Rohit   21     75
2  Mohit   19     90

DataFrame ko simple language mein table jaisa structure samjho:

        columns
          ↓
name | age | marks
------------------
Aman | 20  | 80
Rohit| 21  | 75
Mohit| 19  | 90
 ↑
rows

Important DataFrame Attributes
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)

Yaad rakhna:

shape → rows, columns
size → total elements
columns → column names
index → row numbers
dtypes → har column ka datatype

Agar tumhare test mein NumPy ke saath Pandas bhi aa raha hai, toh main isi format mein Pandas Chapter 1–18 ke proper notes + important MCQs + coding questions bhi bana sakta hoon.

pure notes do na chapter waise

Haan bhai 😄 pure Pandas notes bilkul tumhare NumPy notes ke same format mein — Chapter-wise + code + comments + easy Hinglish explanation. Isko tum Jupyter Notebook mein directly practice kar sakte ho.

🐼 PANDAS — COMPLETE CHAPTER-WISE NOTES
Chapter 1 — Pandas Installation & Introduction
Pandas install karna

Jupyter Notebook mein:

!pip install pandas

Import:

import pandas as pd

Version check:

print(pd.__version__)
Pandas kya hai?

Pandas Python ki library hai jo mainly data analysis aur data manipulation ke liye use hoti hai.

Pandas ke 2 main data structures:

Series → 1D
DataFrame → 2D
Chapter 2 — Pandas Series

Series ek one-dimensional labeled array hoti hai.

import pandas as pd

a = [10,20,30,40,50]

s = pd.Series(a)

print(s)

Output:

0    10
1    20
2    30
3    40
4    50
dtype: int64

Yahan:

0  → index
10 → value
Custom Index
s = pd.Series(
    [10,20,30],
    index=["a","b","c"]
)

print(s)

Output:

a    10
b    20
c    30
Series indexing
print(s["a"])

Output:

10

Position se:

print(s.iloc[0])


Chapter 3 — Series from Dictionary

Dictionary ko Series mein convert kar sakte hain.

data = {
    "a": 10,
    "b": 20,
    "c": 30
}

s = pd.Series(data)

print(s)

Output:

a    10
b    20
c    30
Specific values select karna
data = {
    "maths": 80,
    "english": 70,
    "science": 90
}

s = pd.Series(data)

print(s[["maths","science"]])


Chapter 4 — DataFrame

DataFrame = 2D table

Excel table jaisa samajh lo.

data = {
    "name": ["Aman","Rohit","Mohit"],
    "age": [20,21,19],
    "marks": [80,75,90]
}

df = pd.DataFrame(data)

print(df)

Output:

    name  age  marks
0   Aman   20     80
1  Rohit   21     75
2  Mohit   19     90

Structure:

        columns
           ↓
name | age | marks
------------------
Aman | 20  | 80
Rohit| 21  | 75
Mohit| 19  | 90
 ↑
rows


Chapter 5 — DataFrame Attributes
print(df.shape)

Rows aur columns:

(3, 3)
Size
print(df.size)

Total elements:

9
Columns
print(df.columns)
Index
print(df.index)
Data types
print(df.dtypes)
Dimensions
print(df.ndim)
Information
print(df.info())
Statistical summary
print(df.describe())
Chapter 6 — Creating DataFrame
List of Lists
data = [
    ["Aman",20,80],
    ["Rohit",21,75],
    ["Mohit",19,90]
]

df = pd.DataFrame(
    data,
    columns=["name","age","marks"]
)

print(df)
Dictionary
data = {
    "name": ["Aman","Rohit","Mohit"],
    "age": [20,21,19],
    "marks": [80,75,90]
}

df = pd.DataFrame(data)

print(df)
Chapter 7 — Reading CSV Files

CSV = Comma Separated Values

df = pd.read_csv("students.csv")

print(df)

First 5 rows:

print(df.head())

First 10:

print(df.head(10))

Last 5:

print(df.tail())

Last 10:

print(df.tail(10))
CSV ka data check
print(df.info())
print(df.describe())
Chapter 8 — Reading Excel Files
df = pd.read_excel("students.xlsx")

print(df)

Specific sheet:

df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet1"
)


Chapter 9 — Selecting Columns

Example:

data = {
    "name": ["Aman","Rohit","Mohit"],
    "age": [20,21,19],
    "marks": [80,75,90]
}

df = pd.DataFrame(data)
One column
print(df["name"])
Multiple columns
print(df[["name","marks"]])

Important:

df["name"]

→ Series

df[["name"]]

→ DataFrame

Chapter 10 — Selecting Rows
iloc

iloc → position/index number ke according data select karta hai.

print(df.iloc[0])

First row.

print(df.iloc[1])

Second row.

Multiple rows
print(df.iloc[0:2])
Specific row + column
print(df.iloc[0,1])

First row, second column.

Multiple rows and columns
print(df.iloc[0:2, 0:2])
Chapter 11 — loc

loc labels ke according data select karta hai.

df = pd.DataFrame(
    {
        "name":["Aman","Rohit","Mohit"],
        "marks":[80,75,90]
    },
    index=["a","b","c"]
)

print(df.loc["a"])

Multiple:

print(df.loc[["a","c"]])

Specific column:

print(df.loc["a","marks"])
Chapter 12 — Filtering Data

Ye bahut important topic hai.

Suppose:

print(df)

Marks greater than 80:

print(df[df["marks"] > 80])

Marks less than 80:

print(df[df["marks"] < 80])

Marks equal to 80:

print(df[df["marks"] == 80])
Multiple conditions

AND:

print(df[
    (df["age"] > 18) &
    (df["marks"] > 80)
])

OR:

print(df[
    (df["age"] > 20) |
    (df["marks"] > 80)
])

Important:

& → AND
| → OR


Chapter 13 — Adding New Column
df["city"] = ["Delhi","Mumbai","Delhi"]

print(df)

Calculated column:

df["marks2"] = df["marks"] + 5

print(df)
Example
df["pass"] = df["marks"] >= 40

print(df)

Output mein True/False aayega.

Chapter 14 — Updating Column
df["marks"] = df["marks"] + 10

Specific value:

df.loc[0,"marks"] = 95

Condition ke basis par:

df.loc[df["marks"] < 40, "marks"] = 40

Matlab jiski marks 40 se kam hai, usko 40 kar do.



Chapter 15 — Adding Rows

New row add karne ka modern method:

new_row = pd.DataFrame({
    "name":["Rahul"],
    "age":[22],
    "marks":[85]
})

df = pd.concat([df,new_row], ignore_index=True)

print(df)
Chapter 16 — Deleting Rows & Columns
Column delete
df = df.drop("age", axis=1)

axis=1 → column

Row delete
df = df.drop(0, axis=0)

axis=0 → row

Multiple columns:

df = df.drop(
    ["age","city"],
    axis=1
)


Chapter 17 — Sorting Data
Ascending
df = df.sort_values("marks")

print(df)
Descending
df = df.sort_values(
    "marks",
    ascending=False
)

Multiple columns:

df = df.sort_values(
    ["age","marks"]
)
Chapter 18 — Missing / NULL Values

Missing value check:

print(df.isnull())

Total NULL values:

print(df.isnull().sum())

Alternative:

print(df.isna().sum())
NULL rows
print(df[df["marks"].isnull()])
NOT NULL
print(df[df["marks"].notnull()])
Chapter 19 — Handling Missing Values
Delete NULL rows
df = df.dropna()
Fill NULL
df = df.fillna(0)

Specific column:

df["marks"] = df["marks"].fillna(0)

Mean se fill:

df["marks"] = df["marks"].fillna(
    df["marks"].mean()
)

Median:

df["marks"] = df["marks"].fillna(
    df["marks"].median()
)


Chapter 20 — Duplicates

Duplicate check:

print(df.duplicated())

Total duplicates:

print(df.duplicated().sum())

Duplicates remove:

df = df.drop_duplicates()

Specific column:

df = df.drop_duplicates(
    subset=["name"]
)
Chapter 21 — Unique Values

Column ke unique values:

print(df["city"].unique())

Unique values ki count:

print(df["city"].nunique())

Har value kitni baar hai:

print(df["city"].value_counts())

Example:

Delhi      5
Mumbai     3
Jaipur     2
Chapter 22 — Mathematical Functions
print(df["marks"].sum())

Average:

print(df["marks"].mean())

Median:

print(df["marks"].median())

Minimum:

print(df["marks"].min())

Maximum:

print(df["marks"].max())

Standard deviation:

print(df["marks"].std())

Count:

print(df["marks"].count())
Chapter 23 — GroupBy

Ye bhi bahut important hai.

Example:

data = {
    "city":["Delhi","Delhi","Mumbai","Mumbai"],
    "marks":[80,90,70,85]
}

df = pd.DataFrame(data)

City-wise average:

print(
    df.groupby("city")["marks"].mean()
)

City-wise total:

print(
    df.groupby("city")["marks"].sum()
)

City-wise maximum:

print(
    df.groupby("city")["marks"].max()
)
Chapter 24 — GroupBy Multiple Aggregations
print(
    df.groupby("city")["marks"].agg(
        ["sum","mean","min","max"]
    )
)

Output mein ek saath:

sum
mean
min
max
Chapter 25 — query()

Filtering ka ek aur method:

print(
    df.query("marks > 80")
)

Multiple condition:

print(
    df.query("marks > 80 and city == 'Delhi'")
)
Chapter 26 — Rename Columns
df = df.rename(
    columns={
        "name":"student_name",
        "marks":"score"
    }
)

print(df)
Chapter 27 — String Operations

Suppose:

df["name"]

Uppercase:

df["name"].str.upper()

Lowercase:

df["name"].str.lower()

Length:

df["name"].str.len()

Contains:

df[df["name"].str.contains("A")]

Starts with:

df[df["name"].str.startswith("A")]

Ends with:

df[df["name"].str.endswith("n")]
Chapter 28 — Replace Values
df["city"] = df["city"].replace(
    "Delhi",
    "New Delhi"
)

Multiple values:

df["city"] = df["city"].replace({
    "Delhi":"New Delhi",
    "Mumbai":"Bombay"
})
Chapter 29 — Apply Function
df["marks"] = df["marks"].apply(
    lambda x: x + 5
)

Example:

def add_bonus(x):
    return x + 5

df["marks"] = df["marks"].apply(add_bonus)
Chapter 30 — Merge

Do DataFrames ko combine karna.

df1 = pd.DataFrame({
    "id":[1,2,3],
    "name":["Aman","Rohit","Mohit"]
})

df2 = pd.DataFrame({
    "id":[1,2,3],
    "marks":[80,75,90]
})

Merge:

result = pd.merge(
    df1,
    df2,
    on="id"
)

print(result)
Chapter 31 — Concatenate

Rows ko combine:

df1 = pd.DataFrame({
    "name":["Aman","Rohit"]
})

df2 = pd.DataFrame({
    "name":["Mohit","Rahul"]
})

result = pd.concat(
    [df1,df2],
    ignore_index=True
)

print(result)
Difference
concat → DataFrames ko directly jodta hai

merge → common column/key ke basis par join karta hai
Chapter 32 — Pivot Table
data = {
    "city":["Delhi","Delhi","Mumbai","Mumbai"],
    "gender":["M","F","M","F"],
    "marks":[80,90,70,85]
}

df = pd.DataFrame(data)

Pivot:

result = pd.pivot_table(
    df,
    values="marks",
    index="city",
    columns="gender",
    aggfunc="mean"
)

print(result)

Pivot table ka use data ko summary form mein arrange karne ke liye hota hai.

Chapter 33 — Date & Time
df["date"] = pd.to_datetime(df["date"])

Year:

df["date"].dt.year

Month:

df["date"].dt.month

Day:

df["date"].dt.day

Day name:

df["date"].dt.day_name()
Chapter 34 — Export Data

CSV mein save:

df.to_csv(
    "output.csv",
    index=False
)

Excel mein:

df.to_excel(
    "output.xlsx",
    index=False
)

index=False ka matlab unnecessary index column save nahi karna.

⭐ Chapter 35 — Most Important Pandas Commands

Ye commands pakka yaad kar lena:

import pandas as pd
pd.Series()
pd.DataFrame()
pd.read_csv()
pd.read_excel()
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.size
df.columns
df.dtypes
df["column"]
df.iloc[]
df.loc[]
df.isnull()
df.dropna()
df.fillna()
df.drop()
df.sort_values()
df.groupby()
df.duplicated()
df.drop_duplicates()
df.unique()
df.value_counts()
df.rename()
df.replace()
df.merge()
pd.concat()
pd.pivot_table()
🔥 NumPy vs Pandas — Ek line mein
NumPy	Pandas
np.array()	pd.DataFrame()
Numerical calculations	Data analysis
Mostly arrays	Tables/DataFrames
shape	shape
reshape()	pivot_table()
Mathematical operations	Filtering, grouping, cleaning
Fast numerical computation	Structured/tabular data'''