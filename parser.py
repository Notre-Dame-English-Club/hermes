from csv import DictReader, DictWriter

rolls = []
rollcounter = dict()
class Member():
    def __init__(self, roll):
        self.roll = roll
    
    def is_valid(self):
        if len(self.roll)==8:
            return True
        else:
            return False

    def group(self):
        if self.roll[0] == '1':
            self.dept = 'Science'
        elif self.roll[0] == '4':
            self.dept = 'Humanities'
        elif self.roll[0] == '6':
            self.dept = 'Commerce'
        else:
            return False
        
        self.group = self.roll[3:5]

        return f"{self.dept}{self.group}"
    def add_roll(self, roll):
        self.clubroll = roll

original = open('db.csv', 'r', encoding='utf-8')
verified = open('newdb.csv', 'w', encoding='utf-8')

reader = DictReader(original)
headers = ['name', 'roll', 'email', 'contact', 'clubroll', 'time', 'trx', 'message']
writer = DictWriter(verified, fieldnames=headers)
writer.writeheader()

#Email Address,Name,College Roll,Mobile Number (If Any)
for row in reader:
    name, roll, email, contact, trx = row['Name'], row['College Roll'], row['Email Address'], row['Mobile Number (If Any)'], row['Rocket Transaction ID (txn ID):']
    if roll in rolls:
        continue
    member = Member(roll)
    if member.is_valid():
        group = member.group()
        
        try:
            rollcounter[group]+=1
        except:
            rollcounter[group] = 1
        if len(str(rollcounter[group])) == 1:
            rollstr = f'0{rollcounter[group]}'
        else:
            rollstr = rollcounter[group]
        clubroll = f"1922{roll[0]}{roll[3:5]}{rollstr}"
        if len(trx)==10:
            trxmessage = ""
        else:
            trxmessage = f"Note:\nYour TnxID: {trx} does not seem to be valid. Please recheck your TnxID and send us the correct TnxID. In case you cannot access the TnxID at this moment but have any other proof of successful payment, please reply to this email with the proof. If you think the TnxID is valid, please let us know by replying to this email.\nPlease note that, if you do not receive your email within 72 hours, your membership will be provoked."
        writer.writerow({
            'name':name, 
            'roll':roll, 
            'email':email, 
            'contact':contact, 
            'clubroll':clubroll, 
            'trx':trx, 
            'message':trxmessage,
            'time': row['Timestamp'].split()[0]
        })