InputText = ["754208565333336064","754208580495745024"]
for value in InputText:
 with open('catalina.out', "r") as input:
    for line in input:
        if value in line:
           print line
           x = next(input)
           print(x)
           x = next(input)
           print(x)
