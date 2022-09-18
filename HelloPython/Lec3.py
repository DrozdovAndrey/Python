# list_nums = [i for i in range(1,21) if i%2 == 0]
# list_nums = [(i,i**2) for i in range(1,21) if i%2 == 0]
# list_nums = [i**2 for i in range(1,21) if i%2 == 0]

# print(list_nums)

# list_nums = [(i,i**2) for i in [1,2,3,5,8,15,23,38] if i%2 == 0]
# print(list_nums)

# def select(f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# li = [x for x in range(1,21)]
# print(li)
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = list(map(int, '1 2 3 4 5'.split()))
# print(data)
# for e in data:
#     print(e*10)




# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# users = ['user1','user2','user3','user4','user5']
# ids = [4,5,9,14,7]
# data = list(zip(ids, users))
# print(data)

# users = ['user1','user2','user3','user4','user5']
# data = list(enumerate(users))
# print(data)