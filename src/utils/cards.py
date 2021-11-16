import datetime


class Cards:
    def add_card(self):
        member = input("Enter member")
        description = input("Enter description")
        tag = input("Enter tag")
        checklist = input("Enter checklist")
        date = datetime.datetime.now()
        update_date = date.strftime("%Y-%m-%d %H:%M:%S")
        req = "INSERT INTO card (member, description, tag, checklist, update_date) VALUES ({member}, {description}, {tag}, {checklist}, {update_time})".format(member=member, description=description, tag=tag, checklist=checklist, update_date=update_date)
        return req
