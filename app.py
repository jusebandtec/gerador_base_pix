from base_pix import BasePix
from json_service import JsonService


transacoes = []
for _ in range(0,15):
    transacoes.append(BasePix().transacoes)

json_service = JsonService(transacoes)

json_service.write()