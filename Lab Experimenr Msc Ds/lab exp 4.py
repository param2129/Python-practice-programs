#Sales analysis for based on sales data and interpretations using set operations.
full_dataset={"mobile","TV","Tablet","Robot","Laptop","Speaker","Projector"}
jan={"mobile","TV","Tablet","Robot","Laptop"}
feb={"TV","Robot","Laptop"}
mar={"Laptop","TV"}
apr={"Tablet","Speaker"}
#1 which item sold upto march 
#2 which item sold in jan,feb,mar but not in april 
#3 which item having highest demand
#4 which item has lowest demand
#5 which item is sold in feb but not in mar
#6 which item is sold in jan, feb and march 

#Answers

# 1 
print("1.", jan | feb | mar)
# 2 
print("2.", (jan & feb & mar) - apr)
# 3 
print("3.", jan & feb & mar)
# 4 
print("4.", full_dataset - (jan | feb | mar | apr))
# 5
print("5.", feb - mar)
# 6
print("6.", jan & feb & mar)