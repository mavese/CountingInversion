#Matthew Mantese

from collections import deque
import itertools

def mergeandcount(lft,rgt):
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """
    i = len(lft) - 1
    j = len(rgt) - 1
    lft.reverse()
    rgt.reverse()
    x = len(lft)
    inv = 0
    rls = []
    while lft and rgt:
        if rgt[j] < lft[i]:
            inv += x
            item = rgt.pop()
            for i in range(x):
                print '{} conflicts with {}'.format(lft[i], item)
            rls.append(item)
            j -= 1
        else:
            x -= 1
            rls.append(lft.pop())
            i -= 1
    lft.reverse()
    rgt.reverse()
    rls.extend(lft or rgt)
    return (inv, rls)


def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    if len(seq) <= 1:
        return (0, seq)

    mid = len(seq)/2
    lft = seq[:mid]
    rgt = seq[mid:]
    inv1, lft = sortandcount(lft)
    inv2, rgt = sortandcount(rgt)
    inv3, whole = mergeandcount(lft, rgt)
    return (inv3 + inv2 + inv1, whole)


    

if __name__ =="__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (5,"Cake: I Will Survive"),
             (6,"Aretha Franklin: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs2 = [(3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (8,"Coldplay: Clocks"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs3 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (10,"Garth Brooks: Friends in Low Places"),
             (9,"Nickelback: Gotta be Somebody")]
    print seq1
    print "# Inversions: %i\n" %sortandcount(seq1)[0]
    print seq2
    print "# Inversions: %i\n" %sortandcount(seq2)[0]
    print seq3
    print "# Inversions: %i\n" %sortandcount(seq3)[0]
    print songs1
    print "# Inversions: %i\n" %sortandcount(songs1)[0]
    print songs2
    print "# Inversions: %i\n" %sortandcount(songs2)[0]
    print songs3
    print "# Inversions: %i\n" %sortandcount(songs3)[0]
