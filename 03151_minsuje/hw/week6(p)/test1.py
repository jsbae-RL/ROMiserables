import pandas as pd

def data_conversion(reports):
    a =[]
    b =[]
    for report in reports:
        a = list(set(report.split()))
        b.append(a)
    return(b)
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo muzi","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report_data = pd.DataFrame(index=id_list,columns=data_conversion(report))
print(report_data)