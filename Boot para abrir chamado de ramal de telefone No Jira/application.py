from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import ezodf

def preencher_senha(login,senha, driver):
    
    # Login
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/form/div/div[2]/input").send_keys(login)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/form/button/span/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/div/div[2]/a/span/span/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/button/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div[2]/div/div/div/div/div/input").send_keys(senha)
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/button/span").click()
    time.sleep(20)
    
    
def preencher_formulario(dados, driver):
    
    # ID FILIAL
    #id_filial_element = driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]")
    #id_filial_element.click()
    #id_filial_element.send_keys(dados[0])
    #time.sleep(20)  # Aguarde um pouco para garantir que a página reaja


    #Escolhar A OPÇÃO VOIP
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[1]/div[2]/div/div[1]/div[1]/span[2]").send_keys()
    time.sleep(20)
    #Escolhar A OPÇÃO VOIP
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/label[3]/input").click()
    time.sleep(1)
    #DIGITAR AS INFORMAÇÕES DO RAMAL
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div[1]/div[2]/form/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/p").send_keys(dados[1])
    time.sleep(100)
    

    
def main():
    # Caminho do arquivo ODS
    file_path = r'teste.ods'

    # Configurações do Selenium
    driver_path = r'chromedriver.exe'  # Substitua pelo caminho do seu chromedriver.exe
    url = 'https://grupomateus.atlassian.net/servicedesk/customer/portal/18/create/563'

    
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
            
    else:
        print("Caminho do chromedriver.exe inválido. Verifique o caminho fornecido no script.")

if __name__ == "__main__":
    main()
