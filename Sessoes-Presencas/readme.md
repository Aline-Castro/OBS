---

# Extrator de Dados de Presença dos Parlamentares

Este script extrai dados de presença dos parlamentares da cidade de São Paulo/SP para um mês específico a partir de uma API e gera planilhas Excel com essas informações.

## Funcionalidades

- Extrai dados de presença diários dos parlamentares de uma API.
- Utiliza execução paralela para acelerar a extração dos dados.
- Organiza os dados por parlamentar e data de sessão.
- Gera planilhas Excel individuais para cada parlamentar contendo suas presenças.
- Cria diretórios automaticamente para organizar os arquivos gerados.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `json`
  - `pandas`
  - `beautifulsoup4`
  - `openpyxl` 

## Instalação

1. Clone este repositório para sua máquina local:
   ```sh
   git clone https://github.com/seuusuario/seurepositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```sh
   cd seurepositorio
   ```

3. Instale as dependências:
   ```sh
   pip install requests pandas beautifulsoup4 openpyxl
   ```

## Uso

1. Execute o script Python:
   ```sh
   python extrator_presenca.py
   ```

2. Insira o ano e o mês para os quais você deseja extrair os dados de presença quando solicitado:
   ```
   Digite o ano: 2023
   Digite o mês: 7
   ```

3. O script irá extrair os dados de presença dos parlamentares para o mês especificado e gerar planilhas Excel para cada parlamentar.

4. As planilhas serão salvas no diretório `C:/Voluntario/PRESENCA-2023/{ano}-{mes}` (por exemplo, `C:/Voluntario/PRESENCA-2023/2023-07`).

## Estrutura do Projeto

```
extrator_presenca/
│
├── extrator_presenca.py      # Script principal para extração e geração das planilhas
└── README.md                 # Este arquivo README
```

## Contribuição

Se você quiser contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```sh
   git checkout -b minha-nova-funcionalidade
   ```
3. Faça suas alterações e comite-as:
   ```sh
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Faça um push para a branch:
   ```sh
   git push origin minha-nova-funcionalidade
   ```
5. Abra um pull request.

---
