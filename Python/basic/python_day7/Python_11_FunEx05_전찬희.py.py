
# coding: utf-8

# In[4]:


# 함수의 결괏값은 언제나 하나! 
# 튜플값 하나인 (a+b,a*b)로 돌려준다. 하나의 값으로!

def add_and_mul(a,b):
    return a+b,a*b

result=add_and_mul(3,4)
print(result)

# 튜플 값을 2개의 결괏값처럼 받고 싶다면,
result1,result2=add_and_mul(3,4)
print(result1,result2)

