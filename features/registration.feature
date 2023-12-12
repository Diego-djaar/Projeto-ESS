Feature: Cadastro e Gerenciamento de Lojas e Produtos
As a Representante de um comércio
I want to Ser capaz de fornecer as informações do comércio e produtos
So that Eu possa usufruir da plataforma para minhas vendas

Cenário: Cadastro de Nova Loja com Sucesso
Given que a loja "Hortifruti" não está cadastrada
And o representante está na página de cadastro
When preenche o nome, CNPJ, razão social, email e categoria corretamente
And clica no botão "Cadastrar"
Then "Hortifruti" é armazenada como uma loja válida no sistema
And um popup de cadastro bem-sucedido aparece

Cenário: Tentativa de Cadastro com Informações Incorretas
Given que a loja "Hortifruti" não está cadastrada
And o representante está na página de cadastro
When preenche o CNPJ da loja incorretamente
Then o cadastro não é bem-sucedido
And o campo de CNPJ é limpo
And um popup indicando que o CNPJ foi preenchido incorretamente aparece

Cenário: Tentativa de Cadastro de Loja Já Registrada
Given que a loja "Hortifruti" já está cadastrada
And o representante está na página de Cadastro
When preenche o nome "Hortifruti" no "Nome da Loja"
Then o cadastro não é bem-sucedido
And um popup indicando que a loja já está cadastrada aparece
And um popup oferece o redirecionamento para a página de login

Cenário: Cadastro de Novo Produto com Sucesso
Given que o representante está logado com os dados da loja "Hortifruti"
And está na página de gerenciamento de produto
And deseja acionar "Abacate" como um produto
When seleciona adicionar um novo produto
And preenche os dados do "Abacate" corretamente (Nome, Tipo, Valor, Estoque)
Then o "Abacate" é adicionado à página da loja
And um popup indica o sucesso no cadastro do produto

Cenário: Cadastro de Novo Produto Não Sucedido
Given que o representante está logado com os dados da loja "Hortifruti"
And está na página de gerenciamento de produtos
And deseja acionar "Abacate" como um produto
When seleciona adicionar um novo produto 
And preenche o valor do "Abacate" incorretamente como "dois mil reais"
Then o cadastro do produto é cancelado
And um popup indica o valor como preenchido incorretamente durante o cadastro

Cenário: Alteração de um Produto já Cadastrado
Given que o representante está logado com os dados da loja "Hortifruti"
And está na página de gerenciamento de produtos
And deseja modificar o preço do "Abacate"
When seleciona modificar um produto existente
And escolhe o preço como o dado para modificar
And modifica o valor para "32.80"
Then p preço do produto é atualizado
And um popup indica o sucesso na alteração

Cenário: Remoção de um Produto já Cadastrado
Given que o representante está logado com os dados da loja "Hortifruti"
And está na página de gerenciamento de produtos
And "Abacate" está cadastrado na loja
When seleciona a opção de remover produto
And escolhe o "Abacate" como o produto para remover
Then o "Abacate" é removido do sistema e da página da loja