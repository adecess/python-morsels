def parse_ranges(text):
    intervals = text.split(',')
    return (
            number
            for interval in intervals
            for number in range(int(interval.split("-")[0]), int(interval.split("-")[1]) + 1)
           )

print(list(parse_ranges('0-0, 4-8, 20-20, 43-45')))
