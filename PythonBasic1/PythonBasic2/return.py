# Return

def sum(num1, num2):
   
    return num1 + num2

# Should do one thing really well.
# Should return something.

total = sum(4,5)
print(sum(4,total))
print(sum(4, sum(4,5)))

# ....................................................................

def sum(n1, n2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(n1, n2)

total =  sum(10,20)
print(total)