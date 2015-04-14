# Author: Matt Ankerson
# Date: 14 April 2015
# This file contains the classes that we will use as state objects in the VendingMachine.


# This class is the 'interface' that each state class must adhere to.
class State(object):

    def change_state(self, vm):
        raise NotImplementedError("")

    def __repr__(self):
        raise NotImplementedError("")

# Each of the below classes represents a single state, and provides a method to change to another state.


class WaitingState(State):

    def change_state(self, vm):
        if vm.selection in vm.products:
            if vm.money_received >= vm.products[vm.selection]:
                return MoneyReceivedState()
            else:
                print("Insufficient funds")
                return MakingChangeState()
        else:
            if vm.selection == "":
                return WaitingState()
            else:
                print("Invalid selection")
                exit()

    def __repr__(self):
        return "The vending machine is waiting."


class MoneyReceivedState(State):

    def change_state(self, vm):
        if vm.selection in vm.products:
            return InputReceivedState()
        else:
            print("Invalid item")
            return MakingChangeState()

    def __repr__(self):
        return "The vending machine has received enough money."


class InputReceivedState(State):

    def change_state(self, vm):
        return VendingState()

    def __repr__(self):
        return "The vending machine has received input."


class VendingState(State):

    # deduct cost from received money and decide if we need to make change
    def change_state(self, vm):
        vm.money_received -= vm.products[vm.selection]
        if vm.money_received > 0:
            return MakingChangeState()
        else:
            vm.money_received = 0
            vm.selection = ""
            return WaitingState()

    def __repr__(self):
        return "The vending machine is vending."


class MakingChangeState(State):

    def change_state(self, vm):
        print("You have been refunded: " + str(vm.money_received))
        vm.money_received = 0
        vm.selection = ""
        return WaitingState()

    def __repr__(self):
        return "The vending machine is making change."

