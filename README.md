# Processo de mineração de um hash na blockchain

![Python Badge](https://img.shields.io/badge/python-%5E3.9-blue?style=flat-square&logo=python&logoColor=white)
![Blockchain Badge](https://img.shields.io/badge/blockchain-grey?style=flat-square&logo=blockchain.com&logoColor=white)

Breve código para aprender a realizar a mineração de um hash de 64 bits em hexadecimal para um hash válido começando com os 4 primeiros dígitos em 0000.

## Funcionamento

Coloque em transaction os dados que você deseja que seja gerado um hash, aqui ele é gerado com as seguinte informações:

- Número do bloco na blockchain (é colocado na chamada da função mine);
- Dados da transação (as informações relevantes);
- O valor do hash anterior;
- Quantidade do prefixo 0.

Para que seja gerado um hash compatível à quantidade de zeros colocada se faz o uso do nonce (valor que é escolhido para gerar um hash compatível com os 4 primeiros dígitos valendo 0, é escolhido por meio de um laço for - tentativa e erro). Assim, para gerar este novo hash compatível é colocado:

- Número do bloco na blockchain (é colocado na chamada da função mine);
- Dados da transação (as informações relevantes);
- O valor do hash anterior;
- Nonce escolhido no laço.

Se o prefixo do hash obtiver 4 zeros, ele retorna o novo hash já minerado.

## Aprendizado

- Blockchain;
- Mineração
- Hash;
- SHA256;