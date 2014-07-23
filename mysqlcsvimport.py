import csv, MySQLdb, sys
print sys.argv

statementType = str(sys.argv[1]).lower()
dbname = sys.argv[2]
tablename = sys.argv[3]
filename = sys.argv[4]

if statementType!='update' and statementType!='insert':
  raise Exception("neither update nor insert selected")

db = MySQLdb.connect(db=dbname, read_default_file='~/.my.cnf')
c = db.cursor()

with open(filename) as file:
  input = csv.DictReader(file)
  headers = input.fieldnames
  fields = ''
  for item in headers:
    if len(fields) == 0:
      fields = '`' + str(item) + '`'
    else:
      fields = fields + ', `' + str(item) + '`'
  for item in input:
    values = ''
    for element in headers:
      if len(values) == 0:
        values = '"'+str(item[element].replace('"', "'"))+'"'
      else:
        values = values + ', "' + str(item[element]).replace('"', "'") + '"'
    print item
    query = "insert into {3}.{2} ({0}) values ({1});".format(fields, values, tablename, dbname)
    print query
    c.execute(query)
    db.commit()
