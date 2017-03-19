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

#while i < 6:
    #print "At the top i is %d" % i
    #numbers.append(i)

    #i += 1
    #print "Numbers now: ", numbers
    #print "At the bottom i is %d" % i

count = int(raw_input("How often: "))
loop(count)


#print "Literally variable numbers: %d" % numbers
print "The numbers: "

for num in numbers:
    print num
