from cliente import Cliente
from datetime import datetime
from constantes import TIPOS_INICIACAO
import random
import string
import uuid

class BasePix:

    def __init__(self) -> None:

        cliente = Cliente()
        cliente_contra_parte = Cliente()
        data_hora = self.gerar_data_hora()
        tipo_chave_pix = ""

        if cliente.tipo_pessoa == "PESSOA_JURIDICA":
            tipo_chave_pix = self.gerar_tipo_chave_pix_pj()
        else:
            tipo_chave_pix = self.gerar_tipo_chave_pix_pf()

        chave_pix = self.gerar_chave_pix(tipo_chave_pix, cliente)

        self.transacoes = {
            'endToEnd': self.gerar_end_to_end(data_hora, cliente.ispb),
            'cliente': {
                'documento': cliente.documento,
                'agencia': cliente.agencia,
                'conta': cliente.conta,
                'ispb': cliente.ispb
            },
            'chave': chave_pix,
            'tipoChave': tipo_chave_pix,
            'iniciacao': self.gerar_iniciacao(tipo_chave_pix),
            'clienteContraParte': {
                'documento': cliente_contra_parte.documento,
                'agencia': cliente_contra_parte.agencia,
                'conta': cliente_contra_parte.conta,
                'ispb': cliente_contra_parte.ispb
            },
            'valor': self.gerar_valor(),
            'pixAgendado': random.choice([True, False]),
            'informacaoEntreUsuarios': "",
            'data': data_hora.isoformat()
        }

    def gerar_data_hora(self):
        return datetime.now()

    def gerar_end_to_end(self, data_transacao, ispb) -> str:

        def random_caracters(size=6, chars=string.ascii_uppercase + string.digits):
                    return ''.join(random.choice(chars) for _ in range(size))

        # E -> para Envio/Transferencia
        # D -> Para devolucao
        return f'E{ispb}{data_transacao.strftime("%Y%m%d")}{random_caracters()}'

    def gerar_tipo_chave_pix_pf(self):
        return random.choice(["CPF", "EMAIL", "TELEFONE", "EVP"])

    def gerar_tipo_chave_pix_pj(self):
        return random.choice(["CNPJ", "EMAIL", "TELEFONE", "EVP"])

    def gerar_chave_pix(self, tipo_chave, cliente):
        switch = {
            "CPF": cliente.documento,
            "CNPJ": cliente.documento,
            "EMAIL": cliente.email,
            "EVP": str(uuid.uuid4()),
            "TELEFONE": cliente.telefone
        }

        return switch.get(tipo_chave, "Tipo chave inexistente.")

    def gerar_iniciacao(self, tipo_chave) -> str:

        if tipo_chave == "EVP":
            return "QR_CODE"

        return random.choice(TIPOS_INICIACAO)
    
    def gerar_valor(self) -> float:
        return "{:.2f}".format(random.uniform(0, 1_000_000))
            

    