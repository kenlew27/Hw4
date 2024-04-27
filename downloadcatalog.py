import requests
import pandas as pd
from bs4 import BeautifulSoup

startinglink = "http://collegecatalog.uchicago.edu/thecollege/"

dfsolution = pd.DataFrame({"Course Number": [] , "Description": [], "Instructor": [], "Terms": [], "Equivalent Courses": [], "PreReq": []})
dfdepartment = pd.DataFrame({"Code": [] , "Number of Courses": []})

dep = ["anthropology/" ,
 "architecturalstudies/#" , 
 "arthistory/" , 
 "astronomyastrophysics/" , 
"biologicalchemistry/",
"biologicalsciences/",
"chemistry/",
"cinemamediastudies/",
"classicalstudies/",
"cognitivescience/",
"comparativehumandevelopment/",
"comparativeliterature/",
"caam/",
"computationalsocialscience/",
"computerscience/",
"creativewriting/",
"comparativeraceethnicstudies/",
"datascience/",
"democracystudies/",
"digitalstudies/",
"eastasianlanguagescivilizations/",
"economics/",
"educationandsociety/",
"englishlanguageliterature/",
"environmentalscience/",
"environmentalstudies/",
"cegu/",
"fundamentalsissuesandtexts/",
"genderstudies/",
"geographicalstudies/",
"geophysicalsciences/",
"germanicstudies/",
"globalstudies/",
"healthandsociety/",
"history/",
"scienceandmedicinehips/",
"humanrights/",
"inequalityandsocialchange/",
"Inquiryresearchhumanities/",
"jewishstudies/",
"latinamericanstudies/",
"lawlettersandsociety/",
"linguistics/",
"mathematics/",
"MediaArtsandDesign/",
"medievalstudies/",
"molecularengineering/",
"music/",
"neareasternlanguagescivilizations/",
"neuroscience/",
"norwegianstudies/",
"philosophy/",
"physics/",
"politicalscience/",
"psychology/",
"publicpolicystudies/",
"quantitativesocialanalysis/",
"rdin/",
"religiousstudies/",
"renaissancestudies/",
"romancelanguagesliteratures/",
"slaviclanguagesliteratures/",
"sciencecommunicationpublicdiscourse/",
"sociology/",
"southasianlanguagescivilizations/",
"statistics/",
"theaterperformancestudies/",
"visualarts/",
"yiddish/",
]


def catalog(departmentlink):
    eachdepartment= startinglink + departmentlink
    department = requests.get(eachdepartment)
    soup = BeautifulSoup(department.text, "lxml")
    numberlist = []
    desclist = []
    instructorlist = []
    termslist = []
    equivlist = []
    prereqlist = []

    extraindex = []
    name = ""
    coursetitle = soup.find_all("p", class_ = "courseblocktitle")
    for n,i in enumerate(coursetitle):
        title = i.text
        title  = title.replace('\xa0',' ')
        title = title.split('.')[0]
        if "-" not in title:
            numberlist.append(title)
        else:
            extraindex.append(n)
        title = title.split(' ')
        name = title


    coursedesc = soup.find_all("p", class_ = "courseblockdesc")
    for i in coursedesc:
        desc = i.text
        desclist.append(desc)
    desclist = [i for j, i in enumerate(desclist) if j not in extraindex]

    unbrokendetail = []
    coursedetail = soup.find_all("p", class_ = "courseblockdetail")
    for i in coursedetail:

            #instructors
        detail = i.text
        detail  = detail.replace('\xa0',' ')
        #detail  = detail.replace('Instructor(s):','*')
        detail  = detail.replace('Terms Offered:','*')
        detail  = detail.replace('Equivalent Course(s):','*')
        detail  = detail.replace('Note(s):','*')
        detail  = detail.replace('Prerequisite(s):','*')
        detail = detail.rstrip()
        detail = detail.split('*')
        for n, val in enumerate(detail):
            detail[n]=val.replace('\n','')
            detail[n] = detail[n].rstrip()
        detail = list(filter(None, detail))
        for val in detail:
            if "Instructor(s):" in val:
                instructorlist.append(val.split("Instructor(s):",1)[1])
        if not any("Instructor(s):" in x  for x in detail):
            instructorlist.append("null")

            #Terms
        detail = i.text
        detail  = detail.replace('\xa0',' ')
        detail  = detail.replace('Instructor(s):','*')
        #detail  = detail.replace('Terms Offered:','*')
        detail  = detail.replace('Equivalent Course(s):','*')
        detail  = detail.replace('Note(s):','*')
        detail  = detail.replace('Prerequisite(s):','*')
        detail = detail.rstrip()
        detail = detail.split('*')
        for n, val in enumerate(detail):
            detail[n]=val.replace('\n','')
            detail[n] = detail[n].rstrip()
        detail = list(filter(None, detail))

        if not any("Terms Offered:" in x  for x in detail):
            termslist.append("null")
        else:
            for val in detail:
                if "Terms Offered:" in val:
                    termslist.append(val.split("Terms Offered:",1)[1])

            #Equiv
        detail = i.text
        detail  = detail.replace('\xa0',' ')
        detail  = detail.replace('Instructor(s):','*')
        detail  = detail.replace('Terms Offered:','*')
        #detail  = detail.replace('Equivalent Course(s):','*')
        detail  = detail.replace('Note(s):','*')
        detail  = detail.replace('Prerequisite(s):','*')
        detail = detail.rstrip()
        detail = detail.split('*')
        for n, val in enumerate(detail):
            detail[n]=val.replace('\n','')
            detail[n] = detail[n].rstrip()
        detail = list(filter(None, detail))

        if not any("Equivalent Course(s):" in x  for x in detail):
            equivlist.append("null")
        else:
            for val in detail:
                if "Equivalent Course(s):" in val:
                    equivlist.append(val.split("Equivalent Course(s):",1)[1])

            #Prereq
        detail = i.text
        detail  = detail.replace('\xa0',' ')
        detail  = detail.replace('Instructor(s):','*')
        detail  = detail.replace('Terms Offered:','*')
        detail  = detail.replace('Equivalent Course(s):','*')
        detail  = detail.replace('Note(s):','*')
        #detail  = detail.replace('Prerequisite(s):','*')
        detail = detail.rstrip()
        detail = detail.split('*')
        for n, val in enumerate(detail):
            detail[n]=val.replace('\n','')
            detail[n] = detail[n].rstrip()
        detail = list(filter(None, detail))

        if not any("Prerequisite(s):" in x  for x in detail):
            prereqlist.append("null")
        else:
            for val in detail:
                if "Prerequisite(s):" in val:
                    prereqlist.append(val.split("Prerequisite(s):",1)[1])


    #print(len(numberlist))
    #print(len(desclist))
    #print(len(instructorlist))
    #print(len(termslist))
    #print(len(equivlist))
    #print(len(prereqlist))

    #print((numberlist))
    #print(desclist)
    #print(len(instructorlist))
    #print(len(termslist))
    #print(len(equivlist))
    #print(len(prereqlist))

    df = pd.DataFrame({"Course Number": numberlist , "Description": desclist, "Instructor": instructorlist, "Terms": termslist, "Equivalent Courses": equivlist, "PreReq": prereqlist})
    dfdep = pd.DataFrame({"Code": [name] , "Number of Courses": [len(numberlist)]})
    return (df, dfdep)


for departments in dep:
    dfsolution = pd.concat([dfsolution, catalog(departments)[0]], ignore_index=True)
    dfdepartment = pd.concat([dfdepartment, catalog(departments)[1]]  , ignore_index=True) 


dfsolution.to_csv('catalog.csv')
dfdepartment.to_csv('department.csv')



















   


    





    






#print(dfsolution)
#df.to_csv("catalog.csv")





