Projeto de Integrações_apis_terceiros

O projeto realiza uma integração com a API Fiscal data.
* Resumo
  - Realizando uma requisição HTTP GET.
  - Verificação do Status Code da resposta.
  - Percorrer ao possíveis falhas de conexão.
  - Converte a resposta para JSON.
  - Esse irá exiber os cincos primeiros registros retornados pela API.

* Ferramentas ulilizadas
  - Python (Principal ferramenta para criar o programa)
  - Requests (A nossa requisição para buscar a URL)
  - API (Sistema intermediário para troca entre  dados em sistemas )
  - JSON (Converte ás taxas e data em JSON, formato padrão para troca de sistema)

*Estudos
 - Com esse projeto tenho a noção de que é mexer com API, sistema que permitir trocar de dados entre sistemas, podendo aprender ainda mais com praticas e com novos desafios.

*Funções e seus objetivos
 -Import Requests ( Usei a biblioteca "Requests", para pode usar ás ferramentas certas para poder criar o programa)
 - Definir a URL da API (Como é Integrações_apis_terceiros, resolvi pegar a da fiscal data - https://api.fiscaldata_treasury... )
 - Depois usamos a requisição para http GET.
 - Usamos try,except (Possíveis erros) com if,elif,else (Caminhos provaveis) para que o comando não tenha erros de trava ou caminhos sem rumo
 - Usando For para percorrer os registros e depois exibir os cincos primeiros resgistros
 - E por fim mostrar o resultado na tela 