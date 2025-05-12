import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from utils.leitor import ler_cnpjs
from utils.consulta import consultar_cnpj
from utils.escritor import salvar_resultados
from time import sleep
import os
import threading

def iniciar_interface():
    def selecionar_arquivo():
        caminho = filedialog.askopenfilename(
            title="Selecione a planilha com os CNPJs",
            filetypes=[("Planilhas Excel", "*.xlsx")]
        )
        if not caminho:
            return

        # Inicia o processo em uma nova thread
        thread = threading.Thread(target=processar_planilha, args=(caminho,))
        thread.start()

    def processar_planilha(caminho):
        try:
            registros = ler_cnpjs(caminho)
            total = len(registros)

            if total == 0:
                messagebox.showwarning("Aviso", "Nenhum CNPJ encontrado na planilha.")
                return

            resultados = []
            for i, registro in enumerate(registros, 1):
                cnpj = registro['CNPJ']
                codigo = registro['Código']

                resultado = consultar_cnpj(cnpj)
                resultado['Código'] = codigo
                resultados.append(resultado)

                if i % 5 == 0 or i == total:
                    progress_bar["value"] = i
                    progress_label.config(text=f"Consultando {i}/{total}")
                    janela.update_idletasks()

                sleep(0.6)

            caminho_salvo = salvar_resultados(resultados)

            if caminho_salvo and os.path.exists(caminho_salvo):
                progress_label.config(text="Finalizado.")
            else:
                progress_label.config(text="Arquivo não foi salvo.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante o processamento:\n{e}")
            progress_label.config(text="Erro no processo.")

    # Interface
    janela = tk.Tk()
    janela.title("Consulta de CNPJs")
    janela.geometry("400x250")
    janela.resizable(False, False)

    label = tk.Label(janela, text="Clique no botão abaixo para carregar a planilha:", font=("Arial", 12))
    label.pack(pady=20)

    botao = tk.Button(janela, text="Selecionar Planilha", font=("Arial", 12, "bold"),
                      bg="#004488", fg="white", command=selecionar_arquivo, cursor="hand2")
    botao.pack(pady=10)

    progress_label = tk.Label(janela, text="", font=("Arial", 10))
    progress_label.pack(pady=5)

    progress_bar = ttk.Progressbar(janela, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    janela.mainloop()
