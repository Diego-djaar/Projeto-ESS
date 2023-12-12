Feature: Estatisticas das lojas no final do mês

Cenário: Visualizar Estatisticas gerais da loja
Given o representante está logadado na loja "Hortifruti"
And está da na pagina de Estatisticas da loja
When o representante seleciona a opção "Estatisticas gerais do mês"
Then ele consegue ver diversar informações referentes a loja (Receita total, numero de pedidos, produto mais vendido, principal cliente, valor esperado)
And um popup com a opção de download de um pdf com as estatisticas aparece

Cenário: Visualizar Estatisticas de um produto especifico
Given o representante está logadado na loja "Hortifruti"
And está da na pagina de Estatisticas da loja
And deseja checar as vendas de "descascador de frutas 3000"
When o representante seleciona a opção "Estatisticas dos produtos"
And seleciona "descascador de frutas 3000"
Then ele consegue ver diversar estatisticas do produto (numero de vendas, receita gerada, avaliação media)
