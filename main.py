import numpy as np
import os
import utils


def run_alg(str_list, res_list, j_list, k_list):
    stop_flag = False
    cycle_num = 1
    Reserve_station = []
    activate_list = []
    write_list = []
    register_dict = {} # this store the status of the every register
    while (~stop_flag):
        #Issue new operation
        if str_list != []:
            op_str = str_list.pop()
            res_str = res_list.pop()
            j_str = j_list.pop()
            k_str = k_list.pop()
            new_op = utils.issue_new_op(op_str, res_str, j_str, k_str, cycle_num,register_dict)
            activate_list.append(new_op)

        # write_results for the ones who can write
        if write_list != []:
            write_op = write_list.pop()
            write_op.write_results(cycle_num)

        # execute existing operation
        for idx, op in enumerate(activate_list):
            if_wait_write = op.update_state(cycle_num)
            if if_wait_write:
                write_op = activate_list.pop(idx)
                write_list.append(write_op)

        # at last add the number of cycle
        cycle_num +=1



def main():
    return