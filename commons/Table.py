from terminaltables import SingleTable
import sys
from commons import *
import pytz


class Table:
    def __init__(self, columns):
        self.columns = columns
        self.rows = [[c["name"] for c in self.columns]]
        self.items = []
        self.status = ""


    def append(self, object):
        self.items.append(object)
        try:
            row = []
            for col in self.columns:
                name = col["name"]
                value = object[name] if name in object else ""
                if value == "":
                    pass
                elif "type" not in col:
                    value = value
                elif col["type"] is "size":
                    value = format_bytes(value)
                elif col["type"] is "number":
                    value = format_num(value)
                elif col["type"] is "boolean":
                    value = TICK if value == "true" else CROSS
                elif col["type"] is "age":
                    value = format_seconds(value)

                row.append(value)
            self.rows.append(row)
            # self.print_frame()
        except Exception, e:
           import traceback
           traceback.print_exc(file=sys.stdout)


    def print_frame(self):
        sys.stdout.write( CLEAR_SCREEN + move_cursor(0,0) + SingleTable(self.rows).table)
        sys.stdout.write("\n" + green(self.status + " ...\n"))

    def update_status(self, status):
        self.status = status
        self.print_frame()

