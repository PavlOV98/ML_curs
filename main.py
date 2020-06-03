import iris
import random

def ret_sort(ret):
    return ret[1]

def knn(study_per_type,neigbors):
    total = 150
    f = open('iris.data', 'r')

    all_list=[]
    Setosa=[]
    Versicolour=[]
    Virginica=[]

    for i in range(total):
        line = f.readline()
        buf=iris.Iris(line,i)
        all_list.append(buf)
        if buf.type=='Iris-setosa':
            Setosa.append(buf)
        elif buf.type=='Iris-versicolor':
            Versicolour.append(buf)
        else:
            Virginica.append(buf)

    f.close()

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

    classifed=total-study_per_type*3
    fail=0
    for i in Classify:
        if (i.type!=i.new_type):
            fail=fail+1

    #print(classifed,fail,sep=' ')
    return fail


f=open("otput_s_n.txt","w")
f.write("study\tneghbors\tfail\n")
for study_per_type in range(2,5):
    for neigbors in range(2,30):
        fail=knn(study_per_type,neigbors)
        f.write(study_per_type.__str__()+"\t"+neigbors.__str__()+"\t"+fail.__str__()+"\n")
f.close()

f=open("otput_n_s.txt","w")
f.write("study\tneghbors\tfail\n")
for neigbors in range(2,30):
    for study_per_type in range(2,5):
        fail=knn(study_per_type,neigbors)
        f.write(study_per_type.__str__()+"\t"+neigbors.__str__()+"\t"+fail.__str__()+"\n")
f.close()