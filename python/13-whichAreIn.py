def in_array(array1, array2):
    r = []
    for i in array1:
        for j in array2:
            if i in j:
                r.append(i)
    return sorted(list(set(r)))

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))
