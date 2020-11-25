n = int(input("Enter a number"))
nmin = int(input("Enter a min"))
nmax = int(input("Enter a max"))
for i in range(nmin, nmax+1):
    if i**n in range(nmin,nmax+1):
        print(i)