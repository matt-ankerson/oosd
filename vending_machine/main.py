import vending_machine


# Author: Matt Ankerson
# Date: 14 April 2015

vm = vending_machine.VendingMachine()

print(vm.get_status() + "\n")

# Add the money
money_input = raw_input("Enter the amount of money you'd like to spend: >>")
vm.insert_money(float(money_input))

print("\n" + vm.get_status() + "\n")

# Print the available options
print("Below are your options.\n")
for item in vm.products:
    print(item + " $" + str(vm.products.get(item)))

# Get the selection
selection = raw_input("Type (precisely) what you'd like to purchase: >>")

# Do we want to cancel the transaction?
if selection == 'c':
    vm.cancel_transaction()
else:
    # Make the selection.
    vm.make_selection(selection)

# Observe the changes in state...
# State should always return to 'waiting'
print(vm.get_status())
vm.change_state()
print(vm.get_status())
vm.change_state()
print(vm.get_status())
vm.change_state()
print(vm.get_status())
vm.change_state()
print(vm.get_status())
vm.change_state()
print(vm.get_status())
vm.change_state()
print(vm.get_status())