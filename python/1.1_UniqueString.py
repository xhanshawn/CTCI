# verify if a string has all unique characters.
def isUnique1(s):
	return s and len(s) <=128 and len(s) == len(set(list(s)))
def isUnique2(s):
	if(not s or len(s) > 128): return False
	has = set()
	for c in s:
		if(c in has): return False
		else: has.add(c)
	return True
slong = ""
for i in xrange(128): slong += str(chr(i))
print isUnique1(slong)
print isUnique2(slong)
# this is for testing how to merge