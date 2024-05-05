class Medicine:
    def __init__(self, Tablet, Brand, Compositions,SideEffects,Purpose,Cost):
        self.Tablet = Tablet
        self.Brand=Brand
        self.compositions = Compositions
        self.SideEffects=SideEffects
        self.Purpose=Purpose
        self.Cost=Cost

    def __str__(self):
        return f" Tablet : {self.Tablet}     Brand :  {self.Brand}   Compositions: {', '.join(self.compositions)}      sideeffects  :  {','.join(self.SideEffects)}      Purpose :   {self.Purpose}      Cost :   {self.Cost}"


def compare_composition(user_composition, medicines):
    found_matches = False
    for med in medicines:
        if any(comp.lower() in user_composition for comp in med.compositions):
            found_matches = True
            print("Match found:")
            print(med)
    if not found_matches:
        print("No match found for the given composition.")


def main():
    # Predefined medicines with their compositions
    predefined_medicines = [
        Medicine("Medicine 1","cipla" , ["paracetamol", "ibuprofen","calcium"] , ["vomiting","rashes"] , "fever" , "50"),
        Medicine("Medicine 2","microlabs" , ["aspirin", "calcium","paracetamol"] , ["vomiting","rashes"] ,"fever" , "50"),
        Medicine("Medicine 3" , "cipla" , ["vitamin c" , "iron"] , ["vomiting","rashes"]  ,  "fever"  ,  "50"),
        # Add more predefined medicines as needed
    ]

    # User input for composition
    user_input = input("Enter the composition of the medicine (if more than one compositions seperate by comma): ")
    user_composition = [x.strip().lower() for x in user_input.split(',')]

    # Compare user's composition with predefined medicines
    compare_composition(user_composition, predefined_medicines)


if __name__ == "__main__":
    main()

