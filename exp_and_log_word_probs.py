#program to solve problems like these: G=A(2.7)^(.584t)
import math
from decimal import Decimal
def solve_word_prob():
    print("\nThis program solves equations in the form F=A(2.7)^(.584t)\n")
    var = input("Are you solving for F, A, or t? ")
    if(var=='F'):
        A = input("\nA value: ")
        const = input("\nConstant being raised to a power: ")
        power = input("\nPower the constant is being raised to: ")

        power_result = Decimal(const) ** Decimal(power)
        retval = Decimal(A) * Decimal(power_result)
        print("\n" + str(retval))
    elif(var=='A'):
        F = input("\nF value: ")
        const = input("\nConstant being raised to a power: ")
        power = input("\nPower the constant is being raised to: ")

        power_result = Decimal(const) ** Decimal(power)
        retval = Decimal(F) / power_result
        print("\n" + str(retval))
    elif(var=='t'):
        F = input("\nF value: ")
        A = input("\nA value: ")
        const = input("\nConstant being raised to a power: ")
        t_const = input("\nConstant t is being multiplied by: ")

        log_part = math.log((Decimal(F)/Decimal(A)),Decimal(const))
        retval = log_part / float(t_const)
        print("\n" + str(retval))

solve_word_prob()
