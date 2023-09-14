class student:

    def add():
        zist = int (input("zist:"))
        dini = int (input("dini:"))
        shimi = int (input("shimi:"))
        zaban = int (input("zaban:"))
        ryazi = int (input("ryazi:"))
        alln = [zist,dini,shimi,zaban,ryazi]
        return zist,dini,shimi,zaban,ryazi,alln


    def average():
        global zist
        global dini
        global shimi
        global zaban
        global ryazi
        global sum2
        average = (zist + shimi +dini + zaban + ryazi)/5
        print(average)


    def sum():
        sum2 = (zist + shimi +dini + zaban + ryazi)
        print(sum2)


    def minmax():
        global alln
        min(alln)
        max(alln)
