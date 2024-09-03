list1 = [
    "Q1. Where is the Taj Mahal located?",
    "Q2. What is the capital of India?",
    "Q3. How many states are there in India?",
    "Q4. What is the national sport of India?",
    "Q5. What is the largest state in India by area?",
    "Q6. What is the national animal of India?",
    "Q7. What is the national bird of India?",
    "Q8. Who is known as the Father of the Nation in India?",
    "Q9. What is the national flower of India?",
    "Q10. Which river is known as the Ganga's twin?",
    "Q11. What is the national fruit of India?",
    "Q12. What is the currency of India?",
    "Q13. Which monument is called the 'Black Taj'?",
    "Q14. What is the national tree of India?",
    "Q15. What is the primary language spoken in India?",
    "Q16. Which is the smallest state in India by area?",
    "Q17. What is the name of India's national anthem?",
    "Q18. Which ocean borders India to the south?",
    "Q19. What is the national aquatic animal of India?",
    "Q20. What is the official residence of the President of India?",
    "Q21. Which city is known as the Pink City?",
    "Q22. Which festival is known as the Festival of Lights?",
    "Q23. Who wrote the Indian national anthem?",
    "Q24. Which state in India is known for its backwaters?",
    "Q25. What is the highest civilian award in India?"
]

list2 = [
    "A)Mumbai B)Agra C)Rajkot D)Jamnagar",
    "A)Delhi B)Goa C)Punjab D)Jamnagar",
    "A)23 B)65 C)32 D)29",
    "A)Cricket B)Hockey C)Kabaddi D)Handball",
    "A)Rajasthan B)Maharashtra C)Uttar Pradesh D)Madhya Pradesh",
    "A)Tiger B)Lion C)Elephant D)Peacock",
    "A)Peacock B)Parrot C)Eagle D)Crow",
    "A)Mahatma Gandhi B)Jawaharlal Nehru C)Subhash Chandra Bose D)Sardar Patel",
    "A)Lily B)Lotus C)Rose D)Sunflower",
    "A)Yamuna B)Godavari C)Narmada D)Brahmaputra",
    "A)Mango B)Apple C)Banana D)Grapes",
    "A)Rupee B)Dollar C)Euro D)Pound",
    "A)Hawa Mahal B)Red Fort C)Jama Masjid D)Bibi Ka Maqbara",
    "A)Neem B)Peepal C)Banyan D)Mango",
    "A)Hindi B)English C)Tamil D)Telugu",
    "A)Sikkim B)Goa C)Tripura D)Nagaland",
    "A)Jana Gana Mana B)Vande Mataram C)Sare Jahan Se Accha D)Ae Mere Watan Ke Logon",
    "A)Pacific B)Atlantic C)Indian D)Arctic",
    "A)Dolphin B)Shark C)Whale D)Otter",
    "A)Rashtrapati Bhavan B)Parliament House C)Prime Minister's House D)Supreme Court",
    "A)Jaipur B)Udaipur C)Jodhpur D)Bikaner",
    "A)Holi B)Diwali C)Eid D)Christmas",
    "A)Rabindranath Tagore B)Bankim Chandra Chatterjee C)Sarojini Naidu D)Subhash Chandra Bose",
    "A)Kerala B)Goa C)Tamil Nadu D)Karnataka",
    "A)Padma Shri B)Bharat Ratna C)Padma Bhushan D)Padma Vibhushan"
]

list3 = [
    "B", "A", "D", "B", "A", "A", "A", "A", "B", "A", "A", "A", "D", "C", "A", "B", "A", "C", "A", "A", "A", "B", "A", "A", "B"
]

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

