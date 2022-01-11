import pandas as pd
import csv
import math
import re

profile_baste = pd.read_csv('new_profile_baste.csv', sep=',', names=['type_baste', 'meg', 'rial', 'time',
                                                                     'rate_meg', 'rate_Tom', 'percent'])
patrn_user = pd.read_csv('patrn_user.csv', sep=',', names=['mobile_number', 'type_baste',
                                                           'rank_meg', 'rank_ril'])

fields = ['mobile_number', 'current_type', 'best_type', 'rank', 'most',
          'day_min_value', 'week_min_value', 'month_min_value', 'three_month_min_value',
          'six_month_min_value', 'year_min_value', 'sh_min_value']

with open('final.csv', 'a') as f:
    write = csv.writer(f)
    write.writerow(fields)


def find_dis():
    all_dis_value = []

    for counter in range(1, len(patrn_user)):
        for row in range(1, len(profile_baste)):
            x1 = float(patrn_user.iloc[counter, 2])
            y1 = float(patrn_user.iloc[counter, 3])
            x2 = float(profile_baste.iloc[row, 4])
            y2 = float(profile_baste.iloc[row, 5])
            x_dis = abs(x2 - x1)
            y_dis = abs(y2 - y1)
            mobile_number = patrn_user.iloc[counter, 0]
            current_type = patrn_user.iloc[counter, 1]
            type_baste = profile_baste.iloc[row, 0]
            time = profile_baste.iloc[row, 3]
            percent = profile_baste.iloc[row, 6]
            dis = math.sqrt(pow(x_dis, 2) + pow(y_dis, 2))
            all_dis_value.append([mobile_number, current_type, type_baste, time, dis, percent])

    find_mobile(all_dis_value)

    return 0


def find_mobile(file):  # separate each mobile number as a file

    mobile_value = []

    for i in range(1, len(file)):

        if i+1 != len(file):
            if file[i-1][0] == file[i][0]:
                mobile_value.append(file[i-1])
                continue
            else:
                mobile_value.append(file[i-1])
                find_best(mobile_value)
                mobile_value = []
        else:
            if file[-1][0] == file[-2][0]:
                mobile_value.append(file[-1])
                find_best(mobile_value)
                break
            else:
                find_best(mobile_value)
                mobile_value = []
                find_best(file[-1])

    return 0


def find_best(file):

    current_type = []

    best_type = day_min_value = week_min_value = month_min_value = \
        three_month_min_value = six_month_min_value = year_min_value = sh_min_value = 0

    min_dis = day_min_dis = week_min_dis = month_min_dis = three_month_min_dis = six_month_min_dis = \
        year_min_dis = sh_min_dis = 100000

    with open('final.csv', 'a') as ff:
        writer = csv.writer(ff)
        mobile_number = file[0][0]
        for counter in range(0, len(file)):
            if file[counter][1] not in current_type:
                current_type.append(file[counter][1])
            if int(file[counter][4]) < min_dis:
                best_type = file[counter][2]
                min_dis = file[counter][4]
            if int(file[counter][3]) == 1:
                if int(file[counter][4]) < day_min_dis:
                    day_min_value = file[counter][2]
                    day_min_dis = file[counter][4]
            elif int(file[counter][3]) == 7:
                if int(file[counter][4]) < week_min_dis:
                    week_min_value = file[counter][2]
                    week_min_dis = file[counter][4]
            elif int(file[counter][3]) == 30:
                if int(file[counter][4]) < month_min_dis:
                    month_min_value = file[counter][2]
                    month_min_dis = file[counter][4]
            elif int(file[counter][3]) == 90:
                if int(file[counter][4]) < three_month_min_dis:
                    three_month_min_value = file[counter][2]
                    three_month_min_dis = file[counter][4]
            elif int(file[counter][3]) == 180:
                if int(file[counter][4]) < six_month_min_dis:
                    six_month_min_value = file[counter][2]
                    six_month_min_dis = file[counter][4]
            elif int(file[counter][3]) == 360:
                if int(file[counter][4]) < year_min_dis:
                    year_min_value = file[counter][2]
                    year_min_dis = file[counter][4]
            if int(file[counter][3]) == 3 or int(file[counter][3]) == 5 or \
               int(file[counter][3]) == 10 or int(file[counter][3]) == 10 or \
               int(file[counter][3]) == 20:
                if int(file[counter][4]) < sh_min_dis:
                    sh_min_value = file[counter][2]
                    sh_min_dis = file[counter][4]

        rank = find_rank(current_type, best_type)
        most = best_for_us(best_type)
        row = [mobile_number, current_type, best_type, rank, most,
               day_min_value, week_min_value, month_min_value, three_month_min_value,
               six_month_min_value, year_min_value, sh_min_value]
        writer.writerow(row)

    return 0


def find_rank(current, best):

    current_rank_meg = current_rank_ril = 0
    best_rank_meg = best_rank_ril = 0
    rank = []
    splitted = []

    for i in range(0, len(current)):
        if re.findall('\',', current[i]):
            line = current[i].split(',')
            for j in range(0, len(line)):
                splitted.append(line[j])
        else:
            splitted.append(current[i])

    for item in range(0, len(splitted)):
        for counter in range(0, len(profile_baste)):
            if profile_baste.iloc[counter, 0] == splitted[item] or \
               profile_baste.iloc[counter, 0].replace("[", " ") == splitted[item] or \
               profile_baste.iloc[counter, 0].strip("]") == splitted[item]:
                current_rank_meg = profile_baste.iloc[counter, 4]
                current_rank_ril = profile_baste.iloc[counter, 5]
            if profile_baste.iloc[counter, 0] == best:
                best_rank_meg = profile_baste.iloc[counter, 4]
                best_rank_ril = profile_baste.iloc[counter, 5]
        x = float(current_rank_meg) - float(best_rank_meg)
        y = float(current_rank_ril) - float(best_rank_ril)
        rank.append(int(math.sqrt(pow(x, 2) + pow(y, 2))))

    return rank


def best_for_us(best_type):

    best = 0

    for counter in range(0, len(profile_baste)):
        if profile_baste.iloc[counter, 0] == best_type:
            time = profile_baste.iloc[counter, 3]
            break

    for row in range(0, len(profile_baste)):
        if profile_baste.iloc[row, 3] == time and float(profile_baste.iloc[row, 6]) > best:
            best = float(profile_baste.iloc[row, 6])
            most = profile_baste.iloc[row, 0]

    return most


find_dis()
