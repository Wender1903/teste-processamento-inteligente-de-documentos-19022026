# Teste Técnico (Extração de informações em Faturas de Energia)

Para garantir o eficiente gerenciamento dos créditos de energia provenientes de usinas de energia renovável, é fundamental a extração precisa e automática de dados das notas fiscais de energia elétrica. Além disso, possuir conhecimento sobre faturas de energia elétrica é importante para o sucesso na gestão desses recursos.

Logo, é proposto dois testes como parte da avaliação dos conhecimentos técnicos e teóricos dos candidatos. Essa avaliação tem o objetivo de medir a compreensão do participante no contexto da extração de dados de notas fiscais e no entendimento básico de faturas de energia elétrica.

# Teste 1

Em busca pela eficiência na leitura de faturas, a equipe de desenvolvimento propõe a criação de uma rotina que, a partir de faturas de energia elétrica em formato de PDF, seja capaz de extrair importantes informações.

Nesta atividade, você deve editar o arquivo read.py e desenvolver uma rotina capaz de realizar a leitura da fatura fatura_cpfl.pdf em formato de PDF e retornar as seguintes informações:

- Titular da fatura (Nome e Documento)
- Endereço completo do titular da fatura
- Classificação da Instalação
- Número da instalação
- Valor a Pagar para a distribuidora
- Data de Vencimento
- Mês ao qual a fatura é referente
- Tarifa total com tributos
- Tarifa total Aneel
- Quantidade em kWh do Consumo da fatura
- Saldo em kWh acumulado na Instalação
- Somatório das quantidades das energias compensadas (injetadas)
- Somatório dos Valores Totais das Operações R$
- Contribuição de iluminação Pública
- Alíquotas do ICMS, PIS e COFINS em %
- Linha digitável para pagamento

Organize a saída e visualização das informações extraídas.

# Documentação do Teste 1

Escreva aqui a documentação do desenvolvimento do teste 1.

---

## Teste 1 – Processamento de Faturas da CPFL

### 1. Ferramentas e Bibliotecas Utilizadas

- **pdfplumber**: leitura e extração de texto de PDFs.  
- **reportlab**: geração de PDF organizado com os dados extraídos.  
- **Python standard libraries**: manipulação de strings, listas e dicionários.  

---

### 2. Solução Implementada

O arquivo `read.py` implementa a classe `FaturaCPFL`, que possui os seguintes métodos:

#### 2.1. `ler_pdf()`
- Abre o PDF utilizando `pdfplumber`.  
- Lê todas as páginas e junta o texto em uma lista de linhas (`self.texto`).  

#### 2.2. `extrair_dados()`
- Percorre cada linha do PDF buscando palavras-chave específicas.  
- Extrai os dados desejados, tratando números com vírgula e ponto.  
- Cria um dicionário `self.dados_lidos` com todos os campos solicitados.  

#### 2.3. `processar()`
- Une a leitura do PDF e a extração de dados em um único passo.  
- Retorna o dicionário com todos os dados extraídos.  

#### 2.4. `exibir_dados()`
- Imprime no console todos os dados extraídos de forma organizada.  

#### 2.5. `gerar_pdf_organizado()`
- Cria um PDF de saída com todos os dados, no formato “Chave: Valor”.  
- Adiciona observação para campos não encontrados:  
  > Obs: os valores 'None' é porque não consegui realizar a busca.  

---

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

# Resposta para o Teste 2
## 1-)
### A fatura fatura_cemig.pdf refere-se a uma unidade com Geração Distribuída (GD), enquanto a fatura convencional é de consumo simples. Ela inclui créditos de energia compensada que reduzem o valor final. Diferente da fatura convencional, que apresenta apenas "Energia Elétrica" e "Contribuição de Iluminação Pública", a fatura com GD detalha a energia injetada e compensada. Também mostra o saldo acumulado de geração e inclui uma doação para "Ass Combt Câncer", ausente na fatura convencional.

## 2-)
### Valores Faturados - fatura_cemig.pdf (julho/2023)

- **Energia Elétrica**: 50 kWh – R$ 47,96  
- **Energia SCEE s/ ICMS**: 149 kWh – R$ 76,26  
- **Energia compensada GD II**: 149 kWh – desconto R$ 67,24  
- **Energia comp. adicional**: 7 kWh – desconto R$ 5,24  
- **Bônus Itaipu**: desconto R$ 9,79  
- **Ass Combt Câncer**: doação R$ 10,00  
- **Contrib Ilum Pública**: R$ 24,71  

**Total a pagar:** R$ 76,66

## 3-)
### A informação mais importante na seção Informações Gerais é o Saldo Atual de Geração, que é 234,63 kWh. Esse valor mostra a energia que você gerou e ainda não usou, que pode ser usada para reduzir o consumo das próximas faturas.

## 4-) 
### O consumo da instalação identificado na fatura referente ao mês de julho de 2023 é de 199 kWh.


# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 12:30h.
