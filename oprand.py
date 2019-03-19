import config

class MPIS_OP():
    # Properties
    issue_cycle = 0
    begin_exe_cycle = 0
    end_exe_cycle = 0
    write_cycle = 0
    required_cycle = 0
    executed_cyc = 0
    name = ""
    if_begin_exe = False
    if_write_exe = False
    flag_input_j = False
    flag_input_k = False
    flag_wait_next_cyc = False
    input_j = ""
    input_k = ""
    output = ""
    def __init__(self, name, res, j ,k):
        self.input_j = j;
        self.input_k = k;
        self.output = res;
        self.name = name;
        self.required_cycle = config.REQUIRE_CYCLE[name]
        return

    def issue(self,cycle_num, reg_dict):
        self.issue_cycle = cycle_num
        if self.input_j in reg_dict:
            self.flag_input_j = reg_dict[self.input_j]
        else:
            reg_dict[self.input_j] = True
            self.flag_input_j = True

        if self.input_k in reg_dict:
            self.flag_input_k = reg_dict[self.input_k]
        else:
            reg_dict[self.input_k] = True
            self.flag_input_k = True
        # the results is occupied
        reg_dict[self.output] = False
        self.if_begin_exe = (self.flag_input_k and self.flag_input_j)
        print("%s has been issued!\n"%self.name)
        return reg_dict

    def update_state(self,cycle_num, reg_dict):
        #check if it can begin execute:
        self.flag_input_j = reg_dict[self.input_j]
        self.flag_input_k = reg_dict[self.input_k]
        self.if_begin_exe = (self.flag_input_k and self.flag_input_j)
        if self.if_begin_exe:
            self.executed_cyc += 1
            print("%s is in own_cycle : %d, total is %d cyc!\n" % (self.name, self.executed_cyc, self.required_cycle))
        if self.required_cycle == self.executed_cyc:
            self.if_write_exe = True
            self.end_exe_cycle = cycle_num
        else:
            self.if_write_exe = False
            flag_wait_next_cyc = True
        return

    def write_results(self, cycle_num,reg_dict ):
        if self.if_write_exe and (self.flag_wait_next_cyc == False):
            self.write_cycle = cycle_num
            reg_dict[self.output] = True
            print("%s is written to register" %(self.name))
        return
    pass