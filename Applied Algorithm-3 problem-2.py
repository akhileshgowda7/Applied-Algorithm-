#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse


def f(*x,**y):
    def s1(x):
        s=0
        if x:
            for i in x:
                s+=i
        return s
    
    def p1(x):
        s=1
        if s:
            for i in x:
                s*=i
        return s
    
    def rs1(x):
        reciprocal=map(lambda x:1/x,x)
        return s1(reciprocal)
        
    
    if y["action"]=="sum":
        return s1(*x)
    elif y["action"]=="prod":
        return p1(*x)
    elif y["action"]=="reciprocal sum":
        return rs1(*x)
    else:
        print("bad argument:{}".format(y))
        
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-lst', nargs='+', default=['1'],help="List of numbers",type=int)
    parser.add_argument('-op', default=sum,help="sum,prod,reciprocal sum",type=str)
    args=parser.parse_args()
    
    print(f(args.lst,action=args.op))

       
    
    
        
                            


            


# In[ ]:




