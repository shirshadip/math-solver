def calculator():
    
  
    print("Welcome to the Math Solver!")
    print("Choose a module:")
    choice = input("1. Complex Numbers\n"
                   "2. Sets\n"
                   "3. Permutations\n"
                   "4. combinations\n"
                   "5. vectors\n"
                   "6. quadretic equations\n"
                   "7. sequence and series\n"
                   "Enter your choice (1 or 2 or 3 or 4 or 5 or 6 or 7): ").strip()
    if choice == '1':
        import math_solver.complex_numbers as complex_numbers
        complex_numbers.complex_calculator()
    elif choice == '2':
        import math_solver.sets as sets
        sets.set_calculator()
    elif choice == '3':
        import math_solver.permutation as permutation
        permutation.permutation_calculator()
    elif choice == '4':
        import math_solver.combination as combination
        combination.combination_calculator()
    elif choice== '5':
        import math_solver.vectors as vectors
        vectors.vector_calc()
    elif choice == '6':
        import math_solver.quadretic_equations as quadretic_equations
        quadretic_equations.quadretic()
    elif choice=='7':
        import math_solver.sequence_and_series as sequence_and_series
        sequence_and_series.sec()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")

calculator()