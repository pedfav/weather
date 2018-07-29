import datetime

class Data(object):
    temperatura = ""
    umidade = ""
    data = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, temperatura, umidade):
        self.temperatura = temperatura
        self.umidade = umidade
        self.data = str(datetime.datetime.now())

    def make_data(temperatura, umidade):
        Data = Data(temperatura, umidade)
        return Data

    def to_string(self):
        print(self.data + ' - Temperatura={0:0.1f}* Umidade={1:0.1f}%'.format(self.temperatura, self.umidade))

    def to_json(self):
        return {'temperatura': self.temperatura, 'umidade': self.umidade, 'Hora': self.data}
