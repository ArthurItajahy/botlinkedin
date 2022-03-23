from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


class LinkedinBot:
    def __init__(self, username, password, text, pesquisa):
        self.lokingfor = pesquisa
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
        search_element = driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/input")
        search_element.clear()
        search_element.send_keys(self.lokingfor)
        time.sleep(4)
        search_element.send_keys(Keys.RETURN)
        time.sleep(5)
        people_element = driver.find_element_by_xpath("//button[contains(.,'Pessoas')]")
        self.driver.execute_script('arguments[0].click();', people_element)
        time.sleep(5)
        maximofollow = 0
        while maximofollow < intSeguir:
            conectar = driver.find_elements_by_xpath("//button[contains(.,'Conectar')]")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if len(conectar) > 1:
                for CN in conectar:
                    if maximofollow >= intSeguir:
                        break
                    self.driver.execute_script('arguments[0].click();',CN)
                    time.sleep(3)
                    add = driver.find_element_by_xpath("//button[contains(.,'Adicionar nota')]")
                    self.driver.execute_script('arguments[0].click();', add)
                    time.sleep(3)
                    text_element = driver.find_element_by_css_selector('#custom-message')
                    text_element.clear()
                    text_element.send_keys(self.text)
                    time.sleep(3)
                    enviarText_element = driver.find_element_by_xpath("//button[contains(.,'Enviar')]")
                    self.driver.execute_script('arguments[0].click();', enviarText_element)
                    maximofollow += 1
            else:
                time.sleep(7)
                labels_element = driver.find_element_by_xpath("//button[contains(.,'Avançar')]")
                self.driver.execute_script('arguments[0].click();', labels_element)
                time.sleep(5)
        driver.quit()

class telapython:
    def __init__(self):
        # layout
        sg.theme('Black')
        layout = [
            [sg.Text('EMAIL:'), sg.Input(key='usuario', size=(20, 1)),
             sg.Text('SENHA:'), sg.Input(key='senha', password_char='*', size=(20, 1))],
            [sg.Text('SEGUIR 1 a 100: '), sg.Input(key='seguir', size=(10, 1))],
            [sg.Text('PESQUISAR POR: '), sg.Input(key='pesquisa', size=(10, 2))
            ,sg.Text('TEXTO PARA O PESQUISADO: '), sg.Input(key='text', size=(20, 2))],
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
            pesquisa = self.values['pesquisa']
            text = self.values['text']
            seguir = self.values['seguir']
            intSeguir = int(seguir)
            if self.events == sg.WINDOW_CLOSED:
                break
            if self.events == 'Entrar':
                freudBot = LinkedinBot(usuario, password, text,pesquisa)
                freudBot.login(intSeguir)
                break
            if self.events == 'Sair':
                break

    def fim(self):
        sg.theme('Black')
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
