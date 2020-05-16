# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((new_record,data))
print(np.shape(data))
print(np.shape(census))

age = []

for i in range(len(census)):
    age.append(census[i][0])

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

race_0 = []
race_1 = []
race_2 = []
race_3 = []
race_4 = []


for i in range(len(census)):
    if(int(census[i][2])==0):
        race_0.append(census[i][2])
    if(int(census[i][2])==1):
        race_1.append(census[i][2])
    if(int(census[i][2])==2):
        race_2.append(census[i][2])
    if(int(census[i][2])==3):
        race_3.append(census[i][2])
    if(int(census[i][2])==4):
        race_4.append(census[i][2])
    
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
race_array = np.array([len_0,len_1,len_2,len_3,len_4])
minority_min = np.min([len_0,len_1,len_2,len_3,len_4])


for i in range(4):
    if(race_array[i]==minority_min):
        minority_race = i



senior_citizens = []
for i in range(len(census)):
    if(census[i][0] > 60):
        senior_citizens.append(census[i])

working_hours_sum = 0

for i in range(len(senior_citizens)):
    working_hours_sum += senior_citizens[i][6]

senior_citizens_len = len(senior_citizens)
avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(working_hours_sum)
print(avg_working_hours)


high = []
low  = []
for i in range(len(census)):
    if(census[i][1] > 10):
        high.append(census[i][7])
    if(census[i][1] <= 10):
        low.append(census[i][7])

print(high[4])
print(low[5])
def mean(num):
    zero = 0
    ones = 0
    for i in range(len(num)):
        if(num[i]==0):
            zero +=1
        else:
            ones +=1
    mean = ones/(zero+ones)
    return mean


avg_pay_high = round(mean(high),2)


avg_pay_low = round(mean(low),2)

print(avg_pay_high)
print(avg_pay_low)


