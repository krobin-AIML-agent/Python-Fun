# %%
import datetime, random

skill_applied = {
    "Operations": ["Continuous Improvement", "Lean Systems", "Value Stream Mapping"],
    "Technical": ["SQL", "Python", "ETL/ELT", "File Handling", "ML Workflows", "Data Visualization"],
    "Finance": ["P&L Analysis", "ROI Modeling", "Forecasting"],
    "Executive": ["Strategy", "Decision Dashboards", "Change Management"],
    "AI": ["Automation", "Context Engineering", "Adaptability"],
    "Program Management": ["Planning", "Scheduling", "Risk Management"],
    "Continuous Improvement": ["Process Diagnostics", "Kaizen", "Root Cause Analysis"]
}

skill_mentalmodels = {
    "Operations": ["Tactical", "Precision-Based"],
    "Technical": ["Systematic Thinking", "Problem Decomposition"],
    "Finance": ["Meticulous", "Short-Term & Long-Term Horizon", "Risk Hedging"],
    "Executive": ["Deep Business Acumen", "Change Management"],
    "AI": ["Meta Cognition", "Context Engineering", "Micro-Decision Augmentation"],
    "Program Management": ["Simplified Complexity", "Dependency Mapping", "Decomposition"],
    "Continuous Improvement": ["Lean Thinking", "Pattern Recognition", "Root Cause Analysis"]
}

# Core operating system traits (always output)
base_traits = [
    "Agility", 
    "Relatable", 
    "Treat Humans as Humans", 
    "Authenticity", 
    "Resilience", 
    "Problem-Solving", 
    "Adaptability"
]

def deploy_skillset(*contexts, question=None):
    today = datetime.date.today()
    trigger_date = datetime.date(2025, 10, 2)

    # Timing logic
    if today < trigger_date:
        timing = "Too early."
    elif today == trigger_date:
        timing = "Perfect timing."
    else:
        timing = "Timing has caught up."

    # Applied skills (contextual, only if audience chosen)
    applied_skills = []
    for ctx in contexts:
        if ctx in skill_applied:
            applied_skills += skill_applied[ctx]

    # All mental models (always included)
    all_mental_models = []
    for values in skill_mentalmodels.values():
        all_mental_models.extend(values)

    return {
        "Timing": timing,
        "Context(s)": contexts if contexts else ["Universal"],
        "Question": question,
        "Base Traits": base_traits,
        "Applied Skills (Contextual)": applied_skills if applied_skills else ["None (no specific audience chosen)"],
        "Mental Models (Universal)": all_mental_models,
        "Contextual Engineering Output": base_traits + applied_skills + all_mental_models
    }

# Pretty print diagnostic report
def print_deployment_report(*contexts, question=None):
    report = deploy_skillset(*contexts, question=question)
    print("\n=== CONTEXTUAL ENGINEERING DIAGNOSTIC ===\n")
    print(f"Timing: {report['Timing']}")
    print(f"Context(s): {', '.join(report['Context(s)'])}")
    if report['Question']:
        print(f"Question: {report['Question']}")
    print("\n--- BASE TRAITS (Always Deployed) ---")
    for trait in report['Base Traits']:
        print(f"  • {trait}")
    print("\n--- APPLIED SKILLS (Contextual) ---")
    for skill in report['Applied Skills (Contextual)']:
        print(f"  • {skill}")
    print("\n--- MENTAL MODELS (Universal) ---")
    for model in report['Mental Models (Universal)']:
        print(f"  • {model}")
    print("\n--- CONTEXTUAL ENGINEERING OUTPUT ---")
    for out in report['Contextual Engineering Output']:
        print(f"  • {out}")
    print("\n======================================\n")

# Prompt sequencing
def run_prompt_sequence():
    print("Who are you talking to?")
    print("Options: Operations, Technical, Finance, Executive, AI, Program Management, Continuous Improvement")
    audience_input = input("Enter audience/team (or multiple, separated by commas, leave blank for universal or 'random'): ").strip()

    if not audience_input:  # universal mode
        audiences = []
    elif audience_input.lower() == "random":  # random mode
        all_keys = list(skill_applied.keys())
        num_choices = random.randint(1, len(all_keys))  # choose between 1 and all audiences
        audiences = random.sample(all_keys, num_choices)
        print(f"\n Random Mode Activated → Talking to: {', '.join(audiences)}")
    else:  # manual mode
        audiences = [a.strip() for a in audience_input.split(",") if a.strip()]

    question = input("What's the question/context you want to explore? ")
    print_deployment_report(*audiences, question=question)

# Mindset function — “go get it”
def go_get_it(option="a"):
    options = {
        "a": "Go get it.",
        "b": "Go get it.",
        "c": "Go get it."
    }
    return options.get(option.lower(), "No shortcuts. Go get it.")


