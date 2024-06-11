from datetime import datetime
def note(string):
    string = str(string)
    with open('note.log.txt', 'a') as f:
        time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(time + ':\n')
        f.write(string + '\n')