from datetime import date
def SortEmpire(file):
    current_date = date.today()
    f = open(file)
    infile=f.readlines()
    # ARRAY TO STORE ALL YEARS UPTIL NOW AND USE COUNTING SORT TO SORT IN O(N)
    data = [] 
    for i in range(current_date.year):
        data.append([])
    for item in infile: 
        item = item.strip()
        #SPLITING THE DATE AND NAME WITH A COMMA DUE TO FILE OPTIOn
        data = item.split(", ")
        #PUT ITEM IN THE PERFECT POSITION IN OUR LIST
        data[int(data[1])].append(item)
    #ADD ALL ELEMENTS FROM THE ITEMS TO OUR ANSWER
    answer = []
    for item in data:
        if(len(item)>0):
            for x in item:
                answer.append(x)
    return answer
print(SortEmpire("emperors.txt"))