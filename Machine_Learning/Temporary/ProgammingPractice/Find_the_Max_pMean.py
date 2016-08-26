#https://www.careercup.com/page?pid=yahoo-interview-questions
array=[10,4,50]


def find_max_p_mean(array):
    sorted_array=sorted(array)
    print (sorted_array)
    sum=0
    for i in range(len(sorted_array)):
        sum += (i)*sorted_array[i]
        print (sum)
    print (sum)


find_max_p_mean(array)
