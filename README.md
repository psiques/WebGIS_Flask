**Nome do projeto**: Flask CSV Point Collector

**Descrição**: Este projeto consiste em um aplicativo web desenvolvido em Flask que permite adicionar pontos de latitude e longitude a um arquivo CSV. O aplicativo fornece uma interface simples onde os usuários podem inserir as coordenadas de um ponto e, em seguida, os dados são armazenados no arquivo CSV para posterior uso ou análise.

**Recursos**:
- A página inicial do aplicativo exibe um formulário onde os usuários podem adicionar os pontos.
- Quando um ponto é adicionado através do formulário, os dados de latitude e longitude são coletados e armazenados em um arquivo CSV.
- Se o arquivo CSV ainda não existir, ele será criado automaticamente.
- O aplicativo usa o framework Flask para criar as rotas e gerenciar as requisições HTTP.
- O Flask renderiza um template HTML para exibir a página inicial.
- O Flask recebe a requisição POST do formulário e chama a função `add_point()` para processar os dados e armazená-los no arquivo CSV.
- O Flask também executa o aplicativo quando o arquivo é executado diretamente.

**Instruções de uso**:
1. Certifique-se de ter o Flask instalado em seu ambiente Python.
2. Execute o arquivo Python para iniciar o aplicativo Flask.
3. Acesse a página inicial do aplicativo em um navegador.
4. Preencha os campos de latitude e longitude no formulário e envie os dados.
5. O ponto será adicionado ao arquivo CSV especificado.
6. Uma mensagem de confirmação será exibida indicando que o ponto foi adicionado com sucesso.

Este projeto pode ser útil para coletar e armazenar dados de localização de forma simples, sendo possível expandi-lo para incluir recursos adicionais, como visualização dos pontos em um mapa ou processamento dos dados coletados.
