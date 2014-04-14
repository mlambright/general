import csv, sys

colname = str(sys.argv[1])
infilename = sys.argv[2]
outfilename = sys.argv[3]
dictlist = []

with open(infilename, 'r') as infile:
  drobject = csv.DictReader(infile)
  for row in drobject:
    print row
    dictlist.append(row)
  headers = drobject.fieldnames
  
with open(outfilename,'w') as outfile:
  dwobject = csv.DictWriter(outfile,fieldnames=headers)
  dwobject.writeheader()
  for row in dictlist:  
    if colname in headers:
      row[colname] = "'" + str(row[colname])
      dwobject.writerow(row)
    else:
      raise Exception("column name does not exist in file")

print colname,"converted to text and new file located at",outfilename 

