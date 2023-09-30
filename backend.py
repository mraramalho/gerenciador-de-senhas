from random import *
from tkinter import messagebox, Entry, END
import json as js
import pyperclip


class Password:
    def __init__(self, password_path:str) -> None:
        self.website:Entry = None
        self.senha:Entry = None
        self.user:Entry = None
        self.password_path = password_path
        
    def check_website_name(self, file_name:str, website_name: str) -> str:
        try:
            with open(file_name, 'r') as data_file:
                data = js.load(data_file)
        except FileNotFoundError:
            pass
        else:
            try:
                website_name = data[website_name.title()]
                return website_name
            except KeyError:
                return None


    def update_password_file(self, file_name: str, new_data):
        try:
            with open(file_name, 'r') as file:
                data = js.load(file)
        except FileNotFoundError:
            with open(file_name, 'w') as file:
                js.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file_name, 'w') as file:
                js.dump(data, file, indent=4)
        finally:
            self.website.delete(0, END)
            self.senha.delete(0, END)
            messagebox.showinfo('Senha', 'Senha registrada com sucesso!')


    def add_password(self):
        website_name = self.website.get().title()
        user_name = self.user.get()
        senha_criada = self.senha.get()
        new_data = {
            website_name.title(): {
                'user_name': user_name,
                'senha_criada': senha_criada,
            }
        }
        if website_name == '' or user_name == '' or senha_criada == '':
            messagebox.showerror("Campos Vazios", "Todos os campos devem estar preenchido!")
        elif len(senha_criada) < 8:
            messagebox.showerror("Padrão de Senha Incorreto", "Senha escolhida possui menos de 8 dígitos!")
        else:
            is_ok = messagebox.askokcancel(title=website_name,
                                        message=f'Estes são os dados digitados:\nWebsite: {website_name}'
                                                f'\nEmail: {user_name}\nSenha: {senha_criada}')
            if is_ok:
                if self.check_website_name(self.password_path, website_name=website_name) is not None:
                    atualizar_senha = messagebox.askokcancel(title='Website Cadastrado', message=f'{website_name} '
                                                                                                f'já possui senha '
                                                                                                f'cadastrada, '
                                                                                                f'deseja continuar '
                                                                                                f'mesmo assim? '
                                                                                                f'Para atualizar a'
                                                                                                f' senha pressione OK.')
                    if atualizar_senha:
                        self.update_password_file(self.password_path, new_data=new_data)

                    else:
                        self.website.delete(0, END)
                        self.senha.delete(0, END)
                        messagebox.showinfo('Website possui senha cadastrada.', 'O Website digitado já possui senha '
                                                                                'cadastrada e você esconheu não cadastrar '
                                                                                'nova senha.'
                                                                                '\nObrigado!!')
                else:
                    self.update_password_file(self.password_path, new_data=new_data)


    def generate_password(self):
        self.senha.delete(0, END)

        numero_letras = randint(4, 8)
        numero_letras_maiusculas = randint(2, 4)
        numero_simbolos = randint(2, 4)
        numero_numeros = randint(2, 4)

        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
        letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numero = [str(numero) for numero in range(0, 10)]
        simbolos = ['!', "@", "#", "$", "%", "&", "*", "(", ")", "{", "}", "[", "]", "?"]

        letras_escolhidas = [choice(letras) for _ in range(numero_letras)]
        letras_maiusculas_escolhidas = [choice(letras_maiusculas) for _ in range(numero_letras_maiusculas)]
        numeros_escolhidos = [choice(numero) for _ in range(numero_numeros)]
        simbolos_escolhidos = [choice(simbolos) for _ in range(numero_simbolos)]

        senha_gerada = letras_escolhidas + letras_maiusculas_escolhidas + numeros_escolhidos + simbolos_escolhidos
        shuffle(senha_gerada)
        senha_gerada = ''.join(senha_gerada)

        self.senha.insert(0, senha_gerada)
        pyperclip.copy(senha_gerada)


    def search_password(self):
        website_name = self.website.get().title()
        try:
            with open(self.password_path, 'r') as file:
                senhas = js.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title='Resultado de Busca', message=f'Nenhum resultado encontrado. Cadastre uma senha!')
        else:
            try:
                dados = senhas[website_name]
            except KeyError:
                messagebox.showinfo(title='Resultado de Busca', message=f'Não existe senha cadastrada '
                                                                        f'para o site: {website_name}')
            else:
                messagebox.showinfo(title='Resultado de Busca', message=f'Website: {website_name}\n'
                                                                        f'E-mail\\Usuário: {dados["user_name"]}\n'
                                                                        f'Senha: {dados["senha_criada"]}\n\n'
                                                                        f'Senha copiada com sucesso! Use \'ctr+v\' '
                                                                        f'para cola-la no local desejado.')
                pyperclip.copy(dados['senha_criada'])

            finally:
                self.website.delete(0, END)
                self.senha.delete(0, END)