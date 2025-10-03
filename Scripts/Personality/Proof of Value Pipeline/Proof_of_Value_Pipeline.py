# %%
def proof_of_value_binary():
    print("Welcome to the Proof of Value Pipeline\n")

    # Step 1: Customer Selection & Sequencing
    print("--- Customer Selection ---")
    print("1. Post/Undergraduate Student")  # Fresh out of College
    print("2. Transitioning Professional")  # Moving into Another Field
    print("3. Business Professional Veteran")  # Professional with Skin In the Game
    print("4. Entrepreneur")  # Gig Economy
    print("5. Contract or Freelance")  # Hybrid
    
    customer_type = input("Select customer type (1-5): ")
    
    # Route to appropriate metric style based on customer
    abstract_skill_scraping = {
        "1": {"name": "Post/Undergraduate Student", "metrics": ["Project-based hours", "Academic projects", "Internship experience"]},
        "2": {"name": "Transitioning Professional", "metrics": ["Transferable skills hours", "Cross-domain projects", "Certification progress"]},
        "3": {"name": "Business Professional Veteran", "metrics": ["Billable hours", "Deliverables count", "Client testimonials"]},
        "4": {"name": "Entrepreneur", "metrics": ["Revenue generated", "Business milestones", "Customer acquisition"]},
        "5": {"name": "Contract or Freelance", "metrics": ["Contract hours", "Project deliverables", "Client portfolio"]}
    }

    selected_route = abstract_skill_scraping.get(customer_type, abstract_skill_scraping["5"])
    print(f"\n Selected: {selected_route['name']}")
    print(f"Available metrics: {', '.join(selected_route['metrics'])}\n")

    # Step 2: Input
    years = int(input("Enter your years of experience: "))
    if years <= 0:
        return " Invalid input: No years provided"
    
    total_hours = years * 2000
    print(f"Step 2: {years} years ≈ {total_hours} hours")

    drivers = input("List your key drivers (e.g., adaptability, curiosity, courage, initiative): ")

    # Step 3: Process - Split Direct vs Indirect Work
    print("\n--- Work Distribution ---")
    direct_ratio = float(input("Direct work ratio (0-1, default=0.6): ") or 0.6)

    # Calculate direct and indirect from total hours
    direct_hours = direct_ratio * total_hours
    indirect_ratio = 1 - direct_ratio
    indirect_hours = indirect_ratio * total_hours

    print(f"Step 3a: Direct work = {direct_hours:.0f} hrs ({direct_ratio*100:.0f}% of total)")
    print(f"Step 3b: Indirect work = {indirect_hours:.0f} hrs ({indirect_ratio*100:.0f}% of total)")
    print(f"Total accounted hours: {direct_hours + indirect_hours:.0f} hrs")

    # Optional: Parametric validation for indirect work
    validate = input("\nValidate indirect hours with parametric estimate? (y/n): ").lower()
    if validate == "y":
        print("--- Parametric Validation ---")
        hours_per_week = float(input("Current hours per week on indirect work: "))
        weeks_per_month = float(input("Weeks per month (typically 4-4.3): ") or 4)

        monthly_hours = hours_per_week * weeks_per_month
        annual_parametric = monthly_hours * 12
        lifetime_parametric = annual_parametric * years

        print(f"Parametric estimate: {lifetime_parametric:.0f} hrs over {years} years")
        print(f"Original indirect: {indirect_hours:.0f} hrs")

        use_parametric = input("Use parametric estimate instead? (y/n): ").lower()
        if use_parametric == "y":
            indirect_hours = lifetime_parametric
            print(f"Updated indirect hours to {indirect_hours:.0f} hrs")

    # Step 4: Checkpoint (routed by customer type)
    print(f"\n--- Proof Validation ({selected_route['name']} route) ---")
    proof_direct = input("Direct proof exists? (y/n): ").lower() == "y"
    if not proof_direct:
        print("Build a Portfolio")
    else:
        print(" Keep Building")
    
    proof_indirect = input("Indirect proof exists? (y/n): ").lower() == "y"

    proof_nodes = int(proof_direct) + int(proof_indirect)

    # Step 5: Binary decision
    total_verified_hours = (direct_hours if proof_direct else 0) + (indirect_hours if proof_indirect else 0)
    
    if proof_nodes >= 1:
        return f"Proof of Value Achieved ({proof_nodes} proof nodes)\n   Customer: {selected_route['name']}\n   Total verified: {total_verified_hours:.0f} hrs\n   Drivers: {drivers}"
    else:
        return "No proof → Loop back and refine"


print(proof_of_value_binary())


