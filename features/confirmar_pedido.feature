Feature: Notificação confirmação de pedido | site
Given acabei de confirmar o pagamento de minha  "Bolsa da Nike"
And sou redirecionado para uma nova tela
Then leio a mensagem "Seu pedido foi confirmado, agora é só esperar a entrega"
And meu carrinho está com "0" itens

Feature: Notificação confirmação de pedido | e-mail
Given acabei de confirmar o pagamento de minha  "Bolsa da Nike"
And verifico meu e-mail "João@gmail.com"
Then vejo que recebi um e-mail novo do site "e-commerce@gmail.com"
And vejo que o assunto é "Pedido 1234 confirmado!"

