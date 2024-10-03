#!/usr/bin/python3
""" Module for solving prime game question """


def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None
    largest_num = max(nums)

    sieve = [True for _ in range(max(largest_num + 1, 2))]
    for i in range(2, int(pow(largest_num, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, largest_num + 1, i):
            sieve[j] = False
    sieve[0] = sieve[1] = False
    prime_count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            prime_count += 1
        sieve[i] = prime_count
    maria_wins = 0
    for num in nums:
        maria_wins += sieve[num] % 2 == 1
    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
