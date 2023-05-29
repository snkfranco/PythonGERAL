import tkinter as tk
from tkinter import scrolledtext
import openai

# Cria a janela
janela = tk.Tk()
janela.title("Private Chat")

# Cria o frame com a entrada de texto
frame_entrada = tk.Frame(janela)
frame_entrada.pack(side=tk.TOP)

label_entrada = tk.Label(frame_entrada, text="Digite algo:")
label_entrada.pack(side=tk.LEFT)

entrada_texto = tk.Entry(frame_entrada, width=80)
entrada_texto.pack(side=tk.LEFT)

# Cria a saída rolável
saida_texto = scrolledtext.ScrolledText(janela, width=80, height=10)
saida_texto.pack(side=tk.TOP)

# Define uma função para ser executada quando o botão for pressionado
def exibir_texto():
    
    openai.api_key = "sua api key"

    model_engine = "text-davinci-003"
    prompt = entrada_texto.get()

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=0.4,
    )


    response = completion.choices[0].text
    saida_texto.insert(tk.END, 'Você: ' + prompt + '\n')
    saida_texto.insert(tk.END, '\n' + response + "\n\n")
    entrada_texto.delete(0, tk.END)

# Cria o botão
botao = tk.Button(janela, text="Exibir", command=exibir_texto)
botao.pack(side=tk.BOTTOM)

# Inicia a janela
janela.mainloop()
