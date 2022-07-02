class Classy(object):
    def __init__(self):
        self.items = []
        self.class_objects = {
            "tophat" : 2,
            "bowtie" : 4,
            "monocle": 5
        }

    def addItem(self,class_item):
        if class_item in self.class_objects.keys():
            self.items.append(class_item)



    def getClassiness(self):
        c = 0
        for i in self.items:
            if self.class_objects.keys() in self.items:
                print('yes')

me = Classy()
me.addItem('tophat')
me.addItem("bowtie")

print(me.getClassiness())

