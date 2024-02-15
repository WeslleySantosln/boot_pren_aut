from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import ezodf

def preencher_senha(login,senha, driver):
    
    # Preenche o campo Nome
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/form/div/div[2]/input").send_keys(login)

    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/form/button/span/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/div/div[2]/a/span/span/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/button/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div[2]/div/div/div/div/div/input").send_keys(senha)
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/button/span").click()
    time.sleep(15)
    
    
def preencher_formulario(dados, driver):
    #nome completo
    #driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/input").send_keys(dados[0])
    time.sleep(1)
    #ID MATEUS
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[4]/div[1]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[1])
    time.sleep(1)
    #CPF
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[2])
    time.sleep(1)
    #SETOR
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[5]/div[1]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[3])
    time.sleep(1)
    #CARGO
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[5]/div[2]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[4])
    time.sleep(1)
    #EMAIL DO COLABORADOR
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[6]/div[1]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[5])
    time.sleep(1)
    #CETRO DE CUSTO E FILIAL
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[6]/div[2]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[6],"\t",dados[7],"\n")
    #EMPRESA
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[7]/div[2]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[8])
    #CIDADE FILIAL E ESTADO
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[8]/div[1]/div/div[3]/div/div/div[3]/div/input").send_keys(dados[9],"\t",dados[10],"\n")
    #NOME COMPLETO DO GERENTE DO USUARIO EM CRIACAO
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[11]/div/div/div[3]/div/input").send_keys(dados[11])
    #EMAIL COMPLETO DO GERENTE 
    time.sleep(20)
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[12]/div/div/div[3]/div/input").click()
    time.sleep(20)
    #VOLTA A PAGINA

    
   
    

    
def main():
    # Caminho do arquivo ODS
    file_path = r'C:\Users\tarcisio.chaves\OneDrive - Grupo Mateus\Área de Trabalho\teste\boot_pren_aut-main\boot_pren_aut-main\lista.ods'

    # Configurações do Selenium
    driver_path = r'C:\Users\tarcisio.chaves\OneDrive - Grupo Mateus\Área de Trabalho\teste\boot_pren_aut-main\boot_pren_aut-main\chromedriver.exe'  # Substitua pelo caminho do seu chromedriver.exe
    url = 'https://grupomateus.atlassian.net/servicedesk/customer/portal/18/create/635'

    
    spreadsheet = ezodf.opendoc(file_path) # Carrega a planilha
    sheet = spreadsheet.sheets[0]  # Assume que a planilha desejada está na primeira folha

    # Configuração do WebDriver para o Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    

    # Verifica se o driver existe no caminho fornecido
    if os.path.exists(driver_path):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # Abre o navegador em tela cheia
        driver.get(url)
        time.sleep(5)
        
        # Preenche os campos no site
        login = "weslley.santana@grupomateus.com.br"
        senha = "Dea3665@."
        preencher_senha(login,senha, driver)
        
        for row in sheet.rows():
            time.sleep(2)
            dados = [cell.value for cell in row]
            preencher_formulario(dados, driver)
            time.sleep(15)
            driver.get(url)

            
            
            
            
            # Aguarda alguns segundos para visualizar o preenchimento
            #time.sleep(10)

            # Limpa os campos para a próxima iteração
            #preencher_formulario("", "", "", driver)

            # Aguarda mais alguns segundos antes de continuar
            #time.sleep(10)
    else:
        print("Caminho do chromedriver.exe inválido. Verifique o caminho fornecido no script.")

if __name__ == "__main__":
    main()
