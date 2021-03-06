import logging
import re

class removeDuplicates:
    def __init__(self):
        self.main_fields = ['Name','Street Address','Locality','City','Pincode']

    def website_base(self,website):
        regex = r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)"
        matches = re.match(regex, website, re.IGNORECASE | re.MULTILINE)
        if matches:
            return matches.group(1)
        return ''

    def group_similar(self):
        groups =dict()
        for row in self.rows:
            hsh = self.rhash(row)
            if hsh in groups:
                groups[hsh].append(row)
            else:
                groups[hsh] = [row]
        return groups

    def processAll(self,rows):
        self.rows = rows
        mergers=0
        groups=self.group_similar()
        print "\nInitial size of records"+str(len(self.rows))
        for i in groups:
            if len(groups[i])>1:
##                print "Now merging "+groups[i][0]['Name']+" "+groups[i][1]['Name']
                self.mergeRow(groups[i])
                mergers+=len(groups[i])
        print "Final size of records"+str(len(self.rows))
        print "Total meregers: "+str(mergers)

    def rhash(self,row):
        k=""
        for i in self.main_fields:
            k+=str(row.get(i)).lower().strip()
        return hash(k)

    def mergeRow(self,group):
        multiFields = [['Phone1','Phone2','Phone3','Phone4','Phone5'],['Mail','Mail2'],['Website','Website2']]
        row1 = group.pop(0)
        comm_id = int(row1['EduID'])
        pos=0
        while pos<len(group):
            row2 = group[pos]
            pos+=1
            for i in row1:
                if row2[i]:
                    if i == 'EduID':
                        comm_id = min(comm_id,int(row2[i]))
                    else:
                        row1[i] = self.mergeField(row1[i],row2[i])
            self.rows.remove(row2)
        row1['EduID'] = str(comm_id)

        for fld in multiFields:
            fields=[]
            if fld == ['Website','Website2']:
                unique_bases = set()
                for i in fld:
                    if row1[i]:
                        for x in row1[i].split(','):
                            base = self.website_base(x)
                            if base not in unique_bases:
                                unique_bases.add(base)
                                fields.append(x)
            else:
                for i in fld:
                    if row1[i]:
                        fields+=row1[i].split(',')
    ##                    print i,row1[i]
            for n,i in enumerate(fld):
                if n>len(fields)-1:
                    break
                row1[i] = fields[n]
##                print i,row1[i]

    def mergeField(self,r1,r2):
        if r1:
            field1=r1.split(',')
        else:
            field1=[]
        if r2:
            field2=r2.split(',')
        else:
            field2=[]
        dictionary=dict(zip(field1,[0 for i in field1]))

        for i in field2:
            if not i in dictionary:
                field1.append(i)
        return ','.join(field1)
