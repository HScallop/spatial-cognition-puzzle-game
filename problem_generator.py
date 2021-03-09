#random choose 1 to 6 objects from 6 classifications
import random
import itertools
#p for prism c for corn

#find all possibilities with sum of n
def possibilities(n):
    list1=itertools.combinations_with_replacement(range(n+1),5)
    rlist=[x for x in list1 if sum(x)==n]
    return rlist

#find all possibilities with sum of n in product of c and p
def c_p_possibilities(n):
    rlist=[]
    for i,j in zip(range(n+1),range(n,-1,-1)):
        if i==j:
            temp=itertools.combinations_with_replacement(possibilities(i),2)
            print('asdf')
            print(i,j)
        else:
            temp=itertools.product(possibilities(i),possibilities(j))
        rlist.extend(temp)
    return rlist
    
def encode(classification,num):
    rstr=''
    if num==0:
        return rstr
    sample=random.sample(range(10),num)
    for i in range(num):
        rstr+='{:02d}{:02d}'.format(classification,sample[i])
    return rstr

def add_ans(prob,f5,l5):
    ans_type=random.choices(['c','s','n'],[2,1,1])
    if ans_type[0]=='c':
        print('c')
        n=random.choice(range(len(prob)//4))
        ans=prob[4*n:4*n+4]
        rstr=ans+prob
        return rstr
    if ans_type[0]=='s':
        print('s')
        n=random.choice(range(len(prob)//4))
        ans=prob[4*n:4*n+2]
        while(prob.find(ans)!=-1):
            ans=ans[0:2]+'{:02d}'.format(random.choice(range(10)))
        rstr=ans+prob
        return rstr
    if ans_type[0]=='n':
        print('n')
        n=random.choice(range(10))
        f5=f5+l5
        while(f5[n]!=0):
            n=random.choice(range(10))
        ans=encode(n,1)
        rstr=ans+prob
        return rstr

counter=0
problem_list=[]
problems=''
for N in range(1,8):
    problem_list.extend(c_p_possibilities(N))
with open('problem_type','a') as typ:
    with open('problems_B.txt','a') as fb:
        with open('problems_A.txt','a') as fa:
            for item in problem_list:
                counter+=1
                litem0=list(item[0])
                litem1=list(item[1])
                random.shuffle(litem0)
                random.shuffle(litem1)
                print(litem0,litem1)
                print(litem0,litem1,file=typ)
                for i in range(5):
                    if litem0[i]!=0:
                        problems+=encode(i,litem0[i])
                    if litem1[i]!=0:
                        problems+=encode(i+5,litem1[i])
                print(problems)
                problems=add_ans(problems,litem0,litem1)
                print(problems)
                if counter%2==1:
                    print(problems,file=fa)
                    print('A')
                else:
                    print(problems,file=fb)
                    print('B')
                problems=''
print(len(problem_list))
