import math

class matrix:
    def __init__(self,matrix):
        self.matrix=matrix
        self.is_square = len(self.matrix)==len(self.matrix[0])
        self.order = (len(matrix),len(matrix[0]))

    
    def __add__(self,other):
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[0])):
                res[i].append(self.matrix[i][j]+other.matrix[i][j])
        return res 
    
    
    def __sub__(self,other):
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[0])):
                res[i].append(self.matrix[i][j]-other.matrix[i][j])
        return res
    

    def __mul__(self,other):
        if isinstance(other,matrix):
            res=[]
            for i in range(len(self.matrix)):
                res.append([])
                for j in range(len(other.matrix[0])):
                    res[i].append(0)
                    for k in range(len(other.matrix)):
                        res[i][j]+=self.matrix[i][k]*other.matrix[k][j]
            return matrix(res)
        else:
            res = self.matrix
            for i in range(len(res)):
                for j in range(len(res[0])):
                    res[i][j]*=other
            return matrix(res)


    def transpose(self):
        res=[]
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[0])):
                res[i].append(self.matrix[j][i])

        return matrix(res)
    
    
    @staticmethod
    def minor(mat,coord):
        res = []
        c = 0
        for i in range(len(mat.matrix)):
            if i != coord[0]: 
                res.append([])
                for j in range(len(mat.matrix[0])):
                    if j != coord[1]:
                        res[c].append(mat.matrix[i][j])
                c+=1

        return matrix(res)
    

    def cofactor(self,mat,coord):
        return math.pow(-1,coord[0]+coord[1])*self.minor(mat,coord).determinant()
    
    def determinant(self):

        if self.is_square:

            if self.order[0]==1:
                return self.matrix[0][0]

            if self.order[0]==2:
                return self.matrix[0][0]*self.matrix[1][1]-(self.matrix[1][0]*self.matrix[0][1])
            else:
                res = 0
                for i in range(len(self.matrix[0])):
                    res += -1**(i+2)*self.matrix[0][i]*self.minor(self,(0,i)).determinant()
                return res
            
        else:
            return None

    def adjoint(self):
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[0])):
                res[i].append(self.cofactor(matrix(self.matrix),(j,i)))

        return matrix(res)
    
    def inverse(self):
        return self.adjoint()*(1/self.determinant())

    def __repr__(self):
        s = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                s+=str(self.matrix[i][j])+' '
            s +='\n'
        return s 

