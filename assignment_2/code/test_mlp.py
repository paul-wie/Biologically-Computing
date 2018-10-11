import mlp





def main():
    input = [
                [0,0],
                [1,0],
                [0,1],
                [1,1]
            ]
    target = [
                [0],[1],[1],[0]

             ]
    layer1 = [
                [0.1,0.1,-0.25],
                [0.33,-0.45,0.6],
                [-0.7,-0.8,-0.1],
             ]
    layer2 = [
                [-0.4],
                [-0.4],
                [0.7],
                [0.90]
             ]
    net = mlp.mlp(input,target,3,layer1,layer2)
    net.earlystopping(input,target,0,0)
main()

def test():
        iterations = 0
        ra = 10
        err = [0] *ra
        for x in range(ra):
            shuffle = self.randomize(inputs, targets)
            inputs = shuffle[0]
            targets = shuffle[1]
            for elem in range(len(inputs)):

                input = inputs[elem]
                target = targets[elem]
                print("input:",input)
                print("target", target)

                res_forward = self.forward(input)
                activation_values = res_forward[2]
                print("activation values", activation_values)
                er = self.check_failure(res_forward[1],target)
                err[x] += er
                print("hidden activation", res_forward[0])
                print("output", res_forward[1])
                print("discrete output",convert_output(res_forward[1] ))
                output_err = output_error(convert_output(res_forward[1]),target)
                print("output error",output_err)
                if er==1:
                    self.train(input, target, activation_values, res_forward[1])
                    print("update", er)
                else:
                    print("no update",er)

                print("weight_matrix_1", self.weight_matrix_1)
                print("weight_matrix_2", self.weight_matrix_2)


            print(err)
            print("---------------------------------------------")
