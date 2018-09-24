

def write_it(file, data_set, weights, output, true_output):
    file.write("Data set / Weights / Output / True Output:\t" + str(data_set) +"\t" + str(weights)+ "\t\t"+str(output)+"/"+str(true_output)+"\n")


def write_begin(file,epoch):
    file.write("Epoch: " + str(epoch) + "\n")

def write_end(file,number_wrong):
    file.write("Wrong outputs in this generation: " + str(number_wrong) + "\n")
    file.write("-------------------------------------- \n")
