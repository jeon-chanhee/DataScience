
# coding: utf-8

# In[5]:


# *가 있으면 튜플로 받아들여 여러 인자를 받을 수 있다.

def add_many(*args):
    result=0
    cnt=0
    print(args)
    for i in args:
        print(i, end='\t')
        result=result+i
    return result

result1 = add_many(1,2)
print('=>합 %d' % result1)
print('-'*20)

result2 = add_many(1,2,3)
print('=>합 %d' % result2)
print('-'*20)

