#!/usr/bin/env python3
# -*- codding:utf-8 -*-


#	Tickets in public transportation system have unique numbers. We
# have a funny superstition or omen about them:
#	If the sum of digits in the first half of number equals to sum of
# digits in the second half - such ticket is considered "Lucky" - one
# should at once recollect some long-wished dream and eat this ticket
# - then the dream surely will come to reality!
#	Number is split into halves of equal length, of course. If the
# number contains an odd amount of digits - the middle of them is
# simply ignored. So the numbers like 117234 or 4493278 are examples
# of lucky ones.
#	Of course the number may have trailing zeroes, for example
# 6-digit numbers start from 000000and end with999999
# Input: ticket number
# Output: bool True if ticket is 'lucky ', False otherwise


def check_lucky_ticket(number: str) -> bool:
    halfing_number = int(len(number) / 2)
    first_half = list(map(int, number[0 : halfing_number]))
    second_half = list(map(int, number[-halfing_number :]))

    return sum(first_half) == sum(second_half)

print(check_lucky_ticket(input("Input number ticket: ")))
