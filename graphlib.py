import plotly.graph_objects as go

# Define a list to store instances of the Person objects
Persons = []


# Define a function to create a pie chart for the average data of a specific label
def getavggraph(string):
    # Lists to store labels and corresponding data for averaging
    AvgNames = []
    Avgdatas = []

    # Loop through each person in the Persons list
    for i in Persons:
        # Loop through the labels and datas of the current person
        for x in range(len(i.labels)):
            if string == i.labels[x]:
                # If the label matches the input string, append data and name to lists
                Avgdatas.append(i.datas[x])
                AvgNames.append(i.name)

    # Create a pie chart using Plotly
    figx = go.Figure(data=[go.Pie(labels=AvgNames, values=Avgdatas)])
    figx.update_traces(
        title="Averages Of {}".format(string),
        hoverinfo='label+percent',
        textinfo='value',
        textfont_size=20,
        marker=dict(line=dict(color='#000000', width=2))
    )
    # Show the pie chart
    figx.show()


# Define a function to create a pie chart for a specific person's data
def getpersongraph(string):
    # Loop through each person in the Persons list
    for i in Persons:
        if string == i.name:
            # Create a pie chart using Plotly
            figx = go.Figure(data=[go.Pie(labels=i.labels, values=i.datas)])
            figx.update_traces(
                title="EasyPieCharts-Python-Plotly Of {}".format(i.name),
                hoverinfo='label+percent',
                textinfo='value',
                textfont_size=20,
                marker=dict(line=dict(color='#000000', width=2))
            )
            # Show the pie chart
            figx.show()


# Define a function to add a person with their labels and data
def addperson():
    labels = []
    labeldatas = []
    name = input("Write the Person's Name:")
    print("Enter Labels For Graphic (write 'e' for exit)")
    print("*" * 30)
    a = ""
    while a != "e":
        a = input("Write The Label:")
        if (a != "e"):
            labels.append(a)
            labeldatas.append(input("Write of the {} Label's Data:".format(a)))
        else:
            # Create a Person instance and append it to the Persons list
            pers = Person(name, labels, labeldatas)
            Persons.append(pers)
            return name


# Define a Person object to represent a person with their labels and data
class Person:
    def __init__(self, name, labels, datas):
        self.name = name
        self.datas = datas
        self.labels = labels
        print("Person Added Succesfully")
        print("*" * 30)

    def persongraph(self):
        # Create a pie chart using Plotly
        figx = go.Figure(data=[go.Pie(labels=self.labels, values=self.datas)])
        figx.update_traces(
            title=self.name,
            hoverinfo='label+percent',
            textinfo='value',
            textfont_size=20,
            marker=dict(line=dict(color='#000000', width=2))
        )
        # Show the pie chart
        figx.show()
