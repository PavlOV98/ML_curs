import iris
import random

def ret_sort(ret):
    return ret[1]

def update_min_max(min_arg,max_arg,buf=iris.Iris):
    if (buf.petal_length<min_arg[0]):
        min_arg[0]=buf.petal_length
    if (buf.petal_width<min_arg[1]):
        min_arg[1]=buf.petal_width
    if (buf.sepal_length<min_arg[2]):
        min_arg[2]=buf.sepal_length
    if (buf.sepal_width<min_arg[3]):
        min_arg[3]=buf.sepal_width

    if (buf.petal_length>max_arg[0]):
        max_arg[0]=buf.petal_length
    if (buf.petal_width>max_arg[1]):
        max_arg[1]=buf.petal_width
    if (buf.sepal_length>max_arg[2]):
        max_arg[2]=buf.sepal_length
    if (buf.sepal_width>max_arg[3]):
        max_arg[3]=buf.sepal_width

def knn(study_per_type,neigbors):
    total = 150
    f = open('iris.data', 'r')

    all_list=[]
    Setosa=[]
    Versicolour=[]
    Virginica=[]



    line = f.readline()
    buf = iris.Iris(line, 0)
    all_list.append(buf)
    if buf.type == 'Iris-setosa':
        Setosa.append(buf)
    elif buf.type == 'Iris-versicolor':
        Versicolour.append(buf)
    else:
        Virginica.append(buf)

    min_arg = [buf.petal_length,buf.petal_width,buf.sepal_length,buf.sepal_width]
    max_arg = [buf.petal_length, buf.petal_width, buf.sepal_length, buf.sepal_width]

    for i in range(1,total):
        line = f.readline()
        buf=iris.Iris(line,i)
        update_min_max(min_arg,max_arg,buf)
        all_list.append(buf)
        if buf.type=='Iris-setosa':
            Setosa.append(buf)
        elif buf.type=='Iris-versicolor':
            Versicolour.append(buf)
        else:
            Virginica.append(buf)

    f.close()

    for i in all_list:
        i.normilise(min_arg,max_arg)


    Study=[]
    random.shuffle(Setosa)
    random.shuffle(Versicolour)
    random.shuffle(Virginica)
    for i in range(study_per_type):
        Study.append(Setosa.pop())
        Study.append(Versicolour.pop())
        Study.append(Virginica.pop())


    Classify=Setosa+Versicolour+Virginica


    for i in Classify:
        range_vec=[]
        for b in Study:
            range_vec.append(iris.Check(b,i))
        range_vec.sort(key=iris.keyFunc,reverse = True)

        res=[['Iris-setosa',0],['Iris-versicolor',0],['Iris-virginica',0]]

        range_vec=range_vec[:neigbors]

        """
        for b in range_vec:
            print(b,end=' ')
        print()
        """
        for b in range_vec:
            for c in res:
                if b.type==c[0]:
                    if (b.len==0):
                        c[1] = c[1] + 1
                    else:
                        c[1]=c[1]+1/b.len

        res.sort(key=ret_sort,reverse = True)
        #print(res)

        i.new_type=res[0][0]


    fail=0
    for i in Classify:
        if (i.type!=i.new_type):
            fail=fail+1

    #print(classifed,fail,sep=' ')
    return fail


f=open("otput.txt","w")
f.write("study\tneghbors\tfail\n")
for study_per_type in (13,14,15):
    for neigbors in range(20,45):
        fail=knn(study_per_type,neigbors)
        f.write(study_per_type.__str__()+"\t"+neigbors.__str__()+"\t"+fail.__str__()+"\n")
f.close()

"""
f=open("otput_n_s.txt","w")
f.write("neghbors\tstudy\tfail\n")
for neigbors in range(5,30):
    for study_per_type in range(2,5):
        fail=knn(study_per_type,neigbors)
        f.write(neigbors.__str__()+"\t"+study_per_type.__str__()+"\t"+fail.__str__()+"\n")
f.close()
"""