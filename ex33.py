numbers = []

def loop(rounds):
    i = 0
    while i < rounds:
        print "At the top i is %i" % i
        numbers.append(i)
        i += 1
        #print "Rounds: %i" % rounds
        print "Numbers now: ", numbers
        print "At the bottom i is %i" % i

def loop_for(rounds):
    for x in range(0, rounds):
        numbers.append(x)
        print "Number is : %i" % x

#while i < 6:
    #print "At the top i is %d" % i
    #numbers.append(i)

    #i += 1
    #print "Numbers now: ", numbers
    #print "At the bottom i is %d" % i

loop_type = int(raw_input("1 While Loop\n2 For Loop\nAuswahl: "))
count = int(raw_input("How often: "))
if loop_type == 1:
    loop(count)
elif loop_type == 2:
    loop_for(count)
else:
    print "Wrong entry"


#print "Literally variable numbers: %d" % numbers
print "The numbers: "

for num in numbers:
    print num
