
# coding: utf-8

# In[1]:


# ** 딕셔너리로 만들어져서 출력
# key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)

