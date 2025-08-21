
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
    
