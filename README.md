# Atividades de Aulas Python - BFD

![Banner_BFD](https://github.com/user-attachments/assets/96ffe3d6-8e92-4eb7-8e13-8f0395b5e8c2)

Este repositório contém uma coleção abrangente de scripts Python desenvolvidos durante as aulas de programação. O projeto está organizado em categorias temáticas para facilitar o aprendizado progressivo e a consulta rápida.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades por Categoria](#funcionalidades-por-categoria)
- [Como Executar os Scripts](#como-executar-os-scripts)
- [Projetos Integradores](#projetos-integradores)
- [Contribuição](#contribuição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

## 🎯 Visão Geral

Este projeto demonstra a evolução do aprendizado em Python, desde conceitos básicos até aplicações práticas mais complexas. Cada script é independente e focado em demonstrar conceitos específicos de programação.

## ⚙️ Pré-requisitos

- **Python 3.6+** (recomendado 3.8+)
- **Sistema Operacional**: Windows, Linux ou macOS
- **Editor de Texto**: VS Code, PyCharm ou similar (opcional)

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Atividades-BFD.git
cd Atividades-BFD
```

### 2. Verifique a instalação do Python
```bash
python --version
# ou
python3 --version
```

### 3. Instale as dependências
> ⚠️ **Nota**: Este projeto utiliza apenas a biblioteca padrão do Python. Não há dependências externas necessárias.

```bash
# O arquivo requirements.txt apenas documenta que não há dependências externas
cat requirements.txt
```

## 📁 Estrutura do Projeto

```
Atividades-BFD/
├── atividades/                    # Diretório principal dos scripts
│   ├── conceitos_basicos/        # Fundamentos de programação
│   ├── operacoes_matematicas/    # Cálculos e operações
│   ├── manipulacao_strings/      # Processamento de texto
│   ├── listas_arrays/           # Estruturas de dados
│   ├── tuplas/                  # Tipos de dados imutáveis
│   ├── aplicacoes/              # Aplicações intermediárias
│   ├── aplicacoes_praticas/     # Exercícios práticos
│   ├── basico/                  # Conceitos básicos de listas
│   ├── processamento/           # Processamento de dados
│   └── listas_exercicios/       # (diretório vazio - reservado)
├── requirements.txt              # Lista de dependências
├── LICENSE                      # Licença do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Este arquivo
```

## 🔧 Funcionalidades por Categoria

### 🟢 Conceitos Básicos
Fundamentos essenciais de programação Python.

- **`saudacao_usuario.py`**: Interação básica com usuário através de input/output
- **`valores_trocados.py`**: Demonstração de troca de valores entre variáveis
- **`valida_senha.py`**: Validação de senha com critérios específicos

### 🧮 Operações Matemáticas
Scripts focados em cálculos e operações numéricas.

- **`calculo_media.py`**: Calcula média aritmética de números
- **`calculo_quadrilatero.py`**: Calcula área e perímetro de quadriláteros
- **`calculo_soma.py`**: Realiza soma simples de números
- **`comparar_numeros.py`**: Comparação entre dois números
- **`maior_de_cinco.py`**: Identifica o maior entre cinco números
- **`maior_menor.py`**: Encontra maior e menor em uma lista
- **`numeros_pares.py`**: Lista números pares em um intervalo
- **`soma_ate_zero.py`**: Soma números até entrada zero
- **`soma_mult_numeros.py`**: Soma e multiplicação de números
- **`soma_quadrados.py`**: Calcula soma dos quadrados
- **`tabuada_while.py`**: Gera tabuada usando loop while
- **`verificador_par.py`**: Verifica paridade de números

### 🔤 Manipulação de Strings
Processamento e análise de texto.

- **`contador_de_vogais.py`**: Conta vogais em strings

### 📊 Listas e Arrays
Manipulação de coleções e estruturas de dados.

- **`acesso_indice.py`**: Acesso a elementos por índice
- **`add_elementos.py`**: Adição dinâmica de elementos
- **`dias_sem.py`**: Manipulação de dias da semana
- **`frutas.py`**: Gerenciamento de lista de frutas
- **`lista_laco.py`**: Iteração com loops
- **`listas_simples.py`**: Criação básica de listas
- **`numeros_inteiros.py`**: Manipulação de números inteiros
- **`numeros_reais_inverso.py`**: Ordenação inversa de reais
- **`ocorrencia.py`**: Contagem de ocorrências
- **`ordenacao.py`**: Ordenação de elementos
- **`pares_impares.py`**: Separação de pares e ímpares
- **`rem_element.py`**: Remoção de elementos
- **`sum_elementos.py`**: Soma de elementos de lista

### 📦 Tuplas
Trabalho com estruturas de dados imutáveis.

- **`conversao_lista-tupla.py`**: Conversão entre listas e tuplas
- **`immutabilidade.py`**: Demonstração de imutabilidade
- **`pesq_tupla.py`**: Pesquisa em tuplas
- **`sum_tupla.py`**: Soma de elementos em tupla
- **`tupla_simples.py`**: Criação básica de tuplas

### 🎯 Aplicações
Aplicações práticas que integram múltiplos conceitos.

- **`calcular_medias_alunos.py`**: Calcula médias de múltiplos alunos
- **`tabuleiro_xadrez.py`**: Representação visual de tabuleiro de xadrez

### 📈 Aplicações Práticas
Exercícios focados em casos de uso reais.

- **`altura_idade_maior.py`**: Comparação de altura e idade
- **`alunos_aprovados.py`**: Sistema de aprovação escolar
- **`notas_e_media.py`**: Calculadora de notas acadêmicas

### 📚 Básico
Conceitos introdutórios de manipulação de listas.

- **`adicionar_livros.py`**: Adiciona livros a uma lista
- **`inserir_livro_posicao.py`**: Insere livros em posições específicas
- **`lista_livros_basica.py`**: Lista básica de livros
- **`primeiro_ultimo_livro.py`**: Acesso ao primeiro e último elemento
- **`remover_livro.py`**: Remoção de livros da lista

### ⚙️ Processamento
Scripts de processamento e análise de dados.

- **`contar_ocorrencias.py`**: Conta ocorrências em listas
- **`filtrar_maiores_idade.py`**: Filtra maiores de idade
- **`listar_livros.py`**: Lista organizada de livros
- **`somar_valores.py`**: Soma valores de uma lista

## 🏃 Como Executar os Scripts

### Método 1: Executar individualmente
```bash
# Navegue até o diretório do script
python atividades/categoria/nome_do_script.py

# Exemplos:
python atividades/conceitos_basicos/saudacao_usuario.py
python atividades/operacoes_matematicas/calculo_media.py
python atividades/listas_arrays/frutas.py
```

### Método 2: Usando caminho completo
```bash
# Windows
python "C:\Users\seu-usuario\Atividades-BFD\atividades\conceitos_basicos\saudacao_usuario.py"

# Linux/macOS
python "/home/seu-usuario/Atividades-BFD/atividades/conceitos_basicos/saudacao_usuario.py"
```

### Método 3: Executar todos de uma categoria
```bash
# Windows PowerShell
Get-ChildItem "atividades\operacoes_matematicas\*.py" | ForEach-Object { python $_.FullName }

# Linux/macOS
for file in atividades/operacoes_matematicas/*.py; do python "$file"; done
```

## 🎯 Projetos Integradores

### 🎥 [Streamly](https://github.com/charlles-augusto/Streamly)

Sistema de streaming de vídeo desenvolvido em Python que integra conceitos avançados:

- **Manipulação de arquivos**: Leitura/escrita de dados
- **Programação orientada a objetos**: Classes e encapsulamento
- **Estruturas de dados**: Listas, dicionários e tuplas
- **Controle de fluxo**: Loops e condicionais avançados
- **Validação de dados**: Tratamento de entrada do usuário

### 🔗 Como os Conceitos se Conectam

| Conceitos Básicos | → | Fundamentos para qualquer aplicação |
|-------------------|---|-------------------------------------|
| Operações Matemáticas | → | Cálculos e algoritmos em projetos |
| Manipulação de Strings | → | Processamento de texto e dados |
| Listas e Arrays | → | Gerenciamento de coleções de dados |
| Tuplas | → | Estruturas imutáveis para configurações |
| Aplicações Práticas | → | Casos de uso reais e integração |

## 🚀 Desenvolvimento e Próximos Passos

### 📋 Roadmap de Desenvolvimento

#### Fase 1: Completude (Atual)
- ✅ Todos os scripts básicos implementados
- ✅ Documentação completa
- ✅ Organização por categorias

#### Fase 2: Melhorias (Em Progresso)
- 🔄 Adicionar testes unitários
- 🔄 Implementar tratamento de erros
- 🔄 Adicionar interface gráfica para alguns scripts

#### Fase 3: Novos Projetos (Planejado)
- 📋 Sistema de gerenciamento de biblioteca
- 📋 Calculadora científica com interface gráfica
- 📋 Jogo de adivinhação com persistência de dados
- 📋 Sistema de cadastro de estudantes com arquivo CSV

### 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.8+
- **Biblioteca padrão**: `sys`, `os`, `math`, `random`, `datetime`
- **Sem dependências externas**: Propositadamente para facilitar aprendizado
- **Versionamento**: Git e GitHub
- **Documentação**: Markdown

## 🤝 Contribuição

Sinta-se à vontade para contribuir com este projeto! Toda contribuição é bem-vinda.

### Como Contribuir

1. **Fork o repositório**
   ```bash
   git clone https://github.com/seu-usuario/Atividades-BFD.git
   ```

2. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

3. **Faça suas alterações**
   - Adicione novos scripts em categorias apropriadas
   - Siga as convenções de código existentes
   - Adicione documentação para novos scripts

4. **Commit suas mudanças**
   ```bash
   git add .
   git commit -m "feat: adiciona novo script de ordenação"
   ```

5. **Push para sua branch**
   ```bash
   git push origin feature/nova-funcionalidade
   ```

6. **Crie um Pull Request**
   - Descreva claramente as mudanças
   - Referencie issues relacionadas
   - Aguarde revisão

### Diretrizes de Contribuição

- **Código limpo**: Use nomes descritivos e comentários úteis
- **Testes**: Teste seus scripts antes de submeter
- **Documentação**: Atualize o README.md se necessário
- **Padrões**: Siga a estrutura de diretórios existente

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

Se tiver dúvidas ou sugestões:

1. **Abra uma [Issue](https://github.com/seu-usuario/Atividades-BFD/issues)**
2. **Entre em contato**: [charllesgst@gmail.com](mailto:charllesgst@gmail.com)
3. **Documentação**: Este README.md é sua fonte principal de informações

---

**Desenvolvido com ❤️ por charlles**
