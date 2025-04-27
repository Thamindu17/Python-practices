import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    print("hi") #this is not work because after the return fuction
a,b,c=mean_median_mode([2,4,56,34,78,222,443,90])
print(f"mean is {a} median is {b} mode is {c}")
