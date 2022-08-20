from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        100,
        'Batata',
        'BatataCompany',
        '01/02',
        '01/03', '0MB99',
        'Guardar'
    )

    assert type(product.id) == int
    assert product.id == 100

    assert type(product.nome_do_produto) == str
    assert product.nome_do_produto == 'Batata'

    assert type(product.nome_da_empresa) == str
    assert product.nome_da_empresa == 'BatataCompany'

    assert type(product.data_de_fabricacao) == str
    assert product.data_de_fabricacao == '01/02'

    assert type(product.data_de_validade) == str
    assert product.data_de_validade == '01/03'

    assert type(product.numero_de_serie) == str
    assert product.numero_de_serie == '0MB99'

    assert type(product.instrucoes_de_armazenamento) == str
    assert product.instrucoes_de_armazenamento == 'Guardar'
