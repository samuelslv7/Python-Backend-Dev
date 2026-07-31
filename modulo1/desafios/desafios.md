# DESAFIOS

## 1 - Extração de Domínios de Email
### Descrição
Os domínios de email são essenciais para categorizar e identificar a origem dos contatos, facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma string contendo múltiplos emails separados por ponto e vírgula e retornar uma lista contendo apenas os domínios de cada um desses emails.

### Entrada
A entrada deve receber uma string contendo emails separados por ponto e vírgula: "email;email;email;...". Cada email é uma string.

### Saída
Deverá retornar uma lista de strings com os domínios dos emails.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|------------|-------|
| ana@example.com;bob@test.com | ['example.com', 'test.com'] |
| carlos@empresa.com;maria@web.com | ['empresa.com', 'web.com'] |
| pedro@mail.com	 | ['mail.com'] |

## 2 - Transformação de Datas

### Descrição
Você está desenvolvendo um sistema que integra com uma API de dados transacionais, onde as datas são fornecidas no formato "DD-MM-YYYY". Sua tarefa é processar essa lista de datas e transformá-las para o formato internacional "YYYY/MM/DD".

### Entrada
A entrada deve receber uma string contendo datas separadas por ponto e vírgula: "DD-MM-YYYY;DD-MM-YYYY;...". Cada data é uma string.

### Saída
Deverá retornar uma lista de strings contendo as datas no formato "YYYY/MM/DD".

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|------------|-------|
|01-01-2020;02-02-2021	| ['2020/01/01', '2021/02/02'] |
|15-05-1999;23-11-2003	| ['1999/05/15', '2003/11/23'] |
|31-12-2022	| ['2022/12/31'] |


## 3 - Conversão de Dados de Temperatura
### Descrição
Você está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica. O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit.
Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática:
TF = (TC × 9/5) + 32
Onde:
TF representa a temperatura em graus Fahrenheit,
TC representa a temperatura em graus Celsius.

### Entrada
A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) representando as temperaturas em graus Celsius.

### Saída
Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---------|-------|
| 0,10,20,30,40	| [32.0, 50.0, 68.0, 86.0, 104.0] |
| -5,-15,5,15,25| [23.0, 5.0, 41.0, 59.0, 77.0] |
| 12,25,30,18,5	| [53.6, 77.0, 86.0, 64.4, 41.0] |