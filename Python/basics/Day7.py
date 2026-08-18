#multiplication table

# def print_table(n, i):
#     if(i==11):
#         return
#     else:
#         print("%d * %d = %d" %( n, i , n*i))
#         print_table(n, i+1) 

# print_table(5,1)

# Sum of naturals

# def sum_of_naturals():
#     n = int(input())
#     i=1
#     sum=0
#     if n==0:
#             print("0")
#     else:
#             while i<=n:
#                 sum =sum+i
#                 i=i+1
#             print(sum)
# sum_of_naturals()

# Sum of squares of first natural numbers
def sum_of_naturals():
    n = int(input())
    i=1
    sum=0
    while i<=n:
                sum=sum+(i**2)
                i=i+1
    print(sum)

sum_of_naturals()
