-- Criação da Tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    Codigo INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    ult_compra DATE
);

-- Criação da Tabela Produto
CREATE TABLE IF NOT EXISTS Produto (
    codigo INTEGER PRIMARY KEY,
    descricao TEXT NOT NULL,
    preco_lista REAL,
    preco_promocao REAL,
    percentual_desconto_maximo REAL
);

-- Criação da Tabela Estoque
CREATE TABLE IF NOT EXISTS Estoque (
    codigo_produto INTEGER,
    QTD INTEGER,
    FOREIGN KEY (codigo_produto) REFERENCES Produto(codigo)
);

-- Criação da Tabela Venda
CREATE TABLE IF NOT EXISTS Venda (
    Data DATE,
    codigo_cliente INTEGER,
    Produto INTEGER,
    QTD INTEGER,
    Valor REAL,
    FOREIGN KEY (codigo_cliente) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Produto) REFERENCES Produto(codigo)
);

-- Criação da Tabela Pedido
CREATE TABLE IF NOT EXISTS Pedido (
    data DATE,
    codigo_cliente INTEGER,
    forma_pagamento TEXT,
    produto INTEGER,
    qtd INTEGER,
    valor_unitario REAL,
    valor_total REAL,
    FOREIGN KEY (codigo_cliente) REFERENCES Cliente(Codigo),
    FOREIGN KEY (produto) REFERENCES Produto(codigo)
);

-- Inserção de Dados em Cliente
INSERT INTO Cliente (Codigo, Nome, ult_compra) VALUES
(3, 'Carlos Sousa', '2024-04-28'),
(4, 'Ana Souza', '2024-04-15'),
(5, 'Ricardo Neves', '2024-04-20'),
(6, 'Sofia Cardoso', '2024-04-10'),
(7, 'Eduardo Lima', '2024-04-12'),
(8, 'Beatriz Castro', '2024-04-18'),
(9, 'Luiz Costa', '2024-04-22'),
(10, 'Camila Santos', '2024-04-25'),
(11, 'Marcio Gomes', '2024-04-27'),
(12, 'Fernanda Machado', '2024-04-29');

-- Inserção de Dados em Produto
INSERT INTO Produto (codigo, descricao, preco_lista, preco_promocao, percentual_desconto_maximo) VALUES
(3, 'Leite Integral', 3.50, 3.00, 10),
(4, 'Pao Frances', 0.50, 0.45, 5),
(5, 'Queijo Mussarela', 20.00, 18.00, 10),
(6, 'Presunto Fatiado', 25.00, 22.50, 5),
(7, 'Manteiga', 8.00, 7.00, 10),
(8, 'Arroz Branco', 21.00, 19.00, 5),
(9, 'Feijao Carioquinha', 7.00, 6.00, 10),
(10, 'Acucar Refinado', 3.20, 3.00, 5),
(11, 'Cafe Torrado', 15.00, 14.00, 5),
(12, 'Macarrao Espaguete', 4.50, 4.20, 5);

-- Inserção de Dados em Estoque
INSERT INTO Estoque (codigo_produto, QTD) VALUES
(3, 100),
(4, 150),
(5, 200),
(6, 120),
(7, 140),
(8, 160),
(9, 180),
(10, 200),
(11, 220),
(12, 240);
