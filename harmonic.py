
limit = int(input(" num limit : "))

def harmonic(limit):
    if limit == 0:
        return 1
    else :
        return limit * harmonic(limit - 1)

for x in range(limit):
    print("Limit,Value = ", x + 1,harmonic( x + 1))
    

           