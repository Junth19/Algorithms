# Author : Junth Basnet
# Largest Salary(any Digit Number)
# Solution Strategy : Greedy Algorithm

def IsGreaterOrEqual(salary, maxDigit):
    return int(str(salary) + str(maxDigit)) >= int(str(maxDigit) + str(salary))

def HighestSalary(salary):
    salaryList = []
    while salary != [] :
        maxDigit = 0
        for s in salary:
            if IsGreaterOrEqual(s, maxDigit):
                maxDigit = s
        salaryList.append(maxDigit)
        salary.remove(maxDigit)
    answer = ''.join([str(i) for i in salaryList])
    print(answer)

n = int(input())
salary = [int(i) for i in input().split()]
HighestSalary(salary)





