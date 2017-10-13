def mergeandcount(lft,rgt):
    i = 0
    j = 0
    x = len(lft)
    inv = 0
    rls = []
    while len(lft) > i and len(rgt) > j:
        if rgt[j] < lft[i]:
            inv += x
            rls.append(rgt[j])
            j += 1
        else:
            x -= 1
            rls.append(lft[i])
            i += 1
    return(inv, (rls.extend(lft or rgt)))

def sortandcount(seq):
    if len(seq) <= 1:
        return (0, seq)

    mid = len(seq)/2
    lft = seq[:mid]
    rgt = seq[:mid]
    inv1, lft = sortandcount(lft)
    inv2, rgt = sortandcount(rgt)
    inv3, whole = mergeandcount(lft, rgt)
    return(inv1 + inv2 + inv3, whole)


if __name__ == '__main__':
    seq = [2,3,1]
    print sortandcount(seq)