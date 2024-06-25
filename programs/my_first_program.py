from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computations
    sum_result = my_int1 + my_int2
    diff_result = my_int1 - my_int2
    prod_result = my_int1 * my_int2
    
    # Return all results as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(diff_result, "diff_output", party1),
        Output(prod_result, "prod_output", party1)
    ]

