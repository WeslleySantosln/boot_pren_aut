from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import ezodf

def preencher_senha(login,senha, driver):
    
    # Preenche o campo Nome
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/form/div[1]/input").send_keys(login)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/form/div[2]/div/input").send_keys(senha)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/form/div[4]/input[2]").click()
    time.sleep(28)
     #Cadastro
    driver.find_element(By.XPATH, "/html/body/div[12]/div[2]/div[4]/div").click()
    time.sleep(2)
    
    
def preencher_formulario(dados, driver):
    #Terminal
    driver.find_element(By.XPATH, "/html/body/div[12]/div[2]/span[4]/div[4]/div").click()
    time.sleep(2)
    #Escolher filtro loja
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div/div[1]/div/div[1]/div/div[1]/select").send_keys("loja","\n","\t")
    time.sleep(2)
    #Loja
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div/div[1]/div/div[1]/div/div[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div/div[1]/div/div[1]/div/div[2]/input").send_keys(dados[0])
    time.sleep(2)
    #Abrir Nova Pagina
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[1]/div[3]/div[2]/div[1]/div").click()
    time.sleep(2)
    #Loja
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div[2]/div/div/div[1]/input").send_keys(dados[0],"\n")
    time.sleep(2)
    #PDV
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div[2]/div/div/div[4]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div[2]/div/div/div[4]/input").send_keys(dados[1])
    time.sleep(2)
    #descrição e 
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div[2]/div/div/div[5]/input").send_keys(dados[2],"\t",dados[3],"\n")
    time.sleep(2)
    #conjunto
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[2]/div[2]/div/div/div[7]/input").send_keys(dados[4],"\n")
    time.sleep(2)
    #salvar
    driver.find_element(By.XPATH, "/html/body/div[13]/form/div[1]/div[3]/div[2]/div[1]/div").click()   
    time.sleep(1)
    #salvar
    driver.find_element(By.XPATH, "/html/body/div[6]/center/div[1]").click()   
    time.sleep(5)
    


    
   
    

    
def main():
    # Caminho do arquivo ODS
    file_path = r'C:\Users\tarcisio.chaves\OneDrive - Grupo Mateus\Área de Trabalho\teste\boot_pren_aut-main\boot_pren_aut-main\listaPDV.ods'

    # Configurações do Selenium
    driver_path = r'C:\Users\tarcisio.chaves\OneDrive - Grupo Mateus\Área de Trabalho\teste\boot_pren_aut-main\boot_pren_aut-main\chromedriver.exe'  # Substitua pelo caminho do seu chromedriver.exe
    url = 'https://rhsso.grupomateus.com.br/auth/realms/grupomateus/protocol/openid-connect/auth?client_id=maxipos&redirect_uri=http%3A%2F%2Fpdv.mateus%2Fmaxipos_backoffice%2Fkeycloack.html&state=f4b9fa2c-888a-40fb-869a-bdf3f77c97d5&response_mode=fragment&response_type=code&scope=openid&nonce=386ac1e0-d402-4105-84c4-e209fa4aa91c'
    
    
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
        login = "gm0040721"
        senha = "Processador@2022"
        preencher_senha(login,senha, driver)
        
        for row in sheet.rows():
            time.sleep(2)
            dados = [cell.value for cell in row]
            preencher_formulario(dados, driver)
            time.sleep(15)
            

    else:
        print("Caminho do chromedriver.exe inválido. Verifique o caminho fornecido no script.")

if __name__ == "__main__":
    main()
