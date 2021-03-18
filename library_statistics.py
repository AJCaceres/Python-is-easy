

import statistics as s

list1= [1,8,10,12,15,16]
list2= [5.5,6.22,8.14,10.72]
list3= [40,60]
list4= [1,2,3,3,5,7]
list5= "aaaaabbbbcccccddddddffffffgghhiii"

mean1 = s.mean(list1)

print(s.mean(list1))
print(s.fmean(list2))
print(s.harmonic_mean(list3))
print(s.median(list1),s.median(list2),s.median(list3))
print(s.mode(list4))
print(s.multimode(list5))
print(s.variance(list1,mean1))
print(s.quantiles(list2,n=4))
