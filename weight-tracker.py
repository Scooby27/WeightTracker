from Calendar import Calendar            

def parse_calendar():
    file_lines  = open("Weight.ics", "r").readlines()
    weight_entries = []
    date_entries = []
    last_line_was_weight = False
    for line in file_lines:
        if last_line_was_weight:
            last_line_was_weight = False
            date = line[-17:-9]
            date_entries.append(date)
        if line.startswith("SUMMARY:"):
            weight = line[8:-2]
            if not weight.startswith("Target:"):
                weight_entries.append(weight)
                last_line_was_weight = True
    return Calendar(weight_entries, date_entries)


calendar = parse_calendar()
calendar.print_calendar()