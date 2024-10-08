class AtualizadordeContas:
    def __init__(self, selic, saldo_total = 0):
        self._selic = selic
        self._saldo_total = saldo_total
    def roda(self, conta):
        print(f'Saldo da conta: {conta._saldo}')
        self._saldo_total += conta.atualiza(self._selic)
        print(f'Saldo Final: {self._saldo_total}')
if __name__ == '__main__':
    pass