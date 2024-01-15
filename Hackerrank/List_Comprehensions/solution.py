# Hackerrank - List Comprehension

# Example Input
x = 1
y = 1
z = 2
n = 3

# Solution as Nested For Loop:

#ls = []
#for i in range(x+1): 
#    print("This is x ", i)
#    for j in range(y+1):
#        print("This is y ", j)
#        for k in range(z+1):
#            print("This is z ", k)
#            if i+j+k != n:
#                ls.append([i, j, k])
#                print(ls)

# Solution as List Comprehension: 
# Note: Put the operation in the beginning (what you want the output to be).

ls = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(ls)