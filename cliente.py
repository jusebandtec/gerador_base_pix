import random
import constantes
from fordev.generators import cpf, cnpj
from phone_gen import PhoneNumber
import phonenumbers
from faker import Faker

class Cliente:

    def __init__(self):
        self.tipo_pessoa = self.gerar_tipo_pessoa()
        self.agencia = self.gerar_agencia()
        self.conta = self.gerar_conta()
        self.documento = self.gerar_documento(self.tipo_pessoa)
        self.ispb = self.gerar_ispb()
        self.telefone = self.gerar_telefone()
        self.email = self.gerar_email()

    def gerar_agencia(self) -> str:
        return str(random.randint(1_000, 9_999))

    def gerar_conta(self) -> str:
        return str(random.randint(100_000, 1_000_000))

    def gerar_documento(self, tipo_pessoa) -> str:
        if tipo_pessoa == "PESSOA_JURIDICA":
            return cnpj()
        else:
            return cpf()

    def gerar_telefone(self) -> str:
        phone_number = PhoneNumber("Brazil")
        
        telefone_formulario = phone_number.get_national()

        while len(telefone_formulario) <= 13:
            telefone_formulario = phone_number.get_mobile()

        telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

        return phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)

    def gerar_email(self) -> str:
        fake = Faker()
        return str(fake.email())

    def gerar_ispb(self) -> str:
        lista_ispbs = constantes.ISPBS
        return random.choice(lista_ispbs)

    def gerar_tipo_pessoa(self) -> str:
        return random.choice(["PESSOA_JURIDICA", "PESSOA_FISICA"])
