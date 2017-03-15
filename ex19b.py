# In Reference to the great show Married with Children
def playboys_and_hooters(hooter_pairs_count, playboys_count):
    print "You have %d hooters!" % float(hooter_pairs_count * 2)
    print "You have %d playboys!" % float(playboys_count)
    print "Hehehe, PLAYBOYS! HOOTERS! PLAYBOYS! HOOTERS! *drools*"

h = float(raw_input("How many hooters: "))
p = float(raw_input("How many playboys: "))
print "You typed %r hooters and %r playboys" % (h, p)
playboys_and_hooters(h, p)

