import matplotlib.pyplot as plt
import random

print('Welcome to the Collatz Sequence Generator!')
print('Select a number:')
n = input()
q = n
seq=[]
tst = 1
if n==1:
    print('q')
else:
    while int(n) != 1:
        seq.append(int(n))
        if int(n) %2 == 0:
            n = int(n)/2
        else:
            n=3*int(n) +1
        tst = tst + 1
if len(seq) > 20:
    print("A sample from the Collatz Sequence for the number " + str(q) + " is:")
    print ([ seq[i] for i in sorted(random.sample(range(len(seq)), 20)) ], end = "")
    print(",")
else:
    print("The Collatz Sequence for the number " + str(q) + " is:")
    print(seq, end = "")
    print(",")
print("with a total stopping time of " + str(tst) + ",")
if q == 1:
    print("T")
else:
    print("the peak of the sequence being " + str(max(seq))+".")
plt.plot(seq)
plt.show()

# git test 
