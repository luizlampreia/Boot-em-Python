from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
from faker import Faker

# Inicializa o Faker
faker = Faker('pt_BR')

# Função para gerar telefone no formato (99) 9 9999-9999
def gerar_telefone():
    ddd = random.randint(11, 99)
    primeiro = random.randint(9000, 9999)
    segundo = random.randint(1000, 9999)
    return f"({ddd}) 9 {primeiro}-{segundo}"

# Função para gerar 10 usuários aleatórios
def gerar_usuarios(qtd=10):
    usuarios = []
    qtd_bones_options = ["-30", "+30", "+50", "+100", "+300", "+1000", "+3000", "+10000"]
    prioridade_options = ["Alta qualidade", "Bom custo-benefício", "Menor preço possível"]
    segmento_options = [
        "Agência de Eventos", "Agência de Publicidade", "Agronegócio", "Automotivo",
        "Indústria", "Mercado Financeiro", "Mercado Imobiliário", "Turismo",
        "Varejo e vestuário", "Outros"
    ]
    finalidade_options = [
        "Presentear Clientes", "Realizar ações comerciais", "Realizar ações de marketing",
        "Para a equipe da empresa", "Para revender", "Outros"
    ]
    
    for _ in range(qtd):
        usuarios.append({
            'nome': faker.name(),
            'telefone': gerar_telefone(),
            'email': faker.email(),
            'qtdBones': random.choice(qtd_bones_options),
            'prioridadeProduto': random.choice(prioridade_options),
            'segmento': random.choice(segmento_options),
            'finalidade': random.choice(finalidade_options)
        })
    return usuarios

# Lista de usuários aleatórios
usuarios = gerar_usuarios(10)

# Inicializa o driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Lista para relatório
relatorio_envios = []

for idx, usuario in enumerate(usuarios, start=1):
    driver.get("https://seubone.com/")  # URL do formulário
    time.sleep(2)
    
    try:
        # Passo 1: Telefone
        tel_input = wait.until(EC.presence_of_element_located((By.ID, "telefone-etapa")))
        tel_input.clear()
        tel_input.send_keys(usuario['telefone'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 2: Email
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email-etapa")))
        email_input.clear()
        email_input.send_keys(usuario['email'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 3: Nome
        nome_input = wait.until(EC.presence_of_element_located((By.ID, "nome-etapa")))
        nome_input.clear()
        nome_input.send_keys(usuario['nome'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 4: Quantidade de bonés e prioridade
        qtd_select = Select(wait.until(EC.presence_of_element_located((By.ID, "qtd-bones-etapa"))))
        qtd_select.select_by_value(usuario['qtdBones'])
        prioridade_select = Select(wait.until(EC.presence_of_element_located((By.ID, "prioridade-escolher-produto"))))
        prioridade_select.select_by_value(usuario['prioridadeProduto'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 5: Segmento da empresa
        segmento_select = Select(wait.until(EC.presence_of_element_located((By.ID, "segmento-etapa"))))
        segmento_select.select_by_value(usuario['segmento'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 6: Finalidade dos bonés
        finalidade_select = Select(wait.until(EC.presence_of_element_located((By.ID, "finalidade-etapa"))))
        finalidade_select.select_by_value(usuario['finalidade'])
        driver.find_element(By.ID, "next").click()
        time.sleep(1)

        # Passo 7: Último passo - clicar em "Solicitar Orçamento"
        orcamento_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="solicitar-orcamento"]')))
        orcamento_btn.click()
        time.sleep(1)

        # Confirmação
        print(f"✅ Usuário {idx} enviado: {usuario['nome']} - {usuario['telefone']}")
        relatorio_envios.append({'usuario': usuario, 'enviado': True})

    except Exception as e:
        print(f"❌ Erro ao enviar usuário {idx}: {e}")
        relatorio_envios.append({'usuario': usuario, 'enviado': False, 'erro': str(e)})

# Salva relatório em JSON
with open("relatorio_envios.json", "w", encoding="utf-8") as f:
    json.dump(relatorio_envios, f, ensure_ascii=False, indent=4)

driver.quit()
print("📄 Relatório salvo em 'relatorio_envios.json'")
















