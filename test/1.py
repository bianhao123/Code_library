import pandas as pd

student = pd.read_table('students.txt', sep=',', header=None, names=['sno', 'sname', 'sage', 'ssex', 'sclass'])

course = pd.read_table('course.txt', sep=',', header=None, names=['subject', 'total'])

score = pd.read_table('score.txt', sep=',', header=None, names=['sno', 'subject', 'grade'])

a = pd.merge(score,course,on='subject',how='left')

df1 = a[a['grade']<0.6*a['total']].drop_duplicates(['sno'])
list1 = df1['sno'].to_list()

pass_student = student[~student['sno'].isin(list1)]

df3 = pd.merge(pass_student, score, on='sno')

df3.to_csv('1.csv', index=False)
print(df3[['sno','sname','sclass','subject','grade']])
print('done')