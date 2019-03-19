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
            tmp_str = line.strip().split("\t")
            str_list.append(tmp_str[0])
            res_list.append(tmp_str[1])
            j_list.append(tmp_str[2])
            k_list.append(tmp_str[3])
    return str_list, res_list,j_list,k_list

def issue_new_op(op_str, res,j,k,cycle_num, reg_dict):
    my_op = op.MPIS_OP(op_str, res,j,k)
    my_op.issue(cycle_num,reg_dict)
    return my_op

