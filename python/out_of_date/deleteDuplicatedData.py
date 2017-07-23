import os

def deleteDuplicatedRecords(filePath):

    if os.path.exists(filePath):
        print("passed")
        uniqRecords = sorted(set(open(filePath).readlines()))

        fFile = open(filePath, 'w', encoding="UTF-8")

        for record in uniqRecords:
            fFile.write(record)

        fFile.close()