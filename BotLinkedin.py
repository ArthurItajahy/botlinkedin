from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LinkedinBot:
    def __init__(self, username, password, text):
        self.username = username
        self.password = password
        self.text = text
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Users\user\Desktop\Pythonverse\BotInstagram\geckodriver\geckodriver.exe')

    # input[@name='username']
    # input[@name='password']
    def login(self, intSeguir):
        driver = self.driver
        time.sleep(10)
        driver.get('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(5)
        user_element = driver.find_element_by_xpath("//input[@id='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@id='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.encontrar(intSeguir)
    def encontrar(self,intSeguir):
        driver = self.driver
        driver.get('https://www.linkedin.com/search/results/people/?keywords=tech%20recruiter&origin=TYPEAHEAD_HISTORY&position=0&searchId=df73d4ff-3dce-495e-ae09-c4901643992c&sid=xcb')
        time.sleep(4)
        scroll = 0
        cont = 0
        maximofollow = 0
        conectar = driver.find_elements_by_id("//button[@id='ember61']")
        for CN in conectar:
            if maximofollow < intSeguir:
                self.driver.execute_script('arguments[0].click();',CN)
                time.sleep(3)
                add = driver.find_elements_by_id("//button[@id='ember196']")
                self.driver.execute_script('arguments[0].click();', add)
                time.sleep(3)
                text_element = driver.find_elements_by_id("//textarea[@name='message']")
                text_element.clear()
                text_element.send_keys(self.text)
                text_element.clear()

                maximofollow += 1


class telapython:
    def __init__(self):
        # layout
        sg.theme('Reddit')
        layout = [
            [sg.Text('EMAIL:'), sg.Input(key='usuario', size=(20, 1)),
             sg.Text('SENHA:'), sg.Input(key='senha', password_char='*', size=(20, 1))],
            [sg.Text('SEGUIR 1 a 100: '), sg.Input(key='seguir', size=(10, 1))],
            [sg.Text('TEXTO PARA RECRUTADOR: '), sg.Input(key='text', size=(300, 2))],
            [sg.Button('Entrar', size=(10, 1)),
             sg.Button('Sair', size=(10, 1))],
        ]
        # Janela
        janela = sg.Window('LOGIN LINKEDIN', layout)
        self.events, self.values = janela.read()
        # ler eventos
        self.iniciar()

    def iniciar(self):
        while True:
            usuario = self.values['usuario']
            password = self.values['senha']
            text = self.values['text']
            seguir = self.values['seguir']
            intSeguir = int(seguir)
            if self.events == sg.WINDOW_CLOSED:
                break
            if self.events == 'Entrar':
                freudBot = LinkedinBot(usuario, password, text)
                freudBot.login(intSeguir)
                break
            if self.events == 'Sair':
                break

    def fim(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Você conseguiu se conectar com sucesso!!')],
            [sg.Button('SAIR', size=(10, 1))]
        ]
        janela = sg.Window('LOGIN LINKEDIN', layout)
        self.events, self.values = janela.read()
        while True:
            if self.events == 'Sair' or sg.WINDOW_CLOSED:
                break


window = telapython()
window.fim()