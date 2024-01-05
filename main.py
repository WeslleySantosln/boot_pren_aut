from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import ezodf

def preencher_formulario(nome, driver):
    # Preenche o campo Nome
    driver.find_element(By.XPATH, "/html/body/span[2]/div[2]/div/div/div[2]/main/div/div/div/div[3]/form/div/div[2]/input").send_keys(nome)

    
def main():
    # Caminho do arquivo ODS
    file_path = r'C:\Users\wesley.santana\Documents\teste\teste.ods'

    # Configurações do Selenium
    driver_path = r'C:\Users\wesley.santana\Documents\teste\chromedriver.exe'  # Substitua pelo caminho do seu chromedriver.exe
    url = 'https://grupomateus.atlassian.net/servicedesk/customer/portal/18/create/635'

    # Carrega a planilha
    spreadsheet = ezodf.opendoc(file_path)
    sheet = spreadsheet.sheets[0]  # Assume que a planilha desejada está na primeira folha

    # Configuração do WebDriver para o Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    

    # Verifica se o driver existe no caminho fornecido
    if os.path.exists(driver_path):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # Abre o navegador em tela cheia
        driver.get(url)

        try:
            # Preenche os campos no site
            for row in sheet.rows():
                time.sleep(5)
                nome = [cell.value for cell in row]
                preencher_formulario(nome, driver)

                # Aguarda alguns segundos para visualizar o preenchimento
                time.sleep(10)

                # Limpa os campos para a próxima iteração
                preencher_formulario("", "", "", driver)

                # Aguarda mais alguns segundos antes de continuar
                time.sleep(10)

        finally:
            # Fecha o navegador ao finalizar
            time.sleep(10)
            driver.quit()
    else:
        print("Caminho do chromedriver.exe inválido. Verifique o caminho fornecido no script.")

if __name__ == "__main__":
    main()
