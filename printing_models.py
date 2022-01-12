def print_models(unprinted_designes, completed_models):
    """
    Simulate printing each design, until none are left.
    move each design to completed_models after printing
    """
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designes = ['phone case', 'robot pendant', 'dodecaheadron']
completed_models = []

print_models(unprinted_designes, completed_models)
show_completed_models(completed_models)
