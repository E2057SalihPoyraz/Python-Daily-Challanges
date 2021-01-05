# Given a folder of build files that might look like this:
# /Build-1.dmg
# /Build-2.dmg
# /Build-2.1.dmg
# /Build-2.1.1.dmg
# /Build-3.dmg
# /Build-3.3.dmg
# /Build-3.19.dmg
# Write a script that takes a path to the folder as an argument, and prints the highest build number
# (just the number, i.e. 2.1.1)
# Note: The first digit can go up to 999 and should always be present, but the second and third can only
# go up to 99, and might not be included.

# 1:
import os
import pandas as pd
files = os.listdir('C:/Users/aliyi/PYTHON/Python_Interview_Coding/file_folder')
df = pd.DataFrame(files, columns=['files'])
df['files'] = df['files'].str.replace('Build-','').str.replace('.dmg','')
df[['first','middle','last']] = df.files.str.split(".",expand=True)
df = df.sort_values(by=['last', 'middle', 'first'], ascending=False, axis=0)
print(files)
print(df.head(1)['files'])

#2 :
import pandas as pd
a = """/Build-1.dmg
/Build-2.dmg
/Build-2.1.dmg
/Build-2.1.1.dmg
/Build-2.2.0.dmg
/Build-3.dmg
/Build-3.2.90.dmg
/Build-3.3.dmg
/Build-999.19.25.dmg""".split()
a = pd.Series(a)
a = a.str.extract("(\d+.\d+.\d+|\d+.\d+|\d+)")
versions = [i for i in a[0]]
a = sorted(versions, reverse = True)
print(a)
print(max(a))