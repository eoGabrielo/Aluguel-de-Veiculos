# Aluguel de Veículos

Este é um programa Python simples para calcular o custo de aluguel de veículos. Ele permite que o usuário escolha entre carros e motos, inserindo informações como dias de aluguel, quilômetros rodados e taxa diária.

## Como Usar

1. Execute o programa em um ambiente Python.
2. Insira o tipo de veículo desejado (C para carro, M para moto).
3. Siga as instruções para fornecer informações sobre dias de aluguel, quilômetros rodados e taxa diária do veículo.
4. Obtenha o total a pagar e um resumo detalhado do aluguel.

**README: Aluguel de Veículos**

```markdown
# Aluguel de Veículos

Este é um programa em Python que calcula o custo de aluguel de veículos. Ele guia o usuário através da escolha do tipo de veículo (carro ou moto) e coleta informações sobre dias de aluguel, quilômetros rodados e taxa diária. O resultado é um resumo detalhado e o custo total do aluguel.

## Como Usar

1. Execute o programa em um ambiente Python.
2. Insira o tipo de veículo desejado (C para carro, M para moto).
3. Siga as instruções para fornecer informações sobre dias de aluguel, quilômetros rodados e taxa diária do veículo.
4. Obtenha o total a pagar e um resumo detalhado do aluguel.

## Detalhes do Código

### Apresentação Inicial

O programa começa com uma apresentação visual marcante indicando o serviço de aluguel de veículos.

### Escolha do Tipo de Veículo

O usuário é solicitado a inserir o tipo de veículo desejado (carro ou moto) por meio da entrada do teclado. Um loop garante a validação da escolha.

```python
tipoDoVeiculo= str(input("O veiculo é carro ou moto? [C/M]")).upper().strip()
while tipoDoVeiculo not in "CM":
    tipoDoVeiculo = str(input("Somente Carro ou Moto, Tente novamente: [C/M] ")).upper().strip()
```

### Atribuição da Taxa do Tipo de Veículo

Com base na escolha do usuário, uma taxa específica (`tipoDoVeiculoConta`) é atribuída para cálculos posteriores.

```python
if tipoDoVeiculo == "M":
    tipoDoVeiculoConta= 0.15
if tipoDoVeiculo == "C":
    tipoDoVeiculoConta= 2.15
```

### Entrada de Informações Adicionais

O usuário fornece informações sobre dias de aluguel, quilômetros rodados e a taxa diária do veículo.

### Cálculos e Exibição

O programa realiza cálculos para determinar o custo total do aluguel, considerando dias e quilômetros rodados. Exibe um resumo detalhado, incluindo o tipo de veículo, preço por dia, preço por quilômetro, total a pagar, entre outros.

Agradeço pela utilização do programa. Divirta-se explorando e personalizando conforme necessário.
```

Este README fornece informações detalhadas sobre como usar o programa, sua estrutura de código e convida os usuários a explorar e personalizar conforme necessário.

## Interface Inicial

O programa inicia com uma apresentação visual indicando que se trata de um serviço de aluguel de veículos.

## Escolha do Tipo de Veículo

O usuário é solicitado a inserir o tipo de veículo desejado (carro ou moto) através da entrada do teclado. Um loop garante a validação da escolha.

## Atribuição da Taxa do Tipo de Veículo

Com base na escolha do usuário, uma taxa específica é atribuída (`tipoDoVeiculoConta`) para cálculos posteriores.

## Entrada de Informações Adicionais

O usuário fornece informações sobre dias de aluguel, quilômetros rodados e a taxa diária do veículo.

## Cálculos e Exibição

O programa realiza cálculos para determinar o custo total do aluguel, considerando dias e quilômetros rodados. Exibe um resumo detalhado incluindo o tipo de veículo, preço por dia, preço por quilômetro, total a pagar, entre outros.

Agradeço pela utilização do programa. Divirta-se explorando e personalizando de acordo com suas necessidades.
