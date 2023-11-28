Feature: Notificação confirmação de pedido
Given acabei de confirmar o pagamento de minha  "Bolsa da Nike"
And sou redirecionado para uma nova tela
Then leio a mensagem "Seu pedido foi confirmado, agora é só esperar a entrega"
And meu carrinho está com "0" itens