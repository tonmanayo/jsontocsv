import csv
import json
import pprint
import glob


def dynamicPrint(fileName, outputFile):
    items = {'id': str(i)}
    if fileName in inputFile.keys():
        for value in inputFile[fileName]:
            for key1, val1 in value.items():
                try:
                    items[key1] = items[key1] + "\n" + val1
                except KeyError:
                    items[key1] = val1
    writer = csv.DictWriter(outputFile, fieldnames=items.keys())
    if i == 0:
        writer.writeheader()
    writer.writerow(items)

miOutputFile = open('misc.csv', 'w')
edOutputFile = open('education_and_training.csv', 'w')
exOutputFile = open('extracurricular.csv', 'w')
crOutputFile = open('credibility.csv', 'w')
awOutputFile = open('awards.csv', 'w')
acOutputFile = open('accomplishments.csv', 'w')
skOutputFile = open('skills.csv', 'w')

#outputFile = open('test.csv', 'w')
wxOutputFile = open('workExperience.csv', 'w')
bOutputFile = open('basic.csv', 'w')

fileList = glob.glob('jsonFiles/*.json')
i = 0
pprint.pprint(fileList)
for file in fileList:
    f = open(file, 'r')
    inputFile = json.load(f)
    f.close()

    emails = ""
    gender = ""
    title = ""
    firstName = ""
    middleName = ""
    surname = ""
    education = {}
    phone = ""
    url = ""
    workExperience = [{}]
    #pprint.pprint(inputFile)
    if 'basics' in inputFile.keys():
        bFieldNames = ['id', 'firstName', 'middleName', 'surname', 'gender', 'email', 'phone', 'url', 'title']

        for key, val in inputFile['basics'].items():

            if key == 'gender':
                gender = val
            elif key == 'title':
                title = val
            elif key == 'name':
                for key, val in val.items():
                    if key == 'firstName':
                        firstName = val
                    elif key == 'middleName':
                        middleName = val
                    elif key == 'surname':
                        surname = val
            elif key == 'email':
                for email in val:
                    emails += "\n" + email
            elif key == 'phone':
                for pho in val:
                    phone += "\n" + pho
            elif key == 'url':
                for url1 in val:
                    url += "\n" + url1

        writer = csv.DictWriter(bOutputFile, fieldnames=bFieldNames)
        if i == 0:
            writer.writeheader()
        writer.writerow({'id': i,
                         'firstName': firstName,
                         'middleName': middleName,
                         'surname': surname,
                         'gender':gender,
                         'email': emails,
                         'phone': phone,
                         'url': url,
                         'title': title})

    dynamicPrint('misc', miOutputFile)

    dynamicPrint('education_and_training', edOutputFile)

    dynamicPrint('extracurricular', exOutputFile)

    dynamicPrint('credibility', crOutputFile)

    dynamicPrint('awards', awOutputFile)

    dynamicPrint('accomplishments', acOutputFile)

    dynamicPrint('skills', skOutputFile)

    wxFieldNames = ['id', 'date_start', 'jobtitle', 'organization', 'date_end', 'text']
    writer = csv.DictWriter(wxOutputFile, fieldnames=wxFieldNames)
    if i == 0:
        writer.writeheader()
    date_start = ""
    jobtitle = ""
    organization = ""
    date_end = ""
    text = ""
    if 'work_experience' in inputFile.keys():
        for work in inputFile['work_experience']:
            for key, val in work.items():
                if key == 'date_start':
                    date_start = val
                elif key == 'jobtitle':
                    jobtitle = val
                    workExperience.append({key: val})
                elif key == 'organization':
                    organization = val
                elif key == 'date_end':
                    date_end = val
                elif key == 'text':
                    text = val
            writer.writerow({'id': i,
                             'date_start': date_start,
                             'jobtitle': jobtitle,
                             'organization': organization,
                             'date_end': date_end,
                             'text': text})
    i = i + 1
#
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# newRows = [dicFields]
# newRows.append(dicFields)
#
#
# print(newRows[1])
#
# names = ['tony', 'mack', 'has', 'three']
#
# writer.writeheader()
#
# #writer.writerow({'ID': '1', 'first name': names, 'last name': 'mack'})
# #writer.writerow({'ID': '2', 'last name': 'Beans'})
# #writer.writerow({'ID': '3', 'last name': 'Spam'})
# writer.writerows(newRows)
