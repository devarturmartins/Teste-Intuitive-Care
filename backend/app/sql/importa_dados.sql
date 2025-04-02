COPY agencias (
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans
)
FROM '/assets/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
QUOTE '"'
ENCODING 'UTF8';


COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/assets/1T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/assets/2T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/assets/3T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY despesas (
    data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/assets/4T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';