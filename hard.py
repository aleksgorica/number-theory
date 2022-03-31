from partitions import list_partitions
"""
def hard(arr, count, index, limit_count):
    if (count == limit_count):
        print(arr)
        return 
    if (index == len(arr)): return
    if (count > limit_count): return
    for i in range(len(arr)):
        n_terica =
        for j in range(arr[0]+1):
            current = 
            arr[index] 

"""

def splitable(nterica, idx):
    if (nterica[idx] == 0):
        return False
    if (nterica[idx] == 1):
        for i in range(len(nterica)):
            if i == idx: continue
            if nterica[idx] != 0: return True
        return False
    return True

def split_compositions(cur_composition, idx):
    for x in cur_composition:
        if not splitable(x, idx):
            continue
        particije = list_partitions(x[idx])
        for particija in particije:
            
            cur_composition.append()



def compositions(cur_composition, idx):
    if idx >= len(cur_composition[0]):
        return 
    for x in cur_composition:
        if not splitable(x, idx):
            continue
        compositions(split_compositions(cur_composition, idx), idx+1)

exponents = [3]
vsota = sum(exponents)

arr = [[0]*len(exponents)]*vsota
print(arr)
















"""bom sou kar k primeru, mas array, arr = [2, 1, 3], ti pa hoces dubit vse kombinacije al karkoli je to. 
    {[1, 0, 0], []
[(a_11, a_12, ..., a_1n), (a_21, a_22, a_23, ..., a_2n), ()]
ustvaris [(a_n)]*sum(exponents)
count = 0 --> count = sum
if (count == sum) return

"""
"""imas [2, 1], kako izpisat vse mozno:
[(1, 0), (1, 0), (0, 1)], [(2, 0), (0, 1)], [(1, 0), (1, 1)], [(2, 1)]

[2, 2]
[(1, 0), (1, 0), (0, 1), (0, 1)
(2, 0), (0, 1), (0, 1)
(1, 0), (1, 0), (0, 2)
()]


"""
