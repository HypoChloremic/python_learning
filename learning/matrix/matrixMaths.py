import random, math

class NeuralNetwork:
    def __init__(self, inp, hidden, output):
        print("running neuralNet")
        # constants
        self.input   = inp
        self.hidden = hidden
        self.output  = output
        arg = [self.input, self.hidden, self.output]
        self.weights = [self.genWeights(inp,hidden), self.genWeights(hidden, output)]
        print(self.weights)
        random.seed(2)


    def genWeights(self, fir, sec):
        weights = []
        for i in range(sec):
            weights.append([])
            for j in range(fir):
                weights[i].append(random.randint(0,10))
        return weights
    

    def dotProduct(self, vector, matrix):
        print(vector, matrix)
        temp = []
        for i in range(len(vector)):
            temp.append([])
            for j in range(len(matrix)):
            	temp[-1].append(matrix[j][i]*vector[i])

        dotted = []
        for i in range(len(temp)):
        	p = sum(temp[i])
        	dotted.append(self.sigmoid(p))
        return dotted

    def drive(self, fundInput):
    	hidden = self.dotProduct(fundInput, self.weights[0])
    	output = self.dotProduct(hidden, self.weights[1])
    	print(output, "\n")
    	return output

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

if __name__ == '__main__':
	neur = NeuralNetwork(1,3,1)
	neur.drive([50])
	neur.drive([10])
	neur.drive([1])

	