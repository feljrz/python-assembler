import python_code

class vm_p:

    constant_counter = []
    static_counter = []

    def __init__(self, origin, dest_file):
        self.origin = origin
        self.dest_file = dest_file
    
    @staticmethod
    def aritimetica(expressao):
        logical = {'+': 'add', '-': 'sub', '<':'lt', '>':'gt',
                    '!':'neg', 'and':'and', 'or':'or', 'not':'not'}

    @classmethod
    def constants(cls, expressao):
        if '=' in expressao:
            expressao = expressao.split('=')
            stat

            


   



