N = int(input())
calls = list(map(int, input().split()))
y_cost = 0
m_cost = 0

for call in calls:
    y_time = (call // 30) + 1
    m_time = (call // 60) + 1

    y_cost += 10 * y_time
    m_cost += 15 * m_time

if y_cost < m_cost:
    print(f'Y {y_cost}')
elif y_cost > m_cost:
    print(f'M {m_cost}')
else:
    print(f'Y M {y_cost}')
