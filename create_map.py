import sys

with open(sys.argv[3], "w") as f:
	f.write("[[1, "+"1, "*(int(sys.argv[1])-2)+"1],\n")
	f.write((" [1, "+"0, "*(int(sys.argv[1])-2)+"1],\n")*(int(sys.argv[2])-2))
	f.write(" [1, "+"1, "*(int(sys.argv[1])-2)+"1]]")