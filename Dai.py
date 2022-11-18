
h1 = int(input("Height : "))
h2 = int(input("Height2 : "))

for i in range(h1):
        print(" " * (h1 - i), "*" * (2*i + 1 ))

for i in range(h1 - 2, -1,-1):
       
        print(" " * (h1 - i), "*" * (2*i + 1 ))

print("\n")

for i in range(h2):
       print(" " * (h2 - i), "*" * (2*i + 1 ))

for i in range(h2 - 2, -1,-1):
         print(" " * (h2 - i), "*" * (2*i + 1 ))
