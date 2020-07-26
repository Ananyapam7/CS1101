m = int(input("m = "))
def sum_mth_power_list(x):
    store = 0.0
    for i in x:
        store += i**m
    return store


x = [3,2,4,1,9,8,6,0]    

print sum_mth_power_list(x)
