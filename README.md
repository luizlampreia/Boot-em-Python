# 🤖 Automação de Formulário Web com Selenium

## 📌 Descrição

Este projeto consiste em um script de automação desenvolvido em **Python**, utilizando a biblioteca **Selenium**, com o objetivo de simular o preenchimento automático de um formulário web.

O script gera dados fictícios de usuários e realiza o envio dessas informações de forma automatizada, navegando por múltiplas etapas do formulário como um usuário real faria.

Além disso, o sistema registra os resultados das tentativas de envio, permitindo análise posterior através de um relatório em formato JSON.

---

## 🧠 O que o Script Faz

O script executa um fluxo completo de automação, simulando interações humanas com um site. O processo ocorre da seguinte forma:

### 🔹 1. Geração de Dados Fictícios

Utilizando a biblioteca Faker, o sistema cria usuários aleatórios contendo:

* Nome completo
* Telefone (formato brasileiro)
* Email
* Preferências simuladas (quantidade, prioridade, segmento, finalidade)

Esses dados são utilizados para preencher o formulário automaticamente.

---

### 🔹 2. Inicialização do Navegador

* Abre o navegador Google Chrome via Selenium
* Maximiza a janela
* Configura um sistema de espera inteligente (`WebDriverWait`)

---

### 🔹 3. Automação do Formulário

Para cada usuário gerado, o script:

1. Acessa o site alvo
2. Preenche o formulário em etapas sequenciais:

   * Telefone
   * Email
   * Nome
   * Quantidade de produtos e prioridade
   * Segmento da empresa
   * Finalidade do pedido
3. Interage com campos de texto e menus dropdown
4. Avança entre etapas clicando nos botões
5. Finaliza o envio clicando em "Solicitar Orçamento"

Todo esse fluxo simula o comportamento de um usuário real navegando no site.

---

### 🔹 4. Tratamento de Erros

* Caso ocorra alguma falha durante o processo, o erro é capturado
* O script continua executando os próximos usuários
* O erro é registrado no relatório

---

### 🔹 5. Geração de Relatório

Ao final da execução, é criado um arquivo:

📄 `relatorio_envios.json`

Contendo:

* Dados do usuário
* Status do envio (sucesso ou falha)
* Mensagens de erro (se houver)

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Selenium
* Faker
* JSON
* ChromeDriver

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install selenium faker
```

---

### 2. Configurar o WebDriver

Baixe o ChromeDriver compatível com sua versão do Google Chrome e:

* Coloque na mesma pasta do projeto
  ou
* Adicione ao PATH do sistema

---

### 3. Executar o Script

```bash
python script.py
```

---

## 📊 Exemplo de Fluxo

1. Gera 10 usuários aleatórios
2. Para cada usuário:

   * Acessa o site
   * Preenche o formulário completo
   * Envia os dados
3. Registra o resultado
4. Salva o relatório final

---

## 📂 Estrutura do Projeto

```
.
├── script.py
├── relatorio_envios.json
└── README.md
```

---

## ⚠️ Aviso de Uso Responsável

Este projeto foi desenvolvido exclusivamente para fins **educacionais** e de **teste de automação**.

O uso deste código para:

* gerar tráfego massivo artificial
* sobrecarregar sistemas
* explorar falhas de serviços
* ou realizar ataques (ex: negação de serviço)

**é proibido e pode ser ilegal**, conforme a legislação vigente.

⚠️ Executar este script em múltiplas máquinas ou em alta frequência pode impactar negativamente a disponibilidade de um site.

O autor não se responsabiliza por qualquer uso indevido deste código.

---

## 🔐 Boas Práticas

* Utilize apenas em ambientes controlados ou com autorização
* Respeite limites de requisições dos sistemas
* Evite execuções em larga escala
* Use ferramentas adequadas para testes de carga

Ferramentas recomendadas:

* Apache JMeter
* Locust

---

## 💡 Possíveis Melhorias

* Substituir `time.sleep()` por esperas mais eficientes
* Implementar modo headless (sem interface gráfica)
* Criar funções reutilizáveis para reduzir repetição
* Adicionar logs detalhados
* Permitir configuração via arquivo externo
* Implementar limites de execução para uso seguro

---

## 🎯 Finalidade do Projeto

Este projeto é ideal para:

* Aprendizado de automação web
* Testes de formulários
* Simulação de usuários
* Estudos com Selenium

---

## 👨‍💻 Autor

Luiz Lampreia Neto
