student_dict = {
    "name": ["John" , "Smith", "Alex", "Jony", "Tony"],
    "age": [25,26, 23, 24, 21]
}

import pandas as pd
student_df = pd.DataFrame(student_dict)
print(student_df)

# loop through a data frame
for (index, row) in student_df.iterrows():
    print(row)


# loop through row of a data frame
for (index, row) in student_df.iterrows():
    if row["name"] == "John":
        print(row["age"])