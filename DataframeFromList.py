import pandas as pd

List1 = [["Sukhveer", "Singh", "02125"],
         ["Mark", "hamelton", "07310"],
         ["Chris", "Hamsworth", "02215"]]

DF = pd.DataFrame(List1, columns=["First Name","Last Name", "Zip Code" ])

print(DF)

# Method 2 to define the columns in the other variable 
Columns = ["First Name","Last Name", "Zip Code"]
DF2 = pd.DataFrame(List1, columns=Columns)
print(DF2)

# Method 3 to use pd.DataFrame.from_dict() , and zip function

DF3 = pd.DataFrame.from_dict(dict(zip(Columns, zip(*List1))))
print(DF3)


