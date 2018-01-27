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