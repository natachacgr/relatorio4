class ProductAnalyzer:

    def __init__(self, collection):
        self.collection = collection

    #O total que o cliente B gastou
    def gasto_total_B(self):
        result = self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"cliente_id": "B"}},
            {"$group": {"_id": {"cliente": "$cliente_id"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        return result

    #Produto menos vendido de todas as compras
    def produto_menos_vendido(self):
        return self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])


    #O cliente que menos gastou em uma única compra
    def cliente_que_menos_gastou(self):
        return self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])


    #Produtos que foram vendidos acima de 2 unidades
    def produtos_vendidos_mais_2_unidades(self):
        return self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade": {"$gt":2}}}
        ])