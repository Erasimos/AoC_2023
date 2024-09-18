import shutil
import sys

def create_new_day(day_template, new_day):
    new_file_name = 'day_' + str(new_day) + '.py'
    shutil.copy(day_template, new_file_name)

if __name__ == '__main__':
    new_day = sys.argv[1]
    template_file = 'day_template.py'
    create_new_day(template_file, new_day)