import time
import gspread
from datetime import datetime
from PN7120 import PN7120

print("PiBook Tracker System: NFC PN7120 Controller Test")

def main():
    
    #open Google sheet
    gc = gspread.service_account()
    #wks = gc.open("Where is the money Lebowski?").sheet1
    sh= gc.open("Pibook_tracker_sheet")
    # Dump book sheet template rows
    #print(sh.sheet1.get('A1'))
    sheet = sh.worksheet("BookSheet1")
     # print Book sheet table
    book_atributes = sheet.row_values(1)
    book_titles = sheet.col_values(1)
    #print('Col: ', book_titles)
    #print('Row: ', book_atributes)
    pn7120 = PN7120()
    i=0
    
    while True:
        n=0
        
        pn7120.when_tag_read = lambda text: print("Tag information:",text)
        
        readBook = pn7120.read_once()
        pn7120.start_reading()
        pn7120.stop_reading()
        
        readBook_row = 0
        for bookName in book_titles:
            n = n+1
           # print(bookName)
            #print(type(bookName))
            if bookName == readBook:
               readBook_row = n
            else:
               readBook_row = readBook_row    
                
        print('readBook_row= ',readBook_row)
       # print("Please write the information of the book into NFC TAG")
        text_update_tag = 'seeing through paintings'
        #start counting time
        input("Press Enter to start")
        start_time = time.time()
        input("Press Enter to stop")
        end_time = time.time()
        
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)   
      
        #print("Current TAG:",readBook)
        #print("Updated TAG:",text_update_tag)
        #pn7120.write(text_update_tag)
        i=i+1
        
        startDate_list = sheet.col_values(7)
        targetDate_list = sheet.col_values(8)
        process_list = sheet.col_values(9)
        #print('startDate_list: ', startDate_list)
        #start_data=len(startDate_list)
        
       # now = datetime.now()
       # dateTime_init = now.strftime("%d/%m/%Y %H:%M:%S")
       # print("date and time =", dateTime_init)
        print('Process = ', sheet.cell(readBook_row,9).value) 
        readTime_past = (sheet.cell(readBook_row,9).value)
        readTime_acc = float(readTime_past) + time_lapsed
        #current_readTime = (sheet.cell(3,8).value)
        #print('last_readTime = ', last_readTime)
        #print('current_readTime = ', current_readTime)
        
        
        sheet.update_acell('I3', readTime_acc)
        #sheet.update_acell(sheet.cell(readBook_row,9), readTime_acc)
        #print('targetDate_list: ', targetDate_list)
        #print('process_list: ', process_list)
        #print(len(process_list))
        
        smileyBytes = b'\xf0\x9f\x99\x84'
        #smileyBytes.decode('utf-8')
        sheet.update('J3', smileyBytes.decode('utf-8'))
        
        
        
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
     
main()