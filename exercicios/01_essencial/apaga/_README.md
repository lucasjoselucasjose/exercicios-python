## Objetivo

Manipular strings é uma habilidade essencial no início do aprendizado de programação. Neste exercício, vamos praticar como criar novas strings a partir de uma original, removendo um caractere específico com base em sua posição.

## Especificação
### Remova um caractere de uma posição específica

Abra o arquivo `main.py`. Dentro dele, localize a função resposta. Essa função deverá receber:

- uma `String` chamada `palavra`
- um `int` chamado `index`

Sua tarefa é retornar uma nova `string` igual à original, mas sem o caractere localizado na posição `index`.

As regras são:

- Se `index` for válido, remova o caractere daquela posição.
    Exemplo: apaga('kitten', 1) → 'ktten'
    Exemplo: apaga('kitten', 4) → 'kittn'

- Se `index` for maior ou igual ao tamanho da palavra, retorne a `string` original sem alterações.
    Exemplo: apaga('kitten', 4) → 'kittn'

Atenção: utilize return, não print.
