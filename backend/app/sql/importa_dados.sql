-- Importação dos dados cadastrais das operadoras (arquivo 3.2)
COPY registros (
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans
)
FROM '../../Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- Importação dos dados contábeis (arquivos 3.1)
COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '../../assets/2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '../../assets/2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';