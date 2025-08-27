
TICK = "✅"
CROSS = "❌"


questions = [
    {
        "question": "ENGLISH: What is the synonym of stress?",
        "choices": ["Sad", "Angry", "Joyful", "Tired"],
        "correct_index":  3 
    },
    {
        "question": "What is the past tense of 'eat'?",
        "choices": ["Eated", "Ate", "Eats", "Eating"],
        "correct_index": 1  
    },
    {
        "question":"The past form of cut is?",
        "choices":["cut","cuted","cutes","cute"],
        "correct_index":0
    },
    {
        "question":"___used an ing form",
        "choices":["infinitive","gerund","past tense","present tense"],
        "correct_index":1
    },
    {
        "question":"what is the synonym of popular",
        "choices":["affection","person","eminent","Love"],
        "correct_index":2
    },
        
    {
        "question": "MATH: What is 9 + 5?",
        "choices": ["12", "10", "14", "11"],
        "correct_index":2  
    },
    {
        "question": "What is 9 × 4?",
        "choices": ["27", "18", "21", "36"],
        "correct_index":3  
    },
    {
        "question":"what is the slope of two point A(2,3) and B(1,6)?",
        "choices":["2","1","4","3"],
        "correct_index":3
    },
    {
        "question":"whic one of the following is the volume of sphere",
        "choices":["4πr²","4/3πr²","2πr²/3","2πr²"],
        "correct_index":1
    },
        
        
    {
        "question": " CHEMISTRY: The most reason in bond formation is?",
        "choices":["noble gas electronic structure","lowering energy","electrostatic attraction","electron pair sharing"],
        "correct_index":0
    },
    {
        "question":"which one of the following under goes both oxidation and reduction in a single reaction(disproportional reaction?",
        "choices":["Cl2","Mg","Nacl","H2"],
        "correct_index":0
    },
    {
        "question":"Dalton states that Atom is?",
        "choices":["divisible","continues","indistructible","distructible"],
        "correct_index":2
    },
    {
        "question":"which one is the monomer of natural rubber?",
        "choices":["venyl chloride","neoperene","isoperene","propylene"],
        "correct_index":2
    },
    {
        "question":"which one of the following is the monomer of synthetic rubber?",
        "choices":["venyl chloride","neoperene","isoperene","propylene"],
        "correct_index":1
    },
    {
        "question":" PHYSICS: which one of the following is not the unit of magnetic flux?",
        "choices":["weber","B/A","T/m²","m/s"],
        "correct_index":3
    },
    {
        "question":"which one the follwing is not the equivalent of three resistor R1=1ohm,R2=2ohm,R3=3ohm?",
        "choices":["11/3","9/2","3","6"],
        "correct_index":2
    },
    {
        "question":"The man move toward east at 5m/s and the car move toward to the ease at 7m/s,what is the relative velocity?",
        "choices":["3","5","2","12"],
        "correct_index":3
    },
    {
        "question":"which one of the follwing is condition is write in elastic collision?",
        "choices":["M1V1-M2V2=M1V1+M2V2","(V1-V2)=(V1-V2)","(V1+V2)=(V1+V2)","(V1-V2)=-(V1-V2)"],
        "correct_index":3
    },
    {
        "question":"The circuit have 4ohm in the cell and 6ohm resistorand the current of the circut is 2A.what is the Electromotive force?",
        "choices":["8V","13V","20V","12V"],
        "correct_index":2
    },
    {
        "question":" BIOLOGY: if the cell lose his lysosome which organelle is primarly affect?",
        "choices":["cytoplasm"," smoth endoplasmic reticullum","Rogh endoplasmic reticullum","Golgi apparatus"],
        "correct_index":3
    },
    {
        "question":"which one is the junction between two neuron?",
        "choices":["dendrite","synapse","axon","cell body"],
        "correct_index":1
    },
    {
        "question":"a part os pheripheral nervuos system regulating involuntary body",
        "choices":["Autonomic nervous system","sympatric nervous system","somatic system","para sympathetic nervous system"],
        "correct_index":0
    },
    {
        "question":"which one of the following natural resource is an exhaustible",
        "choices":["Mineral","wild life","soil fertility","Aquatic animal"],
        "correct_index":0
    },
    {
        "question":"one of the following is different from the other",
        "choices":["keratinocytes","melanocytes","langerhans cell","Hallucinogens"],
        "correct_index":3
    },
   {
       "question":"APTITUDE: Which one of the following is an odd?",
       "choices":["famous","eminent","brilliant","popular"],
       "correct_index":2
   },
   {
       "question":"which one is true 7 x 6?",
       "choices":["42","46","39","37"],
       "correct_index":0
   }
       
       
       
        
        
                
    
]


x = ["A", "B", "C", "D"]


score = 0
h=input("enter yuor name: ")

print("Hello",h," WELL COME TO MULTIPLE CHOICE QUIZ - ENGLISH,MATH,CHEMISTRY,PHYSICS,BIOGY AND APTITUDE")
print("============================================================")


for i,q in enumerate(questions, 1):
    print(f"nQ{i}: {q['question']}")
    for idx, choice in enumerate(q["choices"]):
        print(f"   {x[idx]}. {choice}")
    
  
    z = input("Your answer (A, B, C, D ")
    if z in x:
        user_index = x.index(z)
        if user_index == q["correct_index"]:
            print(f"{TICK} Correct!\n")
            score += 1
        else:
                g=x[q["correct_index"]]
                y=q["choices"][q["correct_index"]]
                print(f"{CROSS}Wrong! correct amswer is :{g}.{y}\n" )
    else:
        print(f"{CROSS} Invalid choice. Skipped.\n")
        

print("======================")
print(h,f"your score is:{score}", "out of",len(questions))
print("======================")
if score >= len(questions)*9/2:
    print( h, " Perfect! Excellent job!!!#")
elif score >= len(questions)/2:
    print( h, "👍 Good job! Keep practicing.")
else:
    print( h, "Try again. You’ll get better!")
    # this part is done by Kalid
print("Welcome to General Quiz ")

name = input("Enter your full name ")

print(f"{name}!please follow the following instruction")
print(f"1  do not forget to write your full name ")
print(f" 2 cheating is illegal ")

print(f" 3 {name}!please read the question carefully and answer the question")

print(f" {name}! Get ready for 30 choose questions.\n")

print(" Good Luck ")

questions = [
    "Q1. What is the formula for the area of a rectangle?\n A. Length × Width  B. Length + Width  C. 2 × Length × Width  D. 1/2 × Length × Width",
    "Q2. Solve for x: 3x + 9 = 24\n A. 3  B. 5  C. 7  D. 15",
    "Q3. x² = 64, value of x?\n A. 8  B. -8  C. Both 8 and -8  D. 16",
    "Q4. Perimeter of a square with side 6?\n A. 12  B. 18  C. 24  D. 36",
    "Q5. 15 ÷ 3 + 2 = ?\n A. 5  B. 7  C. 10  D. 12",
    
    "Q6. The basic unit of life is?\n A. Atom  B. Cell  C. Tissue  D. Organ",
    "Q7. Humans have how many chromosomes?\n A. 23  B. 46  C. 44  D. 48",
    "Q8. Photosynthesis produces?\n A. Oxygen  B. Carbon dioxide  C. Water  D. Nitrogen",
    "Q9. Heart pumps?\n A. Air  B. Blood  C. Water  D. Lymph",
    "Q10. Which organ stores bile?\n A. Liver  B. Stomach  C. Gallbladder  D. Kidney",
    
    "Q11. Speed formula is?\n A. Distance × Time  B. Distance ÷ Time  C. Time ÷ Distance  D. Mass × Acceleration",
    "Q12. SI unit of force?\n A. Joule  B. Watt  C. Newton  D. Pascal",
    "Q13. Acceleration due to gravity?\n A. 8.9 m/s²  B. 9.8 m/s²  C. 10.8 m/s²  D. 11.8 m/s²",
    "Q14. Light travels fastest in?\n A. Water  B. Glass  C. Air  D. Vacuum",
    "Q15. 5 workers = 10 days, 10 workers = ?\n A. 20  B. 15  C. 10  D. 5",
    
    "Q16. H2O is?\n A. Oxygen  B. Hydrogen  C. Water  D. Carbon dioxide",
    "Q17. Atomic number of Carbon?\n A. 6  B. 8  C. 12  D. 16",
    "Q18. Which is a noble gas?\n A. Oxygen  B. Helium  C. Nitrogen  D. Hydrogen",
    "Q19. Symbol 'Na' stands for?\n A. Nitrogen  B. Sodium  C. Neon  D. Nickel",
    "Q20. pH of neutral solution?\n A. 0  B. 7  C. 14  D. 1",
    
    "Q21. He __ football yesterday.\n A. play  B. plays  C. played  D. playing",
    "Q22. He was born __ 12 April 2012.\n A. on  B. in  C. at  D. by",
    "Q23. Synonym for angry?\n A. Happy  B. Sad  C. Furious  D. Calm",
    "Q24. Correct article: I saw __ elephant.\n A. a  B. an  C. the  D. none",
    "Q25. Fill in: She is taller __ her brother.\n A. then  B. than  C. as  D. like",
    
    "Q26. Next number: 2, 4, 8, 16, ?\n A. 24  B. 32  C. 64  D. 20",
    "Q27. Odd one: Apple, Orange, Banana, Carrot\n A. Apple  B. Orange  C. Banana  D. Carrot",
    "Q28. 90 ÷ (9+6) = ?\n A. 10  B. 5  C. 6  D. 9",
    "Q29. If 3 pencils cost 15 Rs, 7 pencils cost?\n A. 30  B. 35  C. 25  D. 40",
    "Q30. Clock 3:15 → angle?\n A. 0°  B. 7.5°  C. 45°  D. 90°"
]

answers = {
    1:"A", 2:"B", 3:"C", 4:"C", 5:"B",
    6:"B", 7:"B", 8:"A", 9:"B", 10:"C",
    11:"B", 12:"C", 13:"B", 14:"D", 15:"C",
    16:"C", 17:"A", 18:"B", 19:"B", 20:"B",
    21:"C", 22:"A", 23:"C", 24:"B", 25:"B",
    26:"B", 27:"D", 28:"C", 29:"B", 30:"B"
}

score = 0

for i in range(30):
    print(questions[i])
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    
    while user_ans not in ['A','B','C','D']:
        user_ans = input("Please enter A, B, C, or D: ").strip().upper()
   
    if user_ans == answers[i+1]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {answers[i+1]}\n")

print(f"Quiz finished! Your score: {score}/30")
if score >= 25:
    print("Excellent! ")
elif score >= 20:
    print("Very Good! ")
elif score >= 15 :
    print("Good !")
elif score >=10:
    print("not bad")
else:
    print("you fail please study")
    
 
print ("developed by Kalid F")
