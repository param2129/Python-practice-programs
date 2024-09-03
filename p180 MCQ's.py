list1=["Q1. Where Dose Taj Mahal Is Located ?","Q2.What is The Capital Of India ?","Q3.How Many States Are There In India?","Q4.What Is The National Sports Of India?"]
list2=["A)Mumbai B)Agra C)Rajkot D)Jamnagar","A)Delhi B)Goa C)Punjab D)Jamnagar","A)23 B)65 C)32 D)29","A)Cricket B)Hokey C)Kabaddi D)HandBall"]
list3=["B","A","D","B"]
c1=0
c2=0
for i in range(0,len(list1)):
    print(list1[i])
    print(list2[i])
    op=str(input("Enter your answer =>"))
    Answer=list3[i]
    if op==Answer:
        print("correct :")
        c1=c1+1
    else:   
        print("Incorrect :")
        c2=c2+1

print("Right Answer =>",c1)
print("Wrong Answer =>",c2)





