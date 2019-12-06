import python_code

class vm_p:

    static_counter = 0
    stack = []
    current_line = 0

    def __init__(self, origin, dest_file):
        self.origin = origin
        self.dest_file = dest_file

    def next_line(self):
        atual = vm_p.current_line + 1
        code = self.origin
        return code[atual]
    
    @classmethod
    def push(cls, command):
       cls.stack.append("push"+command)
    
    @classmethod
    def pop(cls, command):
        cls.stack.append('pop', command)

    
    @staticmethod
    def aritimetica(expressao):
        parse = list()
        logical = {'+': 'add', '-': 'sub','=':'EQ', '<':'lt', '>':'gt',
                    '!':'neg', 'and':'and', 'or':'or', 'not':'not'}
        for i in logical.keys():
            inicio_index = expressao.find(i)+1
            for j in logical.keys():
                final_index = expressao.find(j)
                limites = (inicio_index, final_index)
                parse.append(limites)
        

                



    @classmethod
    def constants(cls, expressao):
        if '=' in expressao:
            expressao = expressao.split('=')
            value = expressao[1]
            cls.push("constant"+value)
    
    @classmethod
    def static(cls, expressao):
        if '=' in expressao:
            

    

            


   



