f = open("043.invictus_poem.txt")
for line in f:
    # we could alternately use .strip() or .strip("\n") here
    line = line.rstrip()
	print(line)
f.close()
