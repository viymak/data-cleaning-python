#remove example
import pandas as pd

#create dataframe
libraries = pd.read_csv('libraries.csv')
bpl_branches = pd.DataFrame(libraries)

# Drop Columns
# Syntax: your_dataframe.drop('1st_dropped_column','2nd_column', 'n_dropped_column' ) - Use axis 0 for rows and axis 1 for columns
drop_columns = bpl_branches.drop(columns=['phone', 'network'])
print(drop_columns)

#### ** Tutorial **
```
# Your Dataframe
dictionary = {'branch': [Central Library in Copley Square,Chinatown,North End,West End], 'address': [700 Boylston Street Boston MA 02116,,25 Parmenter St Boston MA 02113,, 'phone': [617 536-5400,617 807-8176,617 227-8135, 617 523-3957], network: [BPL,BPL,BPL,BPL]}
bpl_branches = DataFrame(data=d)

# Use the dropna function to delete rows that contain no data values in the address column
# Syntax: DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

drop_na = 

# Check results

```
#### ** Answer **
```
# Use the dropna function to delete rows that contain no data values in the address column
# Syntax: DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) - Use axis 0 for rows and axis 1 for columns

drop_na = bpl_branches.dropna(subset=['address'])

# Check results
dropna.head()
```
<!-- tabs:end -->


filter

exampleimport pandas as pd

#create dataframe
data = pd.read_csv('grades.csv')
grades = pd.DataFrame(data)

# filter data to only show exams
# syntax: dataframe[dataframe['column'].str.contains('string we are looking for')]
# adding " ~ " as in the example below will reverse the function and return rows that DO NOT CONTAIN

assessments = grades[~ grades['assignment_type'].str.contains('hw', na=False)]

#check results
print(assessments)

data example 
student,assignment_type,grade_%
Arnaud,exam,
Arnaud,hw,92
Arnaud,quiz 1,82
Binti,exam,72
Binti,hw,83
Binti,quiz 1,82
Cyrus,exam,94
Cyrus,hw,82
Cyrus,exam,81

filter_tutorial
import pandas as pd

#create dataframe
data = pd.read_csv('grades.csv')
grades = pd.DataFrame(data)

# filter data to only show exams
exams = grades[grades['assignment_type'].str.contains('exam', na=False)]

#check results
print(exams)

## Merge

#Tutorial
import pandas as pd
import pprint

#create dataframes
libraries = pd.read_csv('libraries.csv')
bpl_branches = pd.DataFrame(libraries)
libraries_2 = pd.read_csv('weekend_hours.csv')
bpl_hours = pd.DataFrame(libraries_2)


# Syntax: dataframe.merge(dataframe_2, how = "") (Default is inner merge)
# Let's try an outer merge
# We included multiple columns in the merge on parameter so that data from 'branch' & 'address' columns would be combined for each table
weekend_hours = bpl_branches.merge(bpl_hours, on=['branch','address'], how='outer')

# Check the outcome
print(weekend_hours.columns)
print(weekend_hours)



# Merge Answer
import pandas as pd

#create dataframes
libraries = pd.read_csv('libraries.csv')
bpl_branches = pd.DataFrame(libraries)
libraries_2 = pd.read_csv('weekend_hours.csv')
bpl_hours = pd.DataFrame(libraries_2)

# Try to create a table that includes only libraries which appear in both tables
# Syntax: dataframe.merge(dataframe_2, how = "") (Default is inner merge)
weekend_hours = bpl_branches.merge(bpl_hours, on='branch', how='inner')

# Check the outcome
print(weekend_hours.columns)
print(weekend_hours)

#What do you notice about the columns? How can this be explained?