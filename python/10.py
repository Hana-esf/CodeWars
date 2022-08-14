def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    elif n > len(customers):
        return max(customers)
    else:
        total_sum = []
        for i in range(n):
            total_sum.append(customers[i])
        for i in range(n,len(customers)):
            m_i = total_sum.index(min(total_sum))
            total_sum[m_i] += customers[i]
        return max(total_sum)


 