def generate_truth_table():
    print(f"{'P':<6} | {'Q':<6} | {'P AND Q':<10} | {'P OR Q':<10} | {'P -> Q':<10}")
    print("-" * 55) # head for dm study tool

    #boolean combinations for p and q
    #dm tests every possible t or f pair
    for p in [True, False]:
        for q in [True, False]:
            p_and_q = p and q
            p_or_q = p or q
            
            p_implies_q = (not p) or q 

            print(f"{str(p):<6} | {str(q):<6} | {str(p_and_q):<10} | {str(p_or_q):<10} | {str(p_implies_q):<10}")

if __name__ == "__main__":
    print("--- Discrete Mathematics 1: Logic Truth Table ---")
    generate_truth_table()