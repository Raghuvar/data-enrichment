import csv
from ref import mobileSTDParser


def test_processMobile():
    inputFile = open('./sample_data.csv')

    # src_reader = csv.reader(src,delimiter=",")
    src_reader = csv.DictReader(inputFile, dialect=csv.excel);

    val = mobileSTDParser.processMobileSTDcode();

    phone_list = [];

    for row in src_reader:
        phoneNo = row['TestPhone'];
        if phoneNo is not None:  # getting Phone1 column data from the row
            city = row["City"]
            expectedResult = row["ExpectedResult"];
            result = val.processSTD(city, phoneNo);
            if(str(result) != expectedResult):
                print "Failure: Expected '"+expectedResult+"' but got "+str(result);
            phone_list.append(result);

    print(phone_list);


if __name__ == '__main__':
    test_processMobile();
