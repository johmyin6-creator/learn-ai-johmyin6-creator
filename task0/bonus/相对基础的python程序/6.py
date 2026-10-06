def num_count(num:list):
    count_dict={}
    for i in num:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    return count_dict
numbers = [1, 2, 1, 3, 2, 1]
print(num_count(numbers))