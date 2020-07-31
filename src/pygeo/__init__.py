#print(f"Hello  {__name__}! ")

# first it was only the above the print statement but if I change something in it such as the print command below it will be auto updated.

#print(f"Hello  {__name__}! , Hey ,It's a nice day ,isn't it ? ")
# now we can you function in package
#GREETING = f"Hello, {__name__}! ,its a nice day "

#def greet():
#    print(GREETING)

# there are different techniques such as agile development , we will be using test driven development
#i,e you write your test before you write your code
def are_equal(a,b,tolerance=1e-8):
    #return a == b
    if not tolerance >= 0:
        raise ValueError("tolarance must be non-negative")
    return abs(a - b) < tolerance