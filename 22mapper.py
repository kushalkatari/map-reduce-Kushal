import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  print(line)    
  datalist = line.strip().split(",")
  print(datalist)
  if (len(datalist) ==7): 
    title,rating,ratingLevel,ratingDescription,releaseyear,userratingscore,userratingsize = datalist
    print(rating)

    # print intermediate key-value pairs to standard output
    print(rating,"\t",1)