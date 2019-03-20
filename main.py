import numpy as np
import os
import utils


def run_alg(str_list, res_list, j_list, k_list):
    stop_flag = False
    cycle_num = 1
    Num_of_Op = len(str_list)
    Reserve_station = []
    activate_list = []
    write_list = []
    register_dict = {} # this store the status of the every register


    while (stop_flag == False):
        print(30 * "##")
        print("This is cycle: %d"%cycle_num)
        print(30 * "--")
        #Issue new operation
        if str_list != []:
            op_str = str_list.pop(0)
            res_str = res_list.pop(0)
            j_str = j_list.pop(0)
            k_str = k_list.pop(0)
            new_op = utils.issue_new_op(op_str, res_str, j_str, k_str, cycle_num, activate_list)
            activate_list.append(new_op)

        # execute existing operation
        for idx, op in enumerate(activate_list):
            op.update_state(cycle_num)
            # if if_wait_write:
            #     write_op = activate_list.pop(idx)
            #     write_list.append(write_op)

        # write_results for the ones who can write
        write_once_flag = True
        for op in activate_list:
            write_once_flag = op.write_results(cycle_num, write_once_flag)
        # change the flag so we can let the op to write on next cycle
        stop_flag = utils.change_flag_wait_and_check_stop(activate_list)
        # at last add the number of cycle
        cycle_num +=1

        print(30*"##" + "\n")
    utils.plot_instruction_status(activate_list)
    return


def main():
    str_list, res_list, j_list, k_list = utils.read_file("txt/oprand.txt")
    run_alg(str_list, res_list, j_list, k_list)
    return

main()