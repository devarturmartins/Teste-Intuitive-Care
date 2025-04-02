SELECT 
    a.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM despesas d
JOIN agencias a ON d.reg_ans = a.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND d.data >= (CURRENT_DATE - INTERVAL '3 months')
GROUP BY a.razao_social
ORDER BY total_despesas DESC
LIMIT 10;



SELECT 
    a.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM despesas d
JOIN agencias a ON d.reg_ans = a.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND d.data >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY a.razao_social
ORDER BY total_despesas DESC
LIMIT 10;