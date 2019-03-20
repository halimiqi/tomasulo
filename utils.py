import os
import numpy as np
import oprand as op

def read_file(file_name):
    str_list = []
    res_list = []
    j_list = []
    k_list = []
    with open(file_name, "r") as fin:
        for line in fin:
            tmp_str = line.strip().split(" ")
            str_list.append(tmp_str[0])
            res_list.append(tmp_str[1])
            j_list.append(tmp_str[2])
            k_list.append(tmp_str[3])
    return str_list, res_list,j_list,k_list

def issue_new_op(op_str, res,j,k,cycle_num, active_list):
    my_op = op.MPIS_OP(op_str, res,j,k)
    my_op.issue(cycle_num,active_list)
    return my_op

def change_flag_wait_and_check_stop(op_list):
    num_ended = 0
    for item in op_list:
        item.flag_wait_next_cyc = False
        if item.if_end_all == True:
            num_ended += 1
    if num_ended == len(op_list):
        return True
    else:
        return False

def plot_instruction_status(activate_list):
    print(30*"##")
    print(15*"  "+ "Issue".center(10) + "Exec".center(10) + "write".center(10))
    for op in activate_list:
        print(op.name.center(30) + str(op.issue_cycle).center(10) + str(op.end_exe_cycle).center(10) + str(op.write_cycle).center(10))
    print(30 * "##")
