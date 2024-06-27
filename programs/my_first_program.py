from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform a computation using my_int1 and my_int2
    sum_result = my_int1 + my_int2

    # Change the output to be the result of the computation
    return [Output(sum_result, "sum_output", party1)]
