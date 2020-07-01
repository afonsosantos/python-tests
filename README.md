# python-tests

Um repositório com código Python de exemplo para testar funcionalidades do Github e outras aplicações.

> O código presente neste repositório poderá conter erros, bugs e problemas de segurança. **O código aqui presente não deverá ser utilizado em produção**.

## Ações

Abaixo está descrito o que acontece quando o código no repositório é atualizado.

### Github Actions

![Calculadora](https://github.com/afonsosantos/python-tests/workflows/Calculadora/badge.svg)

A cada `push` e `pull request` um conjunto de passos e testes são executados, e o resultado reportado junto de cada commit.
O ficheiro com os passos pode ser visto [aqui](.github/workflows/python-app.yml).

### DeepSource

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/afonsosantos/python-tests/?ref=repository-badge)

Este serviço verifica o código Python por inconsistência, bugs, problemas de segurança, performance e muito mais. É executado a cada `push` e `pull request` para o repositório.

