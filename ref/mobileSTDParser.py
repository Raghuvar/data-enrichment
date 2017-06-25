import csv
import os

class processMobileSTDcode:
    def processSTD(self, city, telephone):

        ph_len = len(telephone.replace('-', '').replace(" ",""))  # remove invaid characters e.g. '54-66121  3231'
        # print("length of telephone number is: "+str(ph_len))

        STD_FILE_NAME = os.path.join(os.path.dirname(__file__), 'std_data.csv')
        readfile = open(STD_FILE_NAME)
        filereader = csv.DictReader(readfile, dialect=csv.excel);

        if(ph_len>0 and ph_len < 9):
            for row in filereader:  # here row refers to a row in the csv file of std_data.csv
                field = row['CITY']  # iterating over various fields in csv file which are city, circle and std
                if field.upper() == city.upper():
                    stdno = eval(row['STD'])  # fetching std code
                    # print(stdno)
                    # print(len(str(stdno)))
                    std_len = len(str(stdno))

                    if std_len == 2:
                        std_str = '%0*d' % (3, stdno)  # e.g. converts 11 to 011

                    elif std_len == 3:
                        std_str = '%0*d' % (4, stdno)  # e.g. converts 524 to 0524

                    else:
                        std_str = '%0*d' % (5, stdno)  # e.g. converts 1254 to 01254

                    # print(std_str)
                    # print(len(std_str))

                    new_tele = std_str + telephone.replace('-', '')
                    # print(new_tele)

                    if len(new_tele) == 11:
                        #print('new_tele no: ' + new_tele)
                        return new_tele
                    else:
                        #print('telephone no: ' + telephone)
                        return None

        readfile.close()