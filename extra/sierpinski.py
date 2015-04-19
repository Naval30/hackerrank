
def sierpinski(n):
    d = ["*"]
    for i in xrange(n):
        sp = " " * (2 ** i)
        d = [sp+x+sp for x in d] + [x+" "+x for x in d]
    return d
	

print sierpinski(3)
#print sierpinski(6)

#print "\n".join(sierpinski(6))

