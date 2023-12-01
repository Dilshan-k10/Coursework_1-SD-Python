from graphics import *

credit_range = [0, 20, 40, 60, 80, 100, 120]
total_input = 0
total_credits = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
status = " "
main_list = []
data_list = []


def inputValidate(credit_name):
    global credit_range
    while True:
        try:
            credit_name = int(credit_name)

            if credit_name in credit_range:
                return credit_name
                # print(credit_name)

            else:
                print("Out of range\n")
                credit_name = input(f"Please enter a valid value from {credit_range}: ")

        except ValueError:
            print("Integer required\n")
            credit_name = input(f"Please enter a valid value from {credit_range}: ")


def progressionLevel():

    global progress
    global retriever
    global trailer
    global exclude
    global total_input
    global total_credits
    global status

    total_credits = int(pass_credits + defer_credits + fail_credits)

    if total_credits != 120:
        print("Total incorrect")

    elif pass_credits == 120:
        status = "Progress"
        print(status)
        progress = progress + 1
        return progress

    elif pass_credits == 100:
        status = "Progress (module trailer)"
        print(status)
        trailer = trailer + 1
        return trailer

    elif fail_credits >= 80:
        status = "Exclude"
        print(status)
        exclude = exclude + 1
        return exclude

    else:
        status = "Do not progress (module retriever)"
        print(status)
        retriever = retriever + 1
        return retriever

    return total_credits, status


def userInput():
    global loop_condition
    loop_condition = input(
        "\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    loop_condition = loop_condition.lower()
    print()


def graphicHistogram():

    global total_input
    global progress
    global trailer
    global retriever
    global exclude

    def textFormat(variable_name, size, style):
        variable_name.setSize(size)
        variable_name.setStyle(style)


    def bar_height(bar_name):
        if bar_name == 0:
            value = 20
        else:
            value = ((60 // total_input) * bar_name) + 20

        return value



    win = GraphWin("Histogram", 800, 600)

    win.setCoords(0, 0, 100, 100)

    total_variable = Text(Point(15, 10), total_input)
    textFormat(total_variable, 15, "bold")
    total_variable.draw(win)

    total_message = Text(Point(28, 10), "outcomes in total.")
    textFormat(total_message, 15, "bold")
    total_message.draw(win)

    top_message = Text(Point(22, 95), "Histogram Results")
    textFormat(top_message, 15, "bold")
    top_message.draw(win)

    bottom_line = Line(Point(5, 20), Point(95, 20))
    bottom_line.draw(win)

    progress_bar = Rectangle(Point(10, 20), Point(29, bar_height(progress)))
    progress_bar.setFill("limegreen")
    progress_bar.draw(win)

    progress_label = Text(Point(19, 18), "Progress")
    textFormat(progress_label, 12, "bold")
    progress_label.draw(win)

    progress_value = Text(Point(19, bar_height(progress) + 2), progress)
    textFormat(progress_value, 12, "bold")
    progress_value.draw(win)

    trailer_bar = Rectangle(Point(30, 20), Point(49, bar_height(trailer)))
    trailer_bar.setFill("forestgreen")
    trailer_bar.draw(win)

    trailer_label = Text(Point(39, 18), "Trailer")
    textFormat(trailer_label, 12, "bold")
    trailer_label.draw(win)

    trailer_value = Text(Point(39, bar_height(trailer) + 2), trailer)
    textFormat(trailer_value, 12, "bold")
    trailer_value.draw(win)

    retriever_bar = Rectangle(Point(50, 20), Point(69, bar_height(retriever)))
    retriever_bar.setFill("yellowgreen")
    retriever_bar.draw(win)

    retriever_label = Text(Point(59, 18), "Retriever")
    textFormat(retriever_label, 12, "bold")
    retriever_label.draw(win)

    retriever_value = Text(Point(59, bar_height(retriever) + 2), retriever)
    textFormat(retriever_value, 12, "bold")
    retriever_value.draw(win)

    exclude_bar = Rectangle(Point(70, 20), Point(89, bar_height(exclude)))
    exclude_bar.setFill("salmon")
    exclude_bar.draw(win)

    exclude_label = Text(Point(79, 18), "Exclude")
    textFormat(exclude_label, 12, "bold")
    exclude_label.draw(win)

    exclude_value = Text(Point(79, bar_height(exclude) + 2), exclude)
    textFormat(exclude_value, 12, "bold")
    exclude_value.draw(win)

    win.getMouse()


def saveToList():
    
    global main_list
    global data_list

    data_list.append(status)
    data_list.append(pass_credits)
    data_list.append(defer_credits)
    data_list.append(fail_credits)
    main_list.append(data_list)
    data_list = []


def showListData():

    global main_list

    for item in main_list:
        print(item[0], "- ", end="")
        print(*(item[1:]), sep=", ")


def writeFile():
    global main_list

    with open("details.txt", "w") as file:
        for item in main_list:
            data = (f"{item[0]} - {item[1]}, {item[2]}, {item[3]}\n")
            file.write(str(data))


def viewFile():

    with open("details.txt", "r") as file:
        data = file.read()
    print(data)


# MainProgramme

loop_condition = "y"
while True:
    if loop_condition == "y":
        pass_credits = input("Enter your total PASS credits: ")
        pass_credits = inputValidate(pass_credits)

        defer_credits = input("Enter your total DEFER credits: ")
        defer_credits = inputValidate(defer_credits)

        fail_credits = input("Enter your total FAIL credits: ")
        fail_credits = inputValidate(fail_credits)

        progressionLevel()

        if total_credits == 120:
            total_input = total_input + 1

            saveToList()
            writeFile()

        userInput()

    elif loop_condition == "q":

        graphicHistogram()
        showListData()

        print()

        viewFile()

        break

    else:
        print("----Enter 'y' for yes or 'q' to quit and view results----")
        userInput()
