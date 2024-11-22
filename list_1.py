'''
input two lists from user.merge these lists into a   third list such that in the
merged list all even numbers occur first followed by odd numbers.both the
even numbers and odd numbers should be in the sorted order
'''
list_1=[2,5,6,7,8]
list_2=[3,23,45]
merged_list=list_1+list_2
even_list=[]
odd_list=[]
for i in merged_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even number list is ",even_list)
print("odd number list is ",odd_list)
even_list.sort()
odd_list.sort()
merged_1_list=even_list+odd_list
print("merged list is ",merged_1_list)



