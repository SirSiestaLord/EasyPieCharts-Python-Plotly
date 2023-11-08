import plotly.graph_objects as go

Persons = []


def getavggraph(string):
    AvgNames = []
    Avgdatas = []
    for i in Persons:
        for x in range(len(i.labels)):
            if string == i.labels[x]:
                Avgdatas.append(i.datas[x])
                AvgNames.append(i.name)
    print(Avgdatas)
    print(AvgNames)
    figx = go.Figure(data=[go.Pie(labels=AvgNames,
                                  values=Avgdatas)])
    figx.update_traces(title="Averages Of {}".format(string), hoverinfo='label+percent', textinfo='value',
                       textfont_size=20,
                       marker=dict(line=dict(color='#000000', width=2)))
    figx.show()


def getpersongraph(string):
    for i in Persons:
        if string == i.name:
            figx = go.Figure(data=[go.Pie(labels=i.labels,
                                          values=i.datas)])
            figx.update_traces(title="EasyPieCharts-Python-Plotly Of {}".format(i.name), hoverinfo='label+percent', textinfo='value',
                               textfont_size=20,
                               marker=dict(line=dict(color='#000000', width=2)))
            figx.show()


def addperson():
    labels = []
    labeldatas = []
    name = input("Write the Person's Name:")
    print("Enter Labels For Graphic(write 'e' for exit)")
    print("*" * 30)
    a = ""
    while a != "e":
        a = input("Write The Label:")
        if (a != "e"):
            labels.append(a)
            labeldatas.append(input("Write of the {} Label's Data:".format(a)))
        else:
            pers = Person(name, labels, labeldatas)
            Persons.append(pers)
            return name


class Person:

    def __init__(self, name, labels, datas):
        self.name = name
        self.datas = datas
        self.labels = labels
        print("Person Added Succesfully")
        print("*" * 30)

    def persongraph(self):
        figx = go.Figure(data=[go.Pie(labels=self.labels,
                                      values=self.datas)])
        figx.update_traces(title=self.name, hoverinfo='label+percent', textinfo='value', textfont_size=20,
                           marker=dict(line=dict(color='#000000', width=2)))
        figx.show()
