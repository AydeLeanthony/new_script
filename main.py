from openpyxl import Workbook, load_workbook
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



book = load_workbook('action.xlsx')
sheet = book.active
x = []
y = []
z = []
triple = [] #данные для временного ряда
time = []

counter = 0
save = 0

size = 3 # размер точек


#Добавить все действия и положения
action = ["Бег","Хотьба","прыжек"]
located = ["задний корман", "Передний корман"]
all = []

for i in action:
    for j in located:
        all.append("\n"+i+"/"+j)

for row in sheet.values:
    if row[6] == save :
        add_triple = [] #лист для добавления данных 

        # берем данные по осям x y z
        add_action = all[save]
        cell_x = float(row[1])
        cell_y = float(row[2])
        cell_z = float(row[3])
    
        #добавляем данные в лист
        x.append(cell_x)
        y.append(cell_y)
        z.append(cell_z)

        # добавляем данные для временных рядов
        add_triple.append(cell_x)
        add_triple.append(cell_y)
        add_triple.append(cell_z)

        triple.append(add_triple)
  
  
        time.append(counter) #колонка с временем ( row[4] )
        counter +=1

        # if counter ==100:
        #     break
    else:
        # print(x)
        
        fig, ax = plt.subplots()
        plt.title("График по X"+ add_action)
        ax.scatter(time,x,size) 
        plt.savefig(f"Experiment_{save}_x")

        fig, ax = plt.subplots()
        plt.title("График по Y"+ add_action)
        ax.scatter(time,y,size) 
        plt.savefig(f"Experiment_{save}_y")

        fig, ax = plt.subplots()
        plt.title("График по Z"+ add_action)
        ax.scatter(time,z,size) 
        plt.savefig(f"Experiment_{save}_z") 

        #     break
        save +=1

