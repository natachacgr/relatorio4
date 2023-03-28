from database import Database
from salve_json import writeAJson

from product_analyzer import ProductAnalyzer

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

pAnalyzer = ProductAnalyzer(db.collection)

result = pAnalyzer.gasto_total_B()
writeAJson(result, "gasto_total_B")

result2 = pAnalyzer.produto_menos_vendido()
writeAJson(result2, "produto_menos_vendido")

result3 = pAnalyzer.cliente_que_menos_gastou()
writeAJson(result3, "cliente_que_menos_gastou")

result4 = pAnalyzer.produtos_vendidos_mais_2_unidades()
writeAJson(result4, "produtos_vendidos_mais_2_unidades")