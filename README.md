# Busca CEP

Aplicativo desktop para consulta de endereço por CEP utilizando interface gráfica Tkinter e integração com a API brazilcep.


## Descrição
Este projeto permite ao usuário consultar dados de endereço a partir de um CEP brasileiro, exibindo as informações em uma interface intuitiva. Utiliza a biblioteca brazilcep para integração com serviços de consulta de CEP.

## Requisitos
- Python 3.7 ou superior
- pip
- Bibliotecas: `tkinter`, `requests`, `brazilcep`

## Instalação
1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Instale as dependências:
   ```bash
   pip install requests brazilcep
   ```
   > Obs: `tkinter` já vem instalado nas distribuições padrão do Python.

## Execução
1. Navegue até a pasta do projeto:
   ```bash
   cd busca_cep
   ```
2. Execute o aplicativo:
   ```bash
   python Busca_Cep.py
   ```

## Uso
- Digite o CEP desejado no campo indicado.
- Clique em "Buscar" para consultar o endereço.
- Os campos de endereço, bairro, cidade e UF serão preenchidos automaticamente.
- Para limpar os campos, clique em "Limpar".

## Customização
- Para alterar cores, fontes ou layout, edite o arquivo `Busca_Cep.py` nas funções de interface.
- Para adicionar novas funcionalidades, utilize as classes e métodos já documentados no código.

## Testes
- Para testar a aplicação, execute o arquivo principal e utilize diferentes CEPs válidos e inválidos.
- Teste o tratamento de erros digitando CEPs incompletos ou inexistentes.

## Deploy
Para distribuir o aplicativo como executável:
1. Instale o `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Gere o executável:
   ```bash
   pyinstaller --onefile Busca_Cep.py
   ```
3. O executável estará disponível na pasta `dist`. Basta compartilhar o arquivo gerado.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---
Desenvolvido por Hélio do Nascimento Silva.
