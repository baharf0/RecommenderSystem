import pandas as pd
import re
import csv


def find_ptrn():

    recency = pd.read_csv('rate_consumption_user.csv', sep=',', names=['mobile_number', 'recency'])
    service = pd.read_csv('malekiyat_service.csv', sep=',', names=['mobile_number', 'malekiyat_mahsol',
                          'time_baste', 'meg', 'ril'])

    arraymeg = [len(service)]
    arrayril = [len(service)]
    arrayrec = [len(service)]
    arrayunseen = []

    with open('patrn_user.csv', 'a') as f:
        fields = ['mobile_number', 'type_baste', 'rank_meg', 'rank_ril']
        write = csv.writer(f)
        write.writerow(fields)
        for row in range(1, len(service)):
            service.iloc[row, 3] = list(map(int, re.findall('[0-9]+', service.iloc[row, 3])))
            service.iloc[row, 4] = list(map(int, re.findall('[0-9]+', service.iloc[row, 4])))
            recency.iloc[row, 1] = list(map(int, re.findall('[0-9]+', recency.iloc[row, 1])))
            if service.iloc[row, 3] and service.iloc[row, 4] and recency.iloc[row, 1]:
                arraymeg.append(int(max(service.iloc[row, 3])))
                arrayril.append(int(max(service.iloc[row, 4])))
                arrayrec.append(int(max(recency.iloc[row, 1])))

                rank_meg = arraymeg[row] / arrayrec[row]
                rank_ril = arrayril[row] / arrayrec[row]
                mobile_number = service.iloc[row, 0]
                type_baste = service.iloc[row, 1]
                value = [mobile_number, type_baste, rank_meg, rank_ril]
                write = csv.writer(f)
                write.writerow(value)

            else:
                arraymeg.append(0)
                arrayril.append(0)
                arrayrec.append(0)
                arrayunseen.append([service.iloc[row, 0], service.iloc[row, 1]])

        unseen_type(arrayunseen)

    return 0


def unseen_type(line):

    unseen = []

    for i in range(0, len(line)):
        if line[i][1] not in unseen:
            unseen.append(line[i][1])
    find_unseen(unseen, line)

    return 0


def find_unseen(unseen, line):

    counter = 0

    with open('unseen.csv', 'a') as f:
        for j in range(0, len(unseen)):
            file = []
            for k in range(0, len(line)):
                if unseen[j] == line[k][1] and line[k][0] not in file:
                    counter += 1
                    file.append(line[k][0])
            value = [unseen[j], file]
            write = csv.writer(f)
            write.writerow(value)

    print(counter)

    return 0

find_ptrn()
