# # # Bubble Sort
# # def _long_list(anylist):
# #     len_list = len(anylist)  # THis will give the leng of the list
# #     new_list = anylist
# #     for k in range(1, len_list - 1):
# #         for idx in range(0, len_list - 1):
# #             if new_list[idx] > new_list[idx + 1]:
# #                 new_list[idx], new_list[idx + 1] = new_list[idx + 1], new_list[idx]


# #     return new_list


# # a = [2, -33, 100, 3000]

# # x = _long_list(a)
# # print(x)
# def two_list(A,B):	
# 	list_new = A.append(B)
# 	return list_new

# list1 =[5,6,7,12]
# list2= [3,4,12,7]

# x= two_list(list1,list2)
# print(x)


# def functioi(list1):

# 	new_lis = list1[1:-1]
# 	return new_lis
# B= [2,3,5,6]
# x= functioi(B)
# print(x)


# def add_odd(LongList):
#     lenghtoflist =len(LongList)
#     new_list =[]
#     for eachvalue in LongList:
#         if eachvalue % 2 == 0:
#             new_list.append(eachvalue)
#         elif eachvalue % 2 != 0:
#             eachvalue = eachvalue +1
#             new_list.append(eachvalue)
#     return new_list

# input_list = [12, 3, 4, 5, 6]
# x= add_odd(input_list)
# print(x)



def _sum_odd(firstlist,secondlist):
 	firstlist.extend(secondlist)
 	sum_odd_number =0
 	for eachnumber in firstlist:
 		if eachnumber % 2 != 0:
 			sum_odd_number = sum_odd_number + eachnumber
 	return sum_odd_number
one =[2,3,5]
two= [6,7,2]
x = _sum_odd(one,two)
print(x)


# def unique_list(nonuniquelist):
#     new_lis =[]
# 	for eachnumber in nonuniquelist:
# 		if eachnumber not in new_lis:
# 			new_lis.append(eachnumber)
# 	return new_lis

# def function_two_list(ListA,ListB):
#     new_lis =[]
#     for eachnumber in ListA:
#         if eachnumber not in new_lis:
#             new_lis.append(eachnumber)
#     for morenumbers in ListB:
#         if morenumbers not in new_lis:
#             new_lis.append(morenumbers)
#     return new_lis


# user_number= int(raw_input("Please Enter a Number: "))
# y=1
# while y <= user_number:
# 		print('*' * user_number)
# 		y=y+1

# def charaterpuke(x):
# 	x = print(ord(x))
# 	return x


# Print Letter backwar
#def _word(y):
#	sub_str =''
#	for eachleter in y:
#		sub_str = eachleter + sub_str
#	return sub_str


#print("Enter a word , I will print the word backwars!! Isnt that cool?????")
#word= raw_input("Enter the word: ")
#x= _word(word)
#print("Look at this cool stuff: ",x)










