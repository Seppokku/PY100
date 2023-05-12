from statistics import median
def stat(strg):
    b = [[int(j) for j in i.split('|')] for i in strg.split(', ')]
    list_secs = [i[0] * 3600 + i[1] * 60 + i[2] for i in b]
    range = max(list_secs) - min(list_secs)
    avg = sum(list_secs) / len(list_secs)
    med_ = median(list_secs)
    list_times = [range, avg, med_]

    def convert_to_time(sec):
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        return "%02d|%02d|%02d" % (hour, min, sec)
    time_format = list(map(convert_to_time, list_times))
    return f'Range: {time_format[0]} Average: {time_format[1]} Median: {time_format[2]}'