# Sistema de Monitoramento de Reservatório de Água

Este projeto é uma simulação simples de um sistema de monitoramento de um reservatório de água, desenvolvido em Python.  
O objetivo é exibir mensagens de alerta no terminal com cores diferentes, de acordo com o nível de água do reservatório.

## 🎯 Objetivo
Facilitar a visualização da situação do reservatório, destacando cada nível com uma cor específica, utilizando a biblioteca **colorama**.

## ⚙️ Funcionamento
O sistema trabalha com **cinco níveis de água**, cada um associado a uma mensagem e uma cor:

| Nível | Situação                  | Cor    |
|-------|---------------------------|--------|
| 1     | Muito baixo (crítico)     | Vermelho |
| 2     | Baixo                     | Amarelo |
| 3     | Médio                     | Verde |
| 4     | Alto                      | Ciano |
| 5     | Muito alto (alerta)       | Azul |

### Estrutura do programa
- **Lista de mensagens**: armazena os textos correspondentes a cada nível.
- **Função `cor_por_nivel`**: retorna a cor apropriada para o nível informado.
- **Loop de simulação**: percorre todos os níveis e imprime a mensagem com a cor correspondente.
- **Colorama**: garante que as cores sejam exibidas corretamente em diferentes sistemas operacionais e restaura o estilo padrão após cada impressão.

## 📦 Dependências
- Python 3.x
- Biblioteca [colorama](https://pypi.org/project/colorama/)

Importação da biblioteca:
```from colorama import Fore, Style, init
