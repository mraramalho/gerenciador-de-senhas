from tkinter import (Tk, 
                     Canvas, 
                     PhotoImage, 
                     Label, 
                     Entry, 
                     Button)

from backend import Password

if __name__ == '__main__':
    BG_COLOR : str = '#28DF99'
    FONT :str = 'Open Sans'
    
    ps = Password('arquivos-json\senhas.json')
    
    window = Tk()
    window.title('Gerenciador de Senhas')
    window.config(bg=BG_COLOR, padx=70, pady=70)
    window.iconbitmap(r'images\favicon.ico')

    canvas = Canvas(width=400, height=400, bg=BG_COLOR, highlightthickness=0)
    image = PhotoImage(file='images\logo2.png')
    canvas.create_image(240, 170, image=image)
    canvas.grid(column=0, row=0, columnspan=2)

    lb_website = Label(text='Website: ')
    lb_website.config(fg='white', font=(FONT, 15, 'bold', 'italic'), bg=BG_COLOR)
    lb_website.grid(column=0, row=1)

    ps.website = Entry(show=None, font=(FONT, 10, 'italic'), highlightthickness=0, width=49)
    ps.website.grid(column=1, row=1)
    ps.website.focus()

    lb_user = Label(text='Email/Usuário: ')
    lb_user.config(fg='white', font=(FONT, 15, 'bold', 'italic'), bg=BG_COLOR)
    lb_user.grid(column=0, row=2)

    ps.user = Entry(show=None, font=(FONT, 10, 'italic'), highlightthickness=0, width=60)
    ps.user.grid(column=1, row=2, columnspan=2)
    ps.user.insert(0, '')

    lb_senha = Label(text='Senha: ')
    lb_senha.config(fg='white', font=(FONT, 15, 'bold', 'italic'), bg=BG_COLOR)
    lb_senha.grid(column=0, row=3)

    ps.senha = Entry(show=None, font=(FONT, 10, 'italic'), highlightthickness=0, width=49)
    ps.senha.grid(column=1, row=3)

    pwd_generator = Button(bg='white', text='Gerar Senha', width=9, command=ps.generate_password)
    pwd_generator.grid(column=2, row=3)

    add_password = Button(text='Adicionar Senha', width=60, command=ps.add_password)
    add_password.grid(row=4, column=1, columnspan=2)

    search_password = Button(bg='white', width=9, text='Buscar', command=ps.search_password)
    search_password.grid(column=2, row=1)

    window.mainloop()
