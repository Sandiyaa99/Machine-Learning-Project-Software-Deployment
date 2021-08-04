#SOFTWARE FOR CLASSIFICATION,REGRESSION AND CLUSTERING
#IMPORTING LIBRARIES
import tkinter
from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB

from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix

import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

class pages:
    
#TO BROWSE DATASET
    def page1(self):
        page1 = Tk()

        label1 = Label(page1,text="ML Algorithms Software", bg="#80e5ff",fg='#000000', font=("Vivaldi",16,'bold'))
        label1.pack(pady=20)

        label2 = Label(page1, text="Upload your Dataset",bg="#ccffe6", fg='#000000', font=("Arial Black", 14, 'bold'))
        label2.pack(pady=20)

        def browse_data():
            global input, data
            input = filedialog.askopenfilename(initialdir="/",filetypes = [("csv files","*.csv")])
            data = pd.read_csv(input)
            entry1.insert(0, input)

        entry1 = Entry(page1,bd=3)
        entry1.place(x=130, y=200, height=30, width=380)

        button1 = Button(page1, text='Browse dataset',bg="#b3ff99", fg="#000000", command=lambda: browse_data())
        button1.place(x=500, y=200, height=30, width=90)

        button2 = Button(page1, text='Continue', bg="#9999e6",command=p.page2)
        button2.place(x=300, y=350, height=40, width=80)

        page1.configure(bg="#ffddcc")
        page1.geometry("700x500+100+10")
        page1.title("Page1-Browse your dataset")
        page1.mainloop()

#TO CONFIRM DATASET
    def page2(self):
        page2 = Tk()

        label3 = Label(page2, text="Confirm your dataset", bg="#ccffe6", fg='#000000', font=("Arial Black", 16, 'bold'))
        label3.pack(pady=20)

        frame = Frame(page2)
        frame.pack(padx=20)

        scroll1 = ttk.Scrollbar(frame, orient='vertical')
        scroll1.pack(side=RIGHT, fill=Y)

        scroll2 = ttk.Scrollbar(frame, orient='horizontal')
        scroll2.pack(side=BOTTOM, fill=X)

        global tview
        tview = ttk.Treeview(frame, yscrollcommand=scroll1.set, xscrollcommand=scroll2.set)
        tview.pack()

        scroll1.config(command=tview.yview)
        scroll2.config(command=tview.xview)

        tview["column"] = list(data.columns)
        tview["show"] = "headings"

        for column in tview["column"]:
            tview.heading(column, text=column)

        df_rows = data.to_numpy().tolist()
        for row in df_rows:
            tview.insert("", "end", values=row)
        tview.pack()

        button3 = Button(page2, text='yes',bg="#b3ffb3",command=p.page3)
        button3.place(x=280,y=350,width=90)

        button4 = Button(page2, text='no', bg="#ffb3b3", command=p.page1)
        button4.place(x=380,y=350,width=90)

        page2.configure(bg="#ffddcc")
        page2.title("Page2-Confirming data")
        page2.geometry("800x700+100+10")
        page2.mainloop()
#TO CHOOSE FEATURES
    def page3(self):
        page3 = Tk()

        label31 = Label(page3, text="Select the Features", fg='#000000',bg="#ccffe6", font=("Arial Black", 18, 'bold'))
        label31.pack()

        label32 = Label(page3, text="Independent Variables", fg='#000000', bg="#ff99ff" ,font=("Vivaldi", 14, 'bold'))
        
        label32.place(x=65,y=40,width=220,height=30)

        label33 = Label(page3, text="Dependent Variables", fg='#000000', bg="#ff99ff", font=("Vivaldi", 14, 'bold'))
       
        label33.place(x=65,y=260,width=220,height=30)

        frame1 = Frame(page3)
        frame1.place(x=65,y=75,width=220,height=150)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=BOTH )


        listbox1 = Listbox(frame1, selectmode=MULTIPLE)
        listbox1.config(yscrollcommand=scrollbar1.set)
        listbox1.place(width=205, height=150)

        scrollbar1.config(command=listbox1.yview)

        j=0
        for i in tview["column"]:
            listbox1.insert(j, i)
            j = j + 1

        frame2 = Frame(page3)
        frame2.place(x=65, y=295, width=220, height=150)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT, fill=BOTH)


        listbox2 = Listbox(frame2, selectmode=SINGLE)
        listbox2.config(yscrollcommand=scrollbar2.set)
        listbox2.place(width=205, height=170)

        scrollbar2.config(command=listbox2.yview)

        j = 0
        for i in tview["column"]:
            listbox2.insert(j, i)
            j = j + 1


        def indep_select():
            global indep, indep1
            indep = []
            indep1 = []
            label34 = Label(page3, text="Independent Variables :",bg="#b3b3ff")
            label34.place(x=300, y=40)
            clicked = listbox1.curselection()
            z = 70
            for item in clicked:
                label10 = Label(page3, text=listbox1.get(item),bg="#ff471a")
                label10.place(x=300, y=z)
                indep.append(item)
                indep1.append(listbox1.get(item))
                z = z + 15


        button31 = Button(page3,text="Choose",fg="#ffffff",bg="#004d00",command=indep_select,font=("Arial Black", 8, 'bold'))
        button31.place(x=140,y=225,width=60, height=30)

        def dep_select():
            global dep,dep1
            dep = []
            dep1 = []
            label34 = Label(page3, text="Dependent Variables :",bg="#b3b3ff")
            label34.place(x=320, y=260)
            clicked = listbox2.curselection()
            z = 300
            for item in clicked:
                label10 = Label(page3, text=listbox2.get(item),bg="#ff471a")
                label10.place(x=320, y=z)
                dep.append(item)
                dep1.append(listbox2.get(item))
                z = z + 15


        button32 = Button(page3, text="Choose",fg="#ffffff",bg="#004d00", command=dep_select,font=("Arial Black", 8, 'bold'))
        button32.place(x=140, y=450, width=60, height=30)

        button33 = Button(page3, text = "Submit",fg="#ffffff",bg="#004d00",command=p.page4,font=("Arial Black", 8, 'bold'))
        button33.place(x=320, y=460, height=30, width=180)

        page3.configure(bg="#ffddcc")
        page3.title("Page3-Choosing Feature")
        page3.geometry("800x500+100+10")
        page3.mainloop()
#TO SELECT PROBLEM
    def page4(self):
        page4 = Tk()

        label31 = Label(page4, text="Select the Problem Type", fg='#000000', bg="#ccffe6", font=("Arial Black", 16, 'bold'))
        label31.place(x=200,y=100,height=35)

        button31 = Button(page4, text="Regression", bg="#ff66cc", fg="#ffffff",command=p.regression)
        button31.place(x=90,y=250,width=130,height=40)

        button31 = Button(page4, text="Classification", bg="#ff66cc", fg="#ffffff",command=p.classification)
        button31.place(x=290,y=300,width=130,height=40)

        button31 = Button(page4, text="Clustering", bg="#ff66cc", fg="#ffffff", command=p.clustering)
        button31.place(x=490,y=350,width=130,height=40)

        page4.configure(bg="#ffddcc")
        page4.title("Page4-Selecting Problem")
        page4.geometry("700x500+100+10")
        page4.mainloop()

#REGRESSION ALGORITHM
    def regression(self):
        page5 = Tk()
        global algos
        
        algos="Regression"

        label3 = Label(page5, text="SELECT THE ALGORITHM", fg='#000000', bg="#ccffe6", font=("Arial Black", 16,"bold"))
        label3.pack(pady=10)

        def comboclick(event):
            X = data.iloc[:, indep].values  
            y = data.iloc[:, dep].values                   
            
            if (combo.get() == "Simple Linear Regression"):                                
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=1)
                              
                # Fitting the simple linear regression model to the training dataset               
                global regressor
                regressor = LinearRegression()
                regressor.fit(X_train, y_train)                          
                global acc
                acc = regressor.score(X_train, y_train)              

            elif (combo.get() == "Multiple Linear Regression"):               

                # Splitting the dataset into training and test set.
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

                regressor = LinearRegression()
                regressor.fit(X_train, y_train)                
                acc = regressor.score(X_train, y_train)
                

            elif (combo.get() == "Polynomial Regression"):               
                # Training the dataset in polynomial regression
                from sklearn.preprocessing import PolynomialFeatures
                global poly_reg
                
                poly_reg = PolynomialFeatures(degree=5) 
                x_poly = poly_reg.fit_transform(X)
                
                regressor = LinearRegression()
                regressor.fit(x_poly, y)               
                acc = regressor.score(x_poly,y)
               

            elif(combo.get()=="SVM Regression"):               
                global sc_X,sc_y
                sc_X = StandardScaler()
                sc_y = StandardScaler()
                X = sc_X.fit_transform(X)
                y = sc_y.fit_transform(y)

                regressor = SVR(kernel='rbf')
                regressor.fit(X,y)
                y_pred=regressor.predict(X_test)

                acc = regressor.score(X,y)
               
                

            elif(combo.get()=="Decision Tree Regression"):               
                regressor = DecisionTreeRegressor(random_state=0)
                regressor.fit(X,y)

                acc = regressor.score(X,y)
                y_pred=regressor.predict(X_test)

            elif(combo.get()=="Random Forest Regression"):             
                regressor = RandomForestRegressor(n_estimators=10,random_state=0)
                regressor.fit(X,y)

                acc=regressor.score(X,y)
                y_pred=regressor.predict(X_test)
            else:
                    pred = regressor.predict([result])
                    label64 = Label(page6,text="Click next to view the Prediction")
                    label64.place(x=260,y=z+100)

        options = ["Simple Linear Regression", "Multiple Linear Regression", "Polynomial Regression","SVM Regression","Decision Tree Regression","Random Forest Regression"]
        global combo
        combo = ttk.Combobox(page5, value=options)
        combo.config(width=50)
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", comboclick)
        combo.pack()

        button6 = Button(page5, text='Train Model', bg="#0033cc", fg="#ffffff", command=p.page6)
        button6.pack(pady=20)

        page5.configure(bg="#ffddcc")
        page5.title("Page5-Regression Algorithm")
        page5.geometry("700x500+100+10")
        page5.mainloop()

#CLASSIFICATION ALGORITHM
    def classification(self):
        page8 = Tk()

        global algos
        algos="Classification"

        label3 = Label(page8, text="SELECT THE ALGORITHM", fg='#000000', bg="#ccffe6", font=("Arial Black", 16,"bold"))
        label3.pack(pady=10)

        def comboclick1(event):
            X = data.iloc[:, indep].values
            y = data.iloc[:, dep].values

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            global sc
            sc = StandardScaler()
            X_train = sc.fit_transform(X_train)
            X_test = sc.transform(X_test)

            if(combo2.get()=="Logistic Regression"):               
                global classifier
                classifier = LogisticRegression(random_state=0)
                classifier.fit(X_train,y_train)

                y_pred = classifier.predict(X_test)

                cm = confusion_matrix(y_test,y_pred)
                global acc
                acc = (sum(np.diag(cm))/len(y_test))

            elif(combo2.get()=="Naive Bayes Classification"):             
                classifier = GaussianNB()
                classifier.fit(X_train ,y_train)

                y_pred = classifier.predict(X_test)

                cm = confusion_matrix(y_test,y_pred)
                acc = (sum(np.diag(cm))/len(y_test))

            elif(combo2.get()=="K-Nearest Neighbour Classification"):                
                classifier = KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)
                classifier.fit(X_train,y_train)

                y_pred = classifier.predict(X_test)

                cm = confusion_matrix(y_test,y_pred)
                acc = sum(np.diag(cm))/len(y_test)

            elif(combo2.get()=="SVM Classification"):              
                classifier = SVC(kernel='rbf',random_state=0)
                classifier.fit(X_train,y_train)

                y_pred=classifier.predict(X_test)

                cm = confusion_matrix(y_test,y_pred)
                acc = sum(np.diag(cm))/len(y_test)

            elif(combo2.get()=="Decision Tree Classification"):
                classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
                classifier.fit(X_train,y_train)

                y_pred = classifier.predict(X_test)

                cm = confusion_matrix(y_test,y_pred)
                acc = sum(np.diag(cm))/len(y_test)

            elif(combo2.get()=="Random Forest Classification"):
                classifier = RandomForestClassifier()
                classifier.fit(X_train,y_train)

                y_pred = classifier.predict(X_test)
                cm = confusion_matrix(y_test,y_pred)
                acc = sum(np.diag(cm))/len(y_test)

        options1 = ["Logistic Regression","Naive Bayes Classification","K-Nearest Neighbour Classification","SVM Classification","Decision Tree Classification","Random Forest Classification"]
        global combo2
        combo2 = ttk.Combobox(page8, value=options1)
        combo2.config(width=50)
        combo2.current(0)
        combo2.bind("<<ComboboxSelected>>", comboclick1)
        combo2.pack()

        button6 = Button(page8, text='Train Model', bg="#0033cc", fg="#ffffff",command=p.page6)
        button6.pack(pady=20)

        page8.configure(bg="#ffddcc")
        page8.geometry("700x500+100+10")
        page8.title("Page8-Classification Algorithm")
        page8.mainloop()

#CLUSTERING ALGORITHM
    def clustering(self):
        page9 = Tk()
        global algos
        algos = "clustering"

        label31 = Label(page9, text="SELECT THE ALGORITHM", fg='#000000', bg="#ccffe6", font=("Arial Black", 16,"bold"))
        label31.pack(pady=10)

        def comboclick2(event):
            X = data.iloc[:, indep].values
            if(combo3.get()=="KMeans Clustering"):

                wcss=[]

                for i in range(1,11):
                    kmeans = KMeans(n_clusters=i,random_state=0)
                    kmeans.fit(X)
                    wcss.append(kmeans.inertia_)
                def plot():
                    
                    plt.figure(figsize = (8,5), dpi=50)
                    plt.scatter(range(1,11),wcss)
                    plt.plot(range(1,11),wcss)
                    plt.title("Elbow Method")
                    plt.xlabel("Number of Clusters")
                    plt.ylabel("WCSS")
                    plt.show()

                button91 = Button(page9, text="Click to view the plot", command=plot)
                button91.place(x=290,y=80)

                
            elif(combo3.get()=="Hierarchical Clustering"):

                def plot1():
                    plt.figure(figsize=(8,5),dpi=50)
                    dendrogram = sch.dendrogram(sch.linkage(X,method='ward'))
                    plt.title("Dendrogram")
                    plt.xlabel("X-Values")
                    plt.ylabel("Euclidean Distance")
                    plt.show()

                button91 = Button(page9, text="Click to view the plot", command=plot1)
                button91.place(x=290, y=80)

                

        options2 = ["KMeans Clustering","Hierarchical Clustering"]
        global combo3
        combo3 = ttk.Combobox(page9, value=options2)
        combo3.config(width=50)
        combo3.current(0)
        combo3.bind("<<ComboboxSelected>>", comboclick2)
        combo3.pack()

        page9.configure(bg="#ffddcc")
        page9.geometry("700x500+100+10")
        page9.title("Page5-Clustering Algorithm")
        page9.mainloop()
        
#PREDICTION
    def page6(self):
        page6 = Tk()

        label61 = Label(page6, text="Index Name", fg='#000000', bg="#ffcccc", font=("Arial Black", 20, 'bold'))
        label61.place(x=150, y=100, height=30)

        z=140
        global entry61, entries
        entries = []
        for i in indep1:
            label63 = Label(page6, text=i, fg='#000000', bg="#ffffff", font=("Arial Black", 15, 'bold'))
            label63.place(x=145, y=z)

            entry61 = Entry(page6)
            entry61.place(x=420, y=z, height=30, width=150)
            entries.append(entry61)
            z = z + 25

        label62 = Label(page6, text="Index Values", fg='#000000', bg="#ffcccc", font=("Arial Black", 20, 'bold'))
        label62.place(x=415, y=90)

        def predict():
            global result
            result=[]
            for entry in entries:
                result.append(entry.get())

            if(algos=="Regression"):
                global pred
                
                if(combo.get()=="Simple Linear Regression"):
                    pred=regressor.predict(LinearRegression([result]))
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)
                    
                elif(combo.get()=="Multiple linear Regression"):
                    pred=regressor.predict([result])
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)
                    
                elif(combo.get()=="Polynomial Regression"):
                    pred = regressor.predict(poly_reg.fit_transform([result]))
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)

                elif(combo.get()=="SVM Regression"):
                    pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([result])))
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)

                else:#Decision tree regression and random forest regression
                    pred = regressor.predict([result])
                    label64 = Label(page6)
                    label64.place(x=260,y=z+100)

            elif(algos=="Classification"):
                if (combo2.get() == "Logistic Regression"):
                    pred = classifier.predict(sc.transform([result]))
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)
                    
                elif(combo2.get()=="K-Nearest Neighbour Classification" or combo2.get()=="SVM Classification" or combo2.get()=="Decision Tree Classification" or combo2.get()=="Random Forest Classification"):
                     pred = classifier.predict(sc.transform([result]))
                     label64 = Label(page6)
                     label64.place(x=260, y=z + 100)
                    
                elif(combo2.get()=="Naive Bayes Classification"):
                    pred = classifier.predict(sc.transform([result]))
                    label64 = Label(page6)
                    label64.place(x=260, y=z + 100)
                    
            else:
                    pred = model.predict([result])
                    label64 = Label(page6)
                    label64.place(x=260,y=z+100)
                


        button61 = Button(page6, text="Predict", bg="#99ff99", fg="#ffffff", command=lambda:[predict(),p.page7()])
        button61.place(x=300,y=z+50)

        page6.configure(bg="#ffddcc")
        page6.geometry("700x500+100+10")
        page6.title("Page6-Prediction")
        page6.mainloop()
        
#OUTPUT
    def page7(self):
        page7 = Tk()

        if(algos=="Regression"):
            

            label71 = Label(page7,text="Summary", bg="#ccffe6", fg="#000000", font=("Arial Black", 20, 'bold'))
            label71.place(x=200,y=100,width=300,height=30)

            label72 = Label(page7, text="Prediction Result", bg="#66ccff", fg="#000000",font=("Arial Black", 15, 'bold'))
            label72.place(x=140,y=200,width=200,height=30)

            label73 = Label(page7, text="Accuracy", bg="#66ccff", fg="#000000", font=("Arial Black", 15, 'bold'))
            label73.place(x=140, y=300, width=200, height=30)

            label74 = Label(page7, text=("{:.2f}".format(acc)), bg="#07a81f", fg="#000000")
            label74.place(x=460, y=300, width=100, height=30)

            pred1 = float(pred)
            pred1 = "{:.2f}".format(pred1)

            label75 = Label(page7, text=pred1, bg="#07a81f", fg="#000000")
            label75.place(x=460, y=200, width=100, height=30)

            button71 = Button(page7,text="Back",bg="#ff3300",fg="#000000",command=p.page6)
            button71.place(x=70,y=400,width=90)

            button72 = Button(page7, text="Start New",bg="#ff3300",fg="#000000",command=p.page1)
            button72.place(x=530, y=400,width=100)

        elif(algos=="Classification"):
            label71 = Label(page7, text="Summary", bg="#ccffe6", fg="#000000", font=("Arial Black", 20, 'bold'))
            label71.place(x=200, y=100, width=300, height=30)

            label72 = Label(page7, text="Prediction Result", bg="#00ddff", fg="#000000",
                            font=("Arial Black", 15, 'bold'))
            label72.place(x=140, y=200, width=200, height=30)

            label73 = Label(page7, text="Accuracy", bg="#00ddff", fg="#000000", font=("Arial Black", 15, 'bold'))
            label73.place(x=140, y=300, width=200, height=30)

            label74 = Label(page7, text=("{:.2f}".format(acc)), bg="#07a81f", fg="#000000")
            label74.place(x=460, y=300, width=100, height=30)


            label75 = Label(page7, text=pred, bg="#07a81f", fg="#000000")
            label75.place(x=460, y=200, width=100, height=30)

            button71 = Button(page7, text="Back", bg="#ff3300", fg="#000000", command=p.page6)
            button71.place(x=70, y=400, width=90)

            button72 = Button(page7, text="Start New", bg="#ff3300", fg="#000000", command=p.page1)
            button72.place(x=530, y=400, width=100)

        

        page7.configure(bg="#ffddcc")
        page7.geometry("700x500+100+10")
        page7.title("Page7-Output")
        page7.mainloop()

p = pages()
p.page1()
