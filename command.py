import sys
file=open(sys.argv[1])
data=file.read()
words=data.split()
print("Total words:",len(words))
python command.py py.txt