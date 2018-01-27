from datetime import datetime

class Calendar:
    weight_entries = []
    date_entries = []

    def __init__(self, weight_entries, date_entries):
        self.weight_entries = weight_entries
        self.date_entries = date_entries
    
    def sort_dates (self, element):
        return element[0]

    def print_calendar(self):
        values = []
        for i, value in enumerate(self.date_entries):
            date = datetime.strptime(value, "%Y%M%d")
            values.append([date, self.weight_entries[i]])
        values.sort(key=self.sort_dates)
        for value in values:
            print value[0].strftime('%d/%M/%Y') + ": " + value[1]
        

            

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