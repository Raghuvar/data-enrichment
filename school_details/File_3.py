from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


def school_details(new_url):
    my_url = new_url

    # opening up the connection, grabbing the page
    newClient = uReq(my_url)
    new_page_html = newClient.read()
    newClient.close()

    # html parsing
    new_page_soup = soup(new_page_html, "html.parser")

    new_container = new_page_soup.findAll('td', {"width": "494"})

    # getting school_name, Afilliation_no, Addresss, Phone_no, email_id

    school_name = new_container[0].text.strip()
    affiliation_no = new_container[1].text.strip()
    state = new_container[2].text.strip()
    district = new_container[3].text.strip()
    postal_address = new_container[4].text.strip()
    pin_code = new_container[5].text.strip()
    std_code = new_container[6].text.strip()
    phone_no = new_container[7].text.strip()  # phone number from web-site
    email_id = new_container[10].text.strip()
    web_site = new_container[11].text.strip()
    year_of_foundation = new_container[12].text.strip()
    date_of_opening = new_container[13].text.strip()
    name_of_principal = new_container[14].text.strip()
    sex = new_container[15].text.strip()
    status_of_school = new_container[20].text.strip()
    type_of_affiliation = new_container[21].text.strip()
    affiliation_period_from = new_container[22].text.strip()
    affiliation_period_to = new_container[23].text.strip()
    name_of_trust_society_managing_committee = new_container[24].text.strip()

    # formatting the data
    new_school_name = '\"' + school_name + '\"'
    new_affiliation_no = '\"' + affiliation_no + '\"'
    new_state = '\"' + state + '\"'
    new_district = '\"' + district + '\"'
    new_pin_code = '\"' + pin_code + '\"'
    # std_code = '\"' + std_code + '\"'
    new_year_of_foundation = '\"' + year_of_foundation + '\"'
    new_postal_address = '\"' + postal_address + '\"'
    new_email_id = '\"' + email_id + '\"'
    new_web_site = '\"' + web_site + '\"'
    new_date_of_opening = '\"' + date_of_opening + '\"'
    new_name_of_principal = '\"' + name_of_principal + '\"'
    new_status_of_school = '\"' + status_of_school + '\"'
    new_type_of_affiliation = '\"' + type_of_affiliation + '\"'
    new_affiliation_period_from = '\"' + affiliation_period_from + '\"'
    new_name_of_trust_society_managing_committee = '\"' + \
                                                   name_of_trust_society_managing_committee + '\"'

    updated_affiliation_period_to = re.sub(' +', ' ', affiliation_period_to)
    test_updated_affiliation_period_to = updated_affiliation_period_to.replace(
        '\n', '')
    check_updated_affiliation_period_to = test_updated_affiliation_period_to.replace(
        '\t', '')
    new_affiliation_period_to = '\"' + check_updated_affiliation_period_to + '\"'


    # updating STD code by pre-pending 0 as prefix
    
    # format of phone no and telephone number being followed has 0 as a prefix for both phone no.(+91 is not being used to maintain uniformaty) and telephone no.
    # e.g. 070324xxxxx (phone nummber) and 011270xxxxx (Telephone number).

    print "I'm waiting to update the std code"
    print len(std_code)

    if len(std_code) < 3 and len(std_code) > 1:  # checking for 2-digit std code
        print "2-digit std"
        std_code = str(0) + str(std_code)
    elif len(std_code) < 4 and len(std_code) > 2:  # checking for 3-digit std code
        print "3-digit std"
        if std_code[0] != "0":  # checking if it's  not an 2-digit std code with prefix 0
            std_code = str(0) + str(std_code)
    elif len(std_code) < 5 and len(std_code) > 3:  # checking for 4-digit std code
        print "4-digit std"
        if std_code[0] != "0":  # checking if it's  not an 3-digit std code with prefix 0
            std_code = str(0) + str(std_code)
    elif std_code[0] == "0" and len(std_code) == 5:  # checking for std code
        pass
    else:
        std_code = ""

    # end of code for updating std code



    # updating phone no. to have multiple columns if more then one no. is given
    print "about to update phone numbers"

    # removing extra white spaces
    new_phone_no = phone_no.replace(" ", "")

    # checking if there are more then one contact number given or available
    print "updating phone numbers"
    if new_phone_no.find(',') != -1:
        phone_list = new_phone_no.split(",")
        Phone_no_1 = str(phone_list[0].strip())
        Phone_no_2 = str(phone_list[1].strip())
        # code for adding STD code as perfix in the telephone no.

        if len(Phone_no_1) > 11 or len(Phone_no_1) < 6:     # removing invalid phone of length greater then 11 and telephone no of length less then 6-digits(without STD code).
            Phone_no_1 = ""

        if len(Phone_no_2) > 11 or len(Phone_no_2) < 6:
            Phone_no_2 = ""

        if len(Phone_no_1) < 10:  # checks for telephone no (and not phone number)
            if len(Phone_no_1) < 6:  # removing invalid landline number with less then 6 digits
                Phone_no_1 = ""
            else:
                Phone_no_1 = std_code + Phone_no_1  # adding std code as prefix along and 0 for trunk dialing
                Phone_no_1 = Phone_no_1.replace("-", "")
                if len(Phone_no_1) < 10:
                    Phone_no_1 = ""
                elif len(Phone_no_1) > 11:
                    Phone_no_1 = ""

        if len(Phone_no_2) < 10:
            if len(Phone_no_2) < 6:
                Phone_no_2 = ""
            else:
                Phone_no_2 = std_code + Phone_no_2
                Phone_no_2 = Phone_no_2.replace("-", "")
                if len(Phone_no_2) < 10:
                    Phone_no_2 = ""
                elif len(Phone_no_2) > 11:
                    Phone_no_2 = ""
        Phone_no_1 = '\"' + Phone_no_1 + '\"'
        Phone_no_2 = '\"' + Phone_no_2 + '\"'

        # end of code for adding STD
    else:
        Phone_no_1 = new_phone_no

        if len(Phone_no_1) < 10:
            if len(Phone_no_1) < 6:
                Phone_no_1 = ""
            else:
                Phone_no_1 = std_code + Phone_no_1
                Phone_no_1 = Phone_no_1.replace("-", "")
                if len(Phone_no_1) < 10:
                    Phone_no_1 = ""
        Phone_no_1 = '\"' + Phone_no_1 + '\"'

    # removing the phone no. with less then 10 digits
    new_std_code = '\"' + std_code + '\"'

    # printing the data

    print '------------------------------------------------------------------------------------------------------------'
    print 'school_name    : ' + new_school_name
    print 'affiliation_no : ' + new_affiliation_no
    print 'Address        : ' + new_postal_address + ',' + new_district + ',' + new_state
    print 'pin            : ' + new_pin_code
    # print 'STD_Code       : ' + new_std_code
    print 'Phone_no_1     : ' + Phone_no_1
    print 'Phone_no_2     : ' + Phone_no_2
    print 'email_id       : ' + new_email_id
    print 'web_site       : ' + new_web_site
    print 'year_of_foundation : ' + new_year_of_foundation
    print 'date_of_opening : ' + new_date_of_opening
    print 'name_of_principal : ' + new_name_of_principal
    print 'Sex              : ' + sex
    print 'status_of_school  : ' + new_status_of_school
    print 'type_of_affiliation : ' + new_type_of_affiliation
    print 'affiliation_period_from : ' + new_affiliation_period_from
    print 'affiliation_period_to : ' + new_affiliation_period_to
    print 'name_of_trust_society_managing_committee : ' + new_name_of_trust_society_managing_committee
    print '------------------------------------------------------------------------------------------------------------'

    filename = "shashank_kumar.csv"
    f = open(filename, "a")

    # f.write(Phone_no_1 + "," + Phone_no_2 + "\n")

    f.write(
        new_school_name + "," + new_affiliation_no + "," + new_state + "," + new_district + "," + new_postal_address + "," + new_pin_code + "," + Phone_no_1.replace("-", "").replace("(","").replace(")","") + "," + Phone_no_2.replace("-", "").replace("(","").replace(")","") + "," + new_email_id + "," + new_web_site + "," + new_year_of_foundation + "," + new_date_of_opening + "," + new_name_of_principal + "," + sex + "," + new_status_of_school + "," + new_type_of_affiliation + "," + new_affiliation_period_from + "," + new_affiliation_period_to + "," + new_name_of_trust_society_managing_committee + "\n")

    f.close()
