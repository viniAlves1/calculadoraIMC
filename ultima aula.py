import tkinter as tk

def calculo():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    resultado = peso / (altura ** 2)

    if resultado < 16.9:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você está muito abaixo do peso'''
    elif 17 <= resultado < 18.4:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você está abaixo do peso'''
    elif 18.5 <= resultado < 24.9:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Seu peso é normal''' 
    elif 25 <= resultado < 29.9:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você está acima do peso'''
    elif 30 <= resultado < 34.9:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você tem obesidade grau I'''
    elif 35 <= resultado < 40:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você tem obesidade grau II'''
    elif resultado >= 40:
        resultado_label['text'] = f'''Seu IMC é: {resultado}.
Você tem obesidade grau III'''



root = tk.Tk()
root.title('Calculadora IMC')
root.geometry('500x500')

peso_label = tk.Label(root, text= 'Digite seu peso:')
peso_label.pack()

peso_entry = tk.Entry(root)
peso_entry.pack()

altura_label = tk.Label(root, text= 'Digite sua altura:')
altura_label.pack()

altura_entry = tk.Entry(root)
altura_entry.pack()

btn_calcular = tk.Button(root, text= 'Calcular', command= calculo)
btn_calcular.pack()

resultado_label = tk.Label(root, text='')
resultado_label.pack()


root.mainloop()