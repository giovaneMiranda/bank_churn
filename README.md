# Previsão de Churn 
O objetivo deste Readme é mostrar o contexto do problema, os passos dados para resolvê-lo, os principais insights e o desempenho geral.

![](img/churn.png)

## 1. Problema de Negócio
O TopBank é um banco que opera em três países europeus. Seu principal serviço é uma conta bancária que funciona com outros serviços como cartões de crédito, pagamentos e outros. Os contratos são válidos por 12 meses, após um ano o cliente poderá ou não renová-lo. Não há cobrança pelos serviços bancários.

O modelo de faturaento do banco por conta de cliente: 
- 15% do salário estimado do cliente, para clientes com rendimento estimado inferior à média; 
- 20% do salário estimado do cliente, para clientes com renda estimada superior à média. Problema. 

Nos últimos meses o TopBank notou um crescimento acelerado em sua taxa de churn. O desafio é entender as métricas que indicam um possível churn e ajudá-las a reduzir a taxa de churn. 

## 2. Premissa de Negócio
Os dados foram extraidos de uma competição disponivel no [Kaggle](https://www.kaggle.com/datasets/mervetorkan/churndataset)

Atributos      | Definição
-------------- | ---------------
|RowNumber     | Corresponde ao número do registro (linha) e não tem efeito na saída.|
|CustomerId    | Identificador único do cliete, contém valores aleatórios e não tem efeito na saída do cliente do banco.|
|CreditScore   | Pontuação de crédito de clientes para o mercado financeiro.|
|Geography     | O país do cliente.|
|Gender        | Representa o genero do crédito.|
|Age           | Idade do cliente|
|Tenure        | Número de anos que o cliente está no banco.|
|Balance       | O valor que o cliente tem em sua conta.|
|Tenure        | Número de anos que o cliente está no banco.|
|NumOfProducts | o número de produtos que o cliente comprou.|
|HasCrCard     | Indica se o cliente tiver um cartão de crédito.|
|IsActiveMember| Indica se o cliente estiver ativo (nos últimos 12 meses).|
|EstimatedSalary| Estimativa de salário anual de clientes.|
|Exited         | Indica se o cliente for um churn.|
