import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #oczekiwanie na strone
from selenium.webdriver.common.by import By

# login = ''
# password = ''
driver = webdriver.Chrome()
def start():
    driver.get("https://www.facebook.com")
    time.sleep(1)
    # driver.find_element(By.ID, "email").send_keys(login)
    # driver.find_element(By.ID, "pass").send_keys(password)
    # time.sleep(5)
    # driver.find_element(By.NAME, "login").click()
    # loaded = expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Nie masz kodu?'))
    # WebDriverWait(driver, 10).until(loaded)
    # driver.find_element(By. LINK_TEXT, "Nie masz kodu?").click()
    # driver.find_element(By. LINK_TEXT, "Chcę dostać SMS z kodem logowania").click()
    # driver.find_element(By. LINK_TEXT, "Zamknij").click()
    # auth_code = input("podaj kod: ")
    # driver.find_element(By.ID, "approvals_code").send_keys(auth_code)
    # driver.find_element(By.ID, 'checkpointSubmitButton').click()  #przekarz kod uwierzytelniania
    input("kliknij enter jak przejdziesz do strony glownej")


def unfollow():
    try:
        print('wczytuje strone...')
        #przejscie do zakładki - Dziennik aktywnosci / Kontakty / Strony, polubienia stron i zainteresowania"
        driver.get("https://www.facebook.com/100002743730769/allactivity?activity_history=false&category_key=LIKEDINTERESTS&manage_mode=false&should_load_landing_page=false")
        #czekanie na załadowanie przycisku 3 kropek
        loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Opcje działania"]'))
        WebDriverWait(driver, 15).until(loaded)
        time.sleep(3)
        # załadowanie ikon 3 kropek przy każdym wyświetlonym polubieniu strony
        options = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Opcje działania"]')
        for i in range(2, 1000):
            try:
                #usunięcie 3ciej polubionej strony od góry
                options[2].click()
                #czekanie na załadowanie przycisku "Nie lubię"
                loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[role="menuitem"]'))
                WebDriverWait(driver, 5).until(loaded)
                unlike = driver.find_element(By.CSS_SELECTOR, '[role="menuitem"]')
                #kliknięcie przycisku "Nie lubię"
                unlike.click()
                print(f'strona o indeksie {i} usunieta')
                time.sleep(1)
            except:
                print("nie zdazyl")
                time.sleep(5)
                options[2].click()
                loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[role="menuitem"]'))
                WebDriverWait(driver, 5).until(loaded)
                time.sleep(1)
                unlike = driver.find_element(By.CSS_SELECTOR, '[role="menuitem"]')
                unlike.click()
                time.sleep(1)
    except:
        print("Blad z wczytywaniem strony")


start()
for i in range(100):
    print(f'odpalanie funkcji unfollow poraz {i}')
    try:
        unfollow()
    except:
        print('ERROR')
