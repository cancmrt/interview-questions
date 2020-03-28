import pageparser
import tableparser
import csv
import re


pageList = ["https://solidshape-interview.s3-us-west-1.amazonaws.com/morseys.html","https://solidshape-interview.s3-us-west-1.amazonaws.com/scoop.html"]
               
for p in pageList:

    # Page class getting page content and extract title as a pageName
    page = pageparser.Page(p)

    #Beatifullsoap rule definitions
    defRules = []
    defRules.append(pageparser.DefinitionSelector("p",{"class":"address"}))
    defRules.append(pageparser.DefinitionSelector("p",{"class":"description"}))
    #Extract infos from content based on beatifullsoap find rules
    infos = page.GetDefinitions(defRules)

    #Extract infos from string
    pageTitle = page.PageName
    pageFullAddress = infos[0].strip()
    pageDescription = infos[1].strip()

    pageTelephone = re.findall(r'\d+', pageDescription)
    pageTelephone = "".join(pageTelephone)

    pageAddressSplited = pageFullAddress.split(",")
    pageCity = pageAddressSplited[1].strip()
    pageState = pageAddressSplited[2].strip().split(" ")[0].strip()

    #Taking Page class and then parsing table to readable columns and rows matrix
    te = tableparser.TableEngine(page)
    extractedTable = te.Tables[0]
    
    #Write to tsv ( sory i didn't look at performance concerns here :( )
    with open(pageTitle+".tsv", "wt") as out_file:
        tsvWrite = csv.writer(out_file, delimiter='\t')
        tsvWrite.writerow(["Shop","City","State","Phone","Flavor","Type","Price"])
        for i in range(0,len(extractedTable.Rows)):
            for j in range(0,len(extractedTable.Columns)):
                if extractedTable.Rows[i][j] != "":
                    tsvWrite.writerow([pageTitle,pageCity,pageState,pageTelephone,extractedTable.Columns[j],extractedTable.RemovedLeft[i],extractedTable.Rows[i][j]])





