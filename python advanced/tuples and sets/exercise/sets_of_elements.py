n, m = input().split(' ')

n_set = set()
m_set = set()

for i in range(int(n)):
    n_set.add(int(input()))

for i in range(int(m)):
    m_set.add(int(input()))

unique_set = n_set.intersection(m_set)

[print(num) for num in unique_set]