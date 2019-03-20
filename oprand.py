import config

class MPIS_OP():
    # Properties
    issue_cycle = 0
    #begin_exe_cycle = 0
    end_exe_cycle = 0
    write_cycle = 0
    required_cycle = 0
    executed_cyc = 0
    name = ""
    if_begin_exe = False
    if_write_exe = False
    if_end_all = False
    flag_input = False
    flag_wait_next_cyc = False
    input_j = ""
    input_k = ""
    output = ""

    occupy_op = []
    def __init__(self, name, res, j ,k):
        self.input_j = j
        self.input_k = k
        self.output = res
        self.name = name
        self.required_cycle = config.REQUIRE_CYCLE[name]
        self.occupy_op = []
        return

    def issue(self,cycle_num, activeop_list):
        self.issue_cycle = cycle_num
        # calculate the occupy relations
        for op in activeop_list:
            if (op.output == self.input_j) or (op.output == self.input_k):
                self.occupy_op.append(op)
        if len(self.occupy_op) == 0:
            self.flag_input = True
        self.flag_input= True
        for item in self.occupy_op:
            if item.if_end_all == False:
                self.flag_input = False
                break

        #reg_dict[self.output] = False
        self.if_begin_exe = self.flag_input
        print("%s has been issued!\n"%self.name)
        return

    def update_state(self,cycle_num):
        #check if it can begin execute:
        if len(self.occupy_op) == 0:
            self.flag_input = True
        self.flag_input = True
        for item in self.occupy_op:
            if item.if_end_all == False:
                self.flag_input = False
                break
        self.if_begin_exe = self.flag_input
        if self.if_begin_exe and self.if_write_exe == False:
            self.executed_cyc += 1
            print("%s is in own_cycle : %d, total is %d cyc!\n" % (self.name, self.executed_cyc, self.required_cycle))
            if self.required_cycle == self.executed_cyc:
                self.if_write_exe = True
                self.end_exe_cycle = cycle_num
                self.flag_wait_next_cyc = True
            else:
                self.if_write_exe = False

        return

    def write_results(self, cycle_num, write_once):
        if self.if_write_exe and (self.flag_wait_next_cyc == False) and (write_once == True) and (self.if_end_all == False):
            self.write_cycle = cycle_num
            #reg_dict[self.output] = True
            write_once = False
            self.if_end_all = True
            print("%s is written to register" %(self.name))
        return write_once
    pass