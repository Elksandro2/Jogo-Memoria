from tkinter import *

root = Tk()
root.title("JOGO DA MEMÓRIA")
root.geometry("750x850")
root.minsize(750, 850)
root.maxsize(750, 850)

root.configure(background="#282828")

botao1 = None
botao2 = None

# Variável criada para detectar quando todas as cartas estiverem viradas
contagem = 0

def botaoClick(carta, button):
    global botao1, botao2, contagem

    if botao1 is None:
        botao1 = (carta, button)
        # Primeira carta sempre ficará visivel
        botao1[1].configure(bg="#a69a81")
    elif botao2 is None:
        botao2 = (carta, button)
        if botao1[0] == botao2[0]:
            # Cada par de cartas achadas, será contabilizado 1 par, até chegar no total que é 9
            contagem += 1
            # Se os caracteres forem iguais, mantenha os botões pressionados
            botao1[1].configure(bg="#a69a81")
            botao2[1].configure(bg="#a69a81")
            # Deixará os botões sem funcionalidade depois de achar o par correspondente
            botao1[1].configure(state=DISABLED)
            botao2[1].configure(state=DISABLED)
            # 18 cartas = 9 pares, a pessoa ganhará depois de descobrir todas
            if contagem == 9:
                mensagem_vitoria.config(text="PARABÉNS, VOCÊ VENCEU!")
        else:
            # Caso a segunda carta não seja igual a primeira, desvira a primeira
            botao1[1].configure(bg="#604848")
        # Limpa as variáveis para a próxima jogada
        botao1 = None
        botao2 = None



# Primeira linha
carta1 = Button(
    root,
    text="A",
    padx=40,
    pady=40,
    command=lambda: botaoClick("A", carta1),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta1.grid(row=0, column=1, padx=10, pady=10)

carta2 = Button(
    root,
    text="J",
    padx=40,
    pady=40,
    command=lambda: botaoClick("J", carta2),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta2.grid(row=0, column=2, padx=10, pady=10)

carta3 = Button(
    root,
    text="C",
    padx=40,
    pady=40,
    command=lambda: botaoClick("C", carta3),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta3.grid(row=0, column=3, padx=10, pady=10)

carta4 = Button(
    root,
    text="C",
    padx=40,
    pady=40,
    command=lambda: botaoClick("C", carta4),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta4.grid(row=0, column=4, padx=10, pady=10)

carta5 = Button(
    root,
    text="M",
    padx=40,
    pady=40,
    command=lambda: botaoClick("M", carta5),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta5.grid(row=0, column=5, padx=10, pady=10)

carta6 = Button(
    root,
    text="N",
    padx=40,
    pady=40,
    command=lambda: botaoClick("N", carta6),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta6.grid(row=0, column=6, padx=10, pady=10)

# Segunda linha
carta7 = Button(
    root,
    text="B",
    padx=40,
    pady=40,
    command=lambda: botaoClick("B", carta7),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta7.grid(row=1, column=1, padx=10, pady=10)

carta8 = Button(
    root,
    text="M",
    padx=40,
    pady=40,
    command=lambda: botaoClick("M", carta8),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta8.grid(row=1, column=2, padx=10, pady=10)

carta9 = Button(
    root,
    text="O",
    padx=40,
    pady=40,
    command=lambda: botaoClick("O", carta9),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta9.grid(row=1, column=3, padx=10, pady=10)

carta10 = Button(
    root,
    text="J",
    padx=40,
    pady=40,
    command=lambda: botaoClick("J", carta10),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta10.grid(row=1, column=4, padx=10, pady=10)

carta11 = Button(
    root,
    text="K",
    padx=40,
    pady=40,
    command=lambda: botaoClick("K", carta11),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta11.grid(row=1, column=5, padx=10, pady=10)

carta12 = Button(
    root,
    text="O",
    padx=40,
    pady=40,
    command=lambda: botaoClick("O", carta12),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta12.grid(row=1, column=6, padx=10, pady=10)

# Terceira linha
carta13 = Button(
    root,
    text="A",
    padx=40,
    pady=40,
    command=lambda: botaoClick("A", carta13),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta13.grid(row=2, column=1, padx=10, pady=10)

carta14 = Button(
    root,
    text="S",
    padx=40,
    pady=40,
    command=lambda: botaoClick("S", carta14),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta14.grid(row=2, column=2, padx=10, pady=10)

carta15 = Button(
    root,
    text="K",
    padx=40,
    pady=40,
    command=lambda: botaoClick("K", carta15),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta15.grid(row=2, column=3, padx=10, pady=10)

carta16 = Button(
    root,
    text="N",
    padx=40,
    pady=40,
    command=lambda: botaoClick("N", carta16),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta16.grid(row=2, column=4, padx=10, pady=10)

carta17 = Button(
    root,
    text="S",
    padx=40,
    pady=40,
    command=lambda: botaoClick("S", carta17),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta17.grid(row=2, column=5, padx=10, pady=10)

carta18 = Button(
    root,
    text="B",
    padx=40,
    pady=40,
    command=lambda: botaoClick("B", carta18),
    fg="#604848",
    activeforeground="#604848",
    bg="#604848",
    activebackground="#a69a81",
    relief=FLAT,
    font=("Arial", 12, "bold")
)
carta18.grid(row=2, column=6, padx=10, pady=10)

# Label referente ao texto de vitória do jogador
mensagem_vitoria = Label(
    root,
    text="",
    font=("Arial", 30, "bold"),
    bg="#282828",
    fg="#a69a81"
)
mensagem_vitoria.place(relx=0.5, rely=0.5, anchor=CENTER)  # Posiciona a label ao meio

root.mainloop()