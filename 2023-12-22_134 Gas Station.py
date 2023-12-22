# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        value = []
        max_ = 0
        is_posible = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            val = g - c
            is_posible += val
            value.append(val)
            if val >= value[max_]:
                max_ = i
        if is_posible < 0:
            return -1
        pointer = max_ + 1
        temp = 0
        temp_list = []
        while pointer != max_:
            if pointer == len(value):
                pointer = 0
                continue
            temp += value[pointer]
            if temp > 0:
                temp_list.append(pointer)
            elif ((pointer == max_ - 1 or
                    max_ == 0 and pointer == len(value) - 1) and
                    temp == 0):
                temp_list.append(pointer)
            else:
                temp = 0
                temp_list = []
            pointer += 1
        if temp_list:
            return temp_list[0]
        else:
            return max_

