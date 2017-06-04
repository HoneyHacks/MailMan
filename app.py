import xlrd

from flask import Flask, render_template, request, redirect, url_for
import mailing

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'xls'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def parse_upload_form():
    f = request.files['file']
    data = []
    if f and allowed_file(f.filename):
        extension = str(f.filename.rsplit('.', 1)[1].lower())
        if extension == "xlsx" or extension == "xls":
            workbook = xlrd.open_workbook(file_contents=f.read())
            worksheet = workbook.sheet_by_index(0)
            data = list(cast_row(worksheet.row_values(rx, 0, 4)) for rx in range(worksheet.nrows) if worksheet.row_len(rx) == 4)
        elif extension == "csv":
            data = data_from_csv_string(f.read().decode("utf-8"))
    else:
        csv = request.form['data']
        data = data_from_csv_string(csv)
    return data


@app.route('/item', methods=['POST'])
def item():
    data = parse_upload_form()
    for i in range(len(data)):
        print(data[i][0])
        sendEmail()
    return(render_template('sent.html'))

@app.route('/')
def renderPage():
    return(render_template('index.html'))

def cast_row(row):
    '''
    Convert workbook sheet cells into integers if they are equal to integer
    values and convert everything to a string.
    The xlrd library seems to import cells as float values if the cell had a
    numeric value, so this method is needed to correct that.
    '''
    for i, item in enumerate(row):
        if isinstance(item, (float, int)) and int(item) == item:
            row[i] = str(int(item))
        else:
            row[i] = str(item)
    return row


def data_to_csv_string(data):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    return output.getvalue()

def data_from_csv_string(string):
    data_input = io.StringIO(string)
    reader = csv.reader(data_input)
    return list(reader)


app.run(debug=True)
