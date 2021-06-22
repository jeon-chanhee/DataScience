
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head(3)


# In[2]:


age0 = titanic[(titanic['age']>=0) & (titanic['age']<10)]
age1 = titanic[(titanic['age']>=10) & (titanic['age']<20)]
age2 = titanic[(titanic['age']>=20) & (titanic['age']<30)]
age3 = titanic[(titanic['age']>=30) & (titanic['age']<40)]
age4 = titanic[(titanic['age']>=40) & (titanic['age']<50)]
age5 = titanic[(titanic['age']>=50) & (titanic['age']<60)]
age6 = titanic[(titanic['age']>=60) & (titanic['age']<70)]
age7 = titanic[(titanic['age']>=70) & (titanic['age']<80)]

print('0~10대 사망자수 :',len(age0['survived']==0))
print('10~20대 사망자수 :',len(age1['survived']==0))
print('20~30대 사망자수 :',len(age2['survived']==0))
print('30~40대 사망자수 :',len(age3['survived']==0))
print('40~50대 사망자수 :',len(age4['survived']==0))
print('50~60대 사망자수 :',len(age5['survived']==0))
print('60~70대 사망자수 :',len(age6['survived']==0))
print('70~80대 사망자수 :',len(age7['survived']==0))

