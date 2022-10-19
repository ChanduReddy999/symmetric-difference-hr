"""symmetric difference of two sets in Python(HackerRank Problem)"""
'''method 1'''

# a,b = [set(input().split()) for _ in range(4)][1::2]
# print('\n'.join(sorted(a^b, key=int)))

'''method 2'''

# m = int(input())
# m_str = input()

# n = int(input())
# n_str = input()

# m_set = set(map(int, m_str.split(' ')))
# n_set = set(map(int, n_str.split(' ')))

# my_set = set()
# my_set.update(m_set)
# my_set.update(n_set)

# intersection = m_set.intersection(n_set)

# for i in intersection:
#     my_set.remove(i)
    
# my_set = sorted(list(my_set))

# for n in my_set:
#     print(n)