Avrg_grade = []
passed = 0
total = 0

while True:
   input_grade = (input("Enter your grade(type 'done' to finish): "))
   if input_grade.isdigit():
        input_grade = int(input_grade)
        if input_grade <=40 or input_grade >=100:
            print("Invalid grade")
            break
        else:
            Avrg_grade.append(input_grade)
            total += 1
            if input_grade >= 75:
                 passed += 1
   elif input_grade.lower() =='done':
        result = sum(Avrg_grade) / len(Avrg_grade)
        passing_percentage = passed/total*100
        print(f"Average Grade: {result:.2f}")
        print(f"Total passed: {passed}") 
        print(f"passing percentage {passing_percentage:.2f}")
        break
   else:
        print("Invalid input")
    


        
        
        
        
        
 
