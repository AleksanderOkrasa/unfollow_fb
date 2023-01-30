import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #oczekiwanie na strone
from selenium.webdriver.common.by import By

# login = ''
# password = ''
nazwisko = 'Okrasa'
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


def unfollow_webs():
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

def delete_unfollows_from_view():
    # przejscie do zakładki - Dziennik aktywnosci / Kontakty / Połączenia
    driver.get('https://www.facebook.com/100002743730769/allactivity?activity_history=false&category_key=FOLLOWCLUSTER&manage_mode=false&should_load_landing_page=false')
    three_dots = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Opcje działania"]')
    for i in range(0, 1000):
        try:
            try:
                three_dots[0].click()
            except:
                three_dots = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Opcje działania"]')

                three_dots[0].click()
            finally:
                driver.find_element(By.CSS_SELECTOR, '[role="menuitem"]').click()   # Kliknięcie przycisku "Usuń"
                loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Usuń"]'))
                WebDriverWait(driver, 5).until(loaded)
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Usuń"]').click() #podtwierdzenie usunięcia
                print(f"usunięto stronę o indexie {i+1}")
        except:
            # przejscie do zakładki - Dziennik aktywnosci / Kontakty / Połączenia
            driver.get('https://www.facebook.com/100002743730769/allactivity?activity_history=false&category_key=FOLLOWCLUSTER&manage_mode=false&should_load_landing_page=false')
            loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Opcje działania"]'))

            WebDriverWait(driver, 15).until(loaded)
            time.sleep(1)
            print("Ponownie załadowano stronę")




        # # czekanie na załadowanie przycisku "Nie lubię"
        # loaded = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[role="menuitem"]'))
        # WebDriverWait(driver, 5).until(loaded)
        # # delete = driver.find_element(By.CSS_SELECTOR, '[role="menuitem"]')
        # # confirm = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Usuń"]')
        # options[0].click()
        # time.sleep(0.1)
        # driver.find_element(By.CSS_SELECTOR, '[role="menuitem"]').click()
        # time.sleep(0.1)
        # driver.find_element(By.CSS_SELECTOR, '[aria-label="Usuń"]').click()
        # time.sleep(0.1)
def unfollow_persons():
    # przejscie do zakładki - Dziennik aktywnosci / Kontakty
    driver.get('https://www.facebook.com/100002743730769/allactivity/?activity_history=false&category_key=YOURCONNECTIONS&manage_mode=false&should_load_landing_page=false')

    #driver.get('https://www.facebook.com/100002743730769/allactivity?activity_history=false&category_key=FOLLOWCLUSTER&manage_mode=false&should_load_landing_page=false')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # przescrollowanie na sam dół strony
    persons = driver.find_elements(By.PARTIAL_LINK_TEXT, f'{nazwisko} obserwuje użytkownika')

    #printowanie
    list = []
    list_of_exceptions = ('Paulina', 'Magdalena', 'Politechnik', 'Wiktoria', 'Kamila', 'Marcelina')
    for person in persons:
        if not person.text[40:-16].startswith(list_of_exceptions):
            list.append(person.text[40:-16])
        else:
            print(f'Pominięto osobę {person.text[40:-16]}')

    #stworzenie słownika - nazwa strony(klucz) i link(wartość
    dictionary = {}
    list_of_exceptions = ('Paulina', 'Magdalena', 'Politechnik', 'Wiktoria', 'Kamila', 'Marcelina')
    for person in persons:
        if not person.text[40:-16].startswith(list_of_exceptions):
            dictionary[person.text[40:-16]] = person.get_attribute('href')
        else:
            print(f'Pominięto osobę {person.text[40:-16]} o linku {person.get_attribute("href")}')

    print(dictionary)


start()
# delete_unfollows_from_view()
# unfollow_webs()
for i in range(100):
    print(f'odpalanie funkcji unfollow poraz {i}')
    try:
        # unfollow_webs()
        pass
    except:
        print('ERROR')


