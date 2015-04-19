def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:
        print("ITEMS",items)
        print ("1")
        mid = len(items) / 2        # Determine the midpoint and split
        left = items[0:mid]    
        print("2")
        right = items[mid:]
        print("LEft2", left)
        print("right2", right)
        merge_sort(left)    
        print("22")        # Sort left list in-place
        merge_sort(right)
        print("3")           # Sort right list in-place
        print("LEft", left)
        print("right", right)

        l, r = 0, 0
        for i in range(len(items)): 
            print ("length",len(items))
            # Merging the left and right list
            print("4")
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None
            print ("r", r)
            print("l", l)
            print ("left",left)
            print("right",right)
            print("rval", rval)
            print("lval", lval)
            print("5")
            if (lval and rval and lval < rval) or rval is None:
                print("6")
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                print("7")
                items[i] = rval
                r += 1
            else:
                print("8")
                raise Exception('Could not merge, sub arrays sizes do not match the main array')
            print("item[i]",items[i])
            print("items",items)
            print("9")
        print("10")
    print("11")            
    return items            


alist = [54,26,93,17,77,31,44,55]
print(merge_sort(alist))
           
               