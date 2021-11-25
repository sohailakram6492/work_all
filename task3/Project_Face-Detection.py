data_list=['PAKISTAN', 'National Identity Card', 'ISLANIC REPUBLIC OF PAKISTAN', 'Name', 'Saleem Ullah', 'Father Name', 'Ghulam Ullah Usmani', 'cpbicu', 'Gender', 'Country of Stay', 'M', 'Pakistan', 'Identity Number', 'Date of Birth', '35201-5399394-5', '15.01.1996', 'Qraulh', 'Date of Issue', 'Date 0( Expiry', '15,06.2021', '15.06.2031', 'Holae', 'ESenature']
if 'Name' in data_list:
    name = data_list[data_list.index('Name')+1]
if 'Father Name' in data_list:
    father_name = data_list[data_list.index('Father Name')+1]
if list(filter(lambda data_list: '-' in data_list, data_list)):
    Id_Number=list(filter(lambda x: '-' in x, data_list))[0]
try:
        D_O_Birth,D_O_Issue,D_O_Expiry=list(filter(lambda x: '.' in x, data_list))
except:pass

dictnary = {
    "Name": name,
    "Father Name" : father_name,
    "Id_Number" :Id_Number,
    "Date_Of_Birth":D_O_Birth,
    "Date_Of_Issue":D_O_Issue,
    "Date_Of_Exoiry":D_O_Expiry,
}

print(dictnary)