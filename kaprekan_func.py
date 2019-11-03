
def kaprekar_routine(num):
    """ Returns the fix points or constants for the Kaprekar
        routine from Dattrateya Ramachanda Kraprekar (1949)
        only for base 10.

        Substract the biggest possible number created from digits
        of input number to the smallest possible.

        N_digits | max steps | cycle/Kaprekar constant
        ----------------------------------------------
           4     |     8     | 6174
           3     |     ?     | 495
           2     |     ?     | 09-81-63-27-45

        Source: https://en.wikipedia.org/wiki/Kaprekar%27s_routine
    """
    sequence = list([num])
    n_digits = len(str(num))
    n_steps = 1
    while True:  # two exit conditions
        snum = f'{num:0{n_digits}}'
        if len(set(snum)) == 1:
            # exit if all digits are equal
            msg = "All digits are the same. Last number is 0!"
            print("WARN:", msg)
            sequence.append(0)
            return sequence, n_steps
        biggest = int("".join( sorted(snum, reverse=True, key=int) ))
        smallest = int("".join(sorted(snum, key=int)))
        num = biggest - smallest
        if num in sequence:
            # if got a existing one, it will loop
            msg = f"Next number {num} already in sequence!"
            print("WARN:", msg)
            return sequence, n_steps
        sequence.append(num)
        n_steps += 1


def kaprekar_carpet():
    # TODO: Kaprekar carpet (image)
    # https://youtu.be/pDXek06Bde4?t=161
    pass

# TODO: Other kaprekar routines:
# https://en.wikipedia.org/wiki/D._R._Kaprekar


#
# example useless
#
print("#### EXAMPLE USELESS ####")
for n in [22, 111]:
    k_ser = kaprekar_routine(n)
    print(
        f"kaprekar_routine({n}) - Steps: {k_ser[1]}\n",
        k_ser[0], '\n'
    )

#
# example cycles
#
print("#### EXAMPLE CYCLES ####")
for n in [24, 121, 13451, 123456]:
    k_ser = kaprekar_routine(n)
    print(
        f"kaprekar_routine({n}) - Steps: {k_ser[1]}\n",
        k_ser[0], '\n'
    )

#
# example constants
#
print("#### EXAMPLE CONSTANTS ####")
for n in [0, 1234, 549945, 631764, 63317664, 97508421, 554999445]:
    k_ser = kaprekar_routine(n)
    print(
        f"kaprekar_routine({n}) - Steps: {k_ser[1]}\n",
        k_ser[0], '\n'
    )
