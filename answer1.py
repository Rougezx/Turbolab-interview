d1,m1,y1=map(int,input().split(' '))
d2,m2,y2=map(int,input().split(' '))
cost=0
diff_of_day=d1-d2
diff_of_months=m1-m2
diff_0f_year=y1-y2

if diff_of_day==0 and diff_of_months==0 and diff_0f_year==0:
    cost=20
elif diff_of_day>0 and diff_of_months==0 and diff_0f_year==0:
    cost=30*diff_of_day
elif diff_of_day==0 and diff_of_months>0 and diff_0f_year==0:
    cost=1000*diff_of_months
elif diff_of_day==0 and diff_of_months==0 and diff_0f_year>0:
    cost=2000*diff_0f_year
else:
    cost=30*diff_of_day+1000*diff_of_months+2000*diff_0f_year

print(cost)
