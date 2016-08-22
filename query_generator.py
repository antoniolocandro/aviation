

list = ['TADPO','INT_1','URIOS','EMUSI']

query=''

for e in list:
    query+= '"designator" = "%s" OR '%(e)

print query