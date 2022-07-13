def add(name):
    print("name is",name)
add(int(3))
#file=open('text.txt', 'r')
#print(file.read())
#print(file.readline())
with open('text.txt','r') as reader:
    #print(reader.readline())
    #for line in reader:
     #   print(line)
    """Line=reader.readline()
    while Line!="":
        print(Line)
        Line=reader.readline()"""
    List = reader.readlines()
    print(List)
    reversed(List)
    with open('text.txt', 'w') as writer:
        for line in reversed(List):
            writer.write(line)
    