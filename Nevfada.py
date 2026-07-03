# Clinic Details
OWNER = "KIPLANGAT CHEPKWONY"
CLINIC_NAME = "NEVADA CLINIC"
LOCATION = "Kipsuter"
MOTTO = "We treat but God heals"

# Core Data Structures
patient_list = []
inventory = {"PARACETAMOL": 150, "AMOXICILLIN": 80, "ANTISEPTIC": 45}

def print_header():
    print("==========================================")
    print(f"          {CLINIC_NAME}")
    print(f"          Location: {LOCATION}")
    print(f"          Owner: {OWNER}")
    print(f"          Motto: \"{MOTTO}\"")
    print("==========================================\n")

def register_patient(name, age, symptoms):
    patient = {"name": name, "age": age, "symptoms": symptoms}
    patient_list.append(patient)
    print(f"✔ Success: Patient '{name}' registered.")

def treat_patient(patient_name, medication, quantity):
    print(f"\n--- Treating {patient_name} ---")
    if medication in inventory and inventory[medication] >= quantity:
        inventory[medication] -= quantity
        print(f"✔ Dispensed {quantity} units of {medication}.")
    else:
        print(f"❌ Error: Insufficient stock of {medication}!")

def print_dashboard():
    print("\n--- NEVADA CLINIC DASHBOARD ---")
    
    print("\n[ Active Patients ]")
    for i, p in enumerate(patient_list, 1):
        print(f"{i}. Name: {p['name']} | Age: {p['age']} | Symptoms: {p['symptoms']}")
        
    print("\n[ Chemist Stock Balance ]")
    for item, qty in inventory.items():
        print(f"• {item}: {qty} units available")
    print("==========================================")

# --- SIMULATION RUN ---
print_header()

print("Automatically Simulating Clinic Actions...\n")

# 1. Register multiple patients
register_patient("Mercy Chebet", "28", "Malaria symptoms")
register_patient("John Kiprop", "34", "Severe Headache")

# 2. Simulate dispensing medication (updates inventory automatically)
treat_patient("Mercy Chebet", "AMOXICILLIN", 10)
treat_patient("John Kiprop", "PARACETAMOL", 2)

# 3. View final state of the clinic
print_dashboard()
print("\nSystem simulation completed successfully.")
# --- CONTINUATION: PRICING, NEW STOCKS & REVENUE ---

# 4. Medicine Pricing Structure (Price per unit)
MEDICINE_PRICES = {
    "PARACETAMOL": 5,      # e.g., 5 KES or dollars per unit
    "AMOXICILLIN": 15,
    "ANTISEPTIC": 50
}

# Track clinic's total revenue from treatments
total_revenue = 0

def receive_new_stock(medication, quantity):
    """Simulates receiving a shipment of new medicine supplies."""
    print(f"\n--- 📦 Receiving New Stock Shipment ---")
    if medication in inventory:
        inventory[medication] += quantity
        print(f"✔ Success: Added {quantity} units to {medication}. New balance: {inventory[medication]}")
    else:
        # If it's a completely new brand of medicine
        inventory[medication] = quantity
        print(f"✔ Success: Registered and added new medicine type '{medication}' with {quantity} units.")

def treat_and_bill_patient(patient_name, medication, quantity):
    """Enhanced version of treatment that handles inventory AND billing."""
    global total_revenue
    print(f"\n--- Treating & Billing {patient_name} ---")
    
    # Check if medicine exists and has enough stock
    if medication not in inventory:
        print(f"❌ Error: {medication} is not available in this clinic.")
        return
        
    if inventory[medication] >= quantity:
        # Deduct stock
        inventory[medication] -= quantity
        
        # Calculate bill cost
        unit_price = MEDICINE_PRICES.get(medication, 0)
        total_cost = unit_price * quantity
        total_revenue += total_cost
        
        print(f"✔ Dispensed {quantity} units of {medication}.")
        print(f"💵 Bill Generated: {quantity} x {unit_price} = {total_cost} total cost.")
    else:
        print(f"❌ Error: Insufficient stock of {medication}!")

def print_financial_dashboard():
    """Prints stock balances alongside their unit prices and total revenue."""
    print("\n==========================================")
    print(f"   {CLINIC_NAME} - INVENTORY & FINANCIALS  ")
    print("==========================================")
    
    print("\n[ Available Medicine Prices & Stock ]")
    for item, qty in inventory.items():
        price = MEDICINE_PRICES.get(item, "N/A")
        print(f"• {item:<12} | Stock: {qty:<4} units | Unit Price: {price}")
        
    print(f"\n📈 Total Clinic Revenue Generated: {total_revenue}")
    print("==========================================\n")


# --- SIMULATING THE NEW CONTINUATION ACTIONS ---

# 5. Simulate treating patients with automated billing calculations
treat_and_bill_patient("Mercy Chebet", "AMOXICILLIN", 5)  # 5 units * 15 = 75
treat_and_bill_patient("John Kiprop", "ANTISEPTIC", 1)    # 1 unit * 50 = 50

# 6. Simulate receiving brand new stocks/supplies
receive_new_stock("PARACETAMOL", 100)  # Adds to existing stock
receive_new_stock("VITAMIN C", 200)    # Automatically introduces a new medicine type
MEDICINE_PRICES["VITAMIN C"] = 3       # Set a price for the new medicine

# 7. Print the updated financial and stock dashboard
print_financial_dashboard()

print("Extended simulation completed successfully.")
# --- CONTINUATION: STAFF MEMBERS & LABORATORY RESULTS ---

# 8. Staff Database (List of dictionaries representing clinic team)
staff_members = [
    {"id": 101, "name": "Dr. Langat", "role": "Doctor", "specialization": "General Practitioner"},
    {"id": 102, "name": "Nurse Chepngeno", "role": "Nurse", "specialization": "Triage & Care"},
    {"id": 103, "name": "Alex Cheruiyot", "role": "Lab Technician", "specialization": "Pathology"}
]

def add_lab_result(patient_name, test_name, result, status="Completed"):
    """Finds a patient by name and attaches or updates their laboratory results."""
    print(f"\n--- 🔬 Processing Lab Test for {patient_name} ---")
    patient_found = False
    
    # Search for the patient in our existing list
    for p in patient_list:
        if p["name"].lower() == patient_name.lower():
            # If the patient doesn't have a 'lab_results' key yet, initialize a list
            if "lab_results" not in p:
                p["lab_results"] = []
            
            # Append the new test details
            p["lab_results"].append({
                "test_name": test_name,
                "result": result,
                "status": status
            })
            print(f"✔ Success: Recorded '{test_name}' result for {patient_name}.")
            patient_found = True
            break
            
    if not patient_found:
        print(f"❌ Error: Patient '{patient_name}' not found in the system. Cannot assign lab result.")

def print_clinical_dashboard():
    """Displays the active staff members and the medical lab reports for each patient."""
    print("\n==========================================")
    print(f"       {CLINIC_NAME} - CLINICAL PORTAL     ")
    print("==========================================")
    
    # Display Staff Duties
    print("\n[ On-Duty Clinic Staff ]")
    for staff in staff_members:
        print(f"• {staff['name']} ({staff['role']}) - Spec: {staff['specialization']}")
        
    # Display Patient Records & Lab Outcomes
    print("\n[ Patient Medical & Lab Records ]")
    if not patient_list:
        print("No patient records available.")
    else:
        for i, p in enumerate(patient_list, 1):
            print(f"\n{i}. Patient: {p['name']} | Age: {p['age']}")
            print(f"   Symptoms: {p['symptoms']}")
            
            # Check if lab results exist for this patient
            print("   Lab Results:")
            if "lab_results" in p and p["lab_results"]:
                for test in p["lab_results"]:
                    print(f"     🔬 {test['test_name']}: {test['result']} [{test['status']}]")
            else:
                print("     (No lab tests ordered/pending for this patient)")
    print("==========================================\n")


# --- SIMULATING THE NEW CLINICAL ACTIONS ---

# 9. Log laboratory tests for the simulated patients
add_lab_result("Mercy Chebet", "Malaria Rapid Test", "Positive (Plasmodium falciparum detected)")
add_lab_result("John Kiprop", "Blood Pressure Check", "135/85 mmHg - Mild Hypertension")

# 10. Attempt a test for a non-existent patient to verify safety constraints
add_lab_result("Unknown Patient", "Full Blood Count", "Normal")

# 11. Print the clinical system view showing staff and patient lab outputs
print_clinical_dashboard()

print("Full clinic management simulation completed successfully.")
