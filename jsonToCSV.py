import csv
import json
import pprint
import glob
import collections


def dynamicPrint(fileName, outputFile, items):
    if fileName in inputFile.keys():
        for value in inputFile[fileName]:
            for key1, val1 in value.items():
                try:
                    items[key1.lower()] = items[key1.lower()].replace(",", "") + "\n" + val1.replace(",", "")
                except KeyError:
                    items[key1.lower()] = val1.replace(",", "")
    csvWriter = csv.DictWriter(outputFile, fieldnames=items.keys())
    if i == 0:
        csvWriter.writeheader()
    csvWriter.writerow(items)


miOutputFile = open('misc.csv', 'w')
edOutputFile = open('education_and_training.csv', 'w')
exOutputFile = open('extracurricular.csv', 'w')
crOutputFile = open('credibility.csv', 'w')
awOutputFile = open('awards.csv', 'w')
acOutputFile = open('accomplishments.csv', 'w')
skOutputFile = open('skills.csv', 'w')
wxOutputFile = open('workExperience.csv', 'w')
bOutputFile = open('basic.csv', 'w')

fileList = glob.glob('jsonFiles/*.json')
fileList.sort()
i = 0
#pprint.pprint(fileList)
for file in fileList:
    pprint.pprint(file.title())
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
   # pprint.pprint(inputFile)
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
                         'gender': gender,
                         'email': emails,
                         'phone': phone,
                         'url': url,
                         'title': title})

    miHeaders = {'id': i, 'hobbies': "", 'interests': "", 'miscellaneous': "",
                 'personal interests': "", 'personal strength': "",
                 'personal strengths': "", 'strength': "", 'strengths': ""}
    miHeaders = collections.OrderedDict(sorted(miHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('misc', miOutputFile, miHeaders)

    edHeaders = {'id': i, 'academic background': "", 'academic experience': "",
                 'academic training': "", 'apprenticeships': "", 'certification': "",
                 'certifications': "", 'college activities': "", 'course project experience': "",
                 'courses': "", 'education': "", 'education and training': "", 'educational background': "",
                 'educational qualifications': "", 'educational training': "", 'internship experience': "",
                 'internships': "", 'patent': "", 'professional training': "",
                 'programs': "", 'related course projects': "", 'related courses': "",
                 'special training': "", 'study': "", 'training': "", 'workshops': "",
                 'qualifications': ""}

    edHeaders = collections.OrderedDict(sorted(edHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('education_and_training', edOutputFile, edHeaders)

    exHeaders = {'id': i, 'activities': "",
                 'activities and honors': "",
                 'affiliations': "",
                 'associations': "",
                 'athletic involvement': "",
                 'civic activities': "",
                 'community involvement': "",
                 'extra-curricular activities': "",
                 'honors': "",
                 'memberships': "",
                 'professional activities': "",
                 'professional affiliations': "",
                 'professional associations': "",
                 'professional memberships': "",
                 'volunteer experience': "",
                 'volunteer work': ""}
    exHeaders = collections.OrderedDict(sorted(exHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('extracurricular', exOutputFile, exHeaders)

    crHeaders = {'id': i, 'portfolio': "",
                 'recommendations': "",
                 'references': "",
                 'social media profiles': "",
                 'social profiles': "",
                 'testimonials': "",
                 'web portfolio': "",
                 'websites': ""}
    crHeaders = collections.OrderedDict(sorted(crHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('credibility', crOutputFile, crHeaders)

    awHeaders = {'id': i, 'academic Honors': "",
                 'accolades': "",
                 'accomplishments': "",
                 'achievements': "",
                 'activities and honors': "",
                 'awards': "",
                 'distinctions': "",
                 'endorsements': "",
                 'fellowship': "",
                 'fellowships': "",
                 'honors': "",
                 'scholarship': "",
                 'scholarships': ""}
    awHeaders = collections.OrderedDict(sorted(awHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('awards', awOutputFile, awHeaders)

    acHeaders = {'conference presentations': "",
                 'conventions': "",
                 'current research interests': "",
                 'dissertation': "",
                 'dissertations': "",
                 'exhibits': "",
                 'licenses': "",
                 'papers': "",
                 'presentations': "",
                 'professional publications': "",
                 'publications': "",
                 'research': "",
                 'research grants': "",
                 'research interests': "",
                 'research projects': "",
                 'thesis / theses': ""}
    acHeaders = collections.OrderedDict(sorted(acHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('accomplishments', acOutputFile, acHeaders)

    skHeaders = {'id': i, 'Abilities': "",
                 'Areas of Experience': "",
                 'Areas of Expertise': "",
                 'Areas of Knowledge': "",
                 'Career Related Skills': "",
                 'Computer Knowledge': "",
                 'Computer Skills': "",
                 'Credentials': "",
                 'Expertise': "",
                 'Language Competencies and Skills': "",
                 'Languages': "",
                 'Professional Skills': "",
                 'Proficiencies': "",
                 'Programming Languages': "",
                 'Qualifications': "",
                 'Skills': "",
                 'Specialized Skills': "",
                 'Technical Experience': "",
                 'Technical Skills': "",
                 'Technologies': ""}
    skHeaders = collections.OrderedDict(sorted(skHeaders.items(), key=lambda t: len(t[0])))
    dynamicPrint('skills', skOutputFile, skHeaders)

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
