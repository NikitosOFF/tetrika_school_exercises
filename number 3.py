# def get_zeros(n):
#     result = factorial(n)
#     count = 0
#     while result % 10 == 0:
#         result = result // 10
#         count += 1
#     return count
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(get_zeros(5))
# print(get_zeros(12))
# print(get_zeros(125))


def get_zeros(n):
    count = 0
    while n != 0:
        n = n // 5
        count += n
    return count


print(get_zeros(5))
print(get_zeros(12))
print(get_zeros(130))
