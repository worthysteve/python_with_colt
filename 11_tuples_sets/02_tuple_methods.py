
#! LOOPING
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
    print(month)

i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1

#! Tuple methods
#* count
#* index

nums = (1,2,3,(4,5), 6,7)
print(nums[3])
print(nums[3][1])