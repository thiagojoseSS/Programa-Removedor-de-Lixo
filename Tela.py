import os
import tkinter as tk
from tkinter import filedialog
import zipfile


pastaRoot = ""

listDef = ["_confirmOp.xml", "_mdfAtz.xml", "_canc.xml", "_cteAtz.xml", "_cteCanc.xml", "_cc.xml", "_ciencOp.xml",
           "_RegPassag.xml", "_mdfCanc.xml", "_OpNRealiz.xml", "_descOp.xml", "_1.xml", "_2.xml"]

listRem = ["_confirmOp.xml", "_mdfAtz.xml", "_canc.xml", "_cteAtz.xml", "_cteCanc.xml", "_cc.xml", "_ciencOp.xml",
           "_RegPassag.xml", "_mdfCanc.xml", "_OpNRealiz.xml", "_descOp.xml", "_1.xml", "_2.xml"]

listNew = []

numeroDeArqRemovidos = 0
numeroDeArqLidos = 0


def tratamentoArq(caminho):
    pastas(caminho)


def pastas(caminho):
    global numeroDeArqRemovidos, numeroDeArqLidos, pastaRoot

    for cam, pastas, arq in os.walk(caminho):
        arquivosAtual = os.listdir(caminho)
        for arqk in arquivosAtual[:]:
            if arqk.endswith('.xml'):
                numeroDeArqLidos += 1
        
        for esteArq in arq:
            for aSeExcluido in listRem[:]:
                if esteArq.find(aSeExcluido) >= 0:  # Pode ser colocado 44 no logar de 0, pois é o tamanha da Chave.
                    rotaR = cam + "/" + esteArq
                    numeroDeArqRemovidos += 1
                    os.remove(rotaR)
                
        for pasta in pastas[:]:
            rota = cam + "/" + pasta
            tratamentoArq(rota)


def selecion():
    global pastaRoot
    init = os.path.expanduser("~/Documents")
    pastaRoot = filedialog.askdirectory(initialdir=init)
    tx1.config(text=pastaRoot)


def excluir():
    global pastaRoot, numeroDeArqRemovidos, numeroDeArqLidos

    tratarChecks()
    if pastaRoot != "":
        tratamentoArq(pastaRoot)
        textoResposta = "Arquivo(s) Lido(s)!\t\t" + str(numeroDeArqLidos)
        lResultado = tk.Label(janela, text=textoResposta, fg="darkgreen", justify=tk.LEFT).place(x=200, y=210)
        textoResposta2 = "Arquivo(s) Removido(s)!\t" + str(numeroDeArqRemovidos)
        lResultado2 = tk.Label(janela, text=textoResposta2, fg="red", justify=tk.LEFT).place(x=200, y=230)
        dif = "Arquivo(s) Restante(s)!\t" + str(int(numeroDeArqLidos-numeroDeArqRemovidos))
        lDif = tk.Label(janela, text=dif, fg="darkblue", justify=tk.LEFT).place(x=200, y=250)
        numeroDeArqLidos = 0
        numeroDeArqRemovidos = 0


def tratarChecks():
    global listNew, listDef

    listNew.clear()
    
    if cVar1.get() == 0 or cVar2.get() == 0 or cVar3.get() == 0 or cVar4.get() == 0 or cVar5.get() == 0 or \
        cVar6.get() == 0 or cVar7.get() == 0 or cVar8.get() == 0 or cVar9.get() == 0 or cVar10.get() == 0 or \
            cVar11.get() == 0 or cVar12.get() == 0:

        if cVar1.get() == 1:
            listNew.append(listDef[0])

        if cVar2.get() == 1:
            listNew.append(listDef[1])

        if cVar3.get() == 1:
            listNew.append(listDef[2])

        if cVar4.get() == 1:
            listNew.append(listDef[3])

        if cVar5.get() == 1:
            listNew.append(listDef[4])

        if cVar6.get() == 1:
            listNew.append(listDef[5])

        if cVar7.get() == 1:
            listNew.append(listDef[6])

        if cVar8.get() == 1:
            listNew.append(listDef[7])

        if cVar9.get() == 1:
            listNew.append(listDef[8])

        if cVar10.get() == 1:
            listNew.append(listDef[9])

        if cVar11.get() == 1:
            listNew.append(listDef[10])

        if cVar12.get() == 1:
            listNew.append(listDef[11])
            listNew.append(listDef[12])

        listRem.clear()
        i = 0
        while i <= len(listNew) - 1:
            listRem.append(listNew[i])
            i += 1


# def descompactar(caminho):
#
#     for cam, past, arq in os.walk(caminho):
#         pass
#
#     filess = os.listdir(caminho)
#
#     extrairZips()
#
#
# def extrairZips(caminho, pasta):
#     novaPasta = caminho + "/" + pasta + ".zip"
#     aquiExtrair = zipfile.ZipFile(novaPasta, 'w')
#
#
# def testes(caminho=None):
#     global pastaRoot
#
#     newZip = pastaRoot if caminho is None else caminho
#     newZip = newZip + '.rar'
#     fantasy_zip = zipfile.ZipFile(newZip, 'w')
#
#     for folder, subfolders, files in os.walk(pastaRoot):
#
#         for file in files:
#             if file.endswith('.xml'):
#                 fantasy_zip.write(os.path.join(folder, file),
#                                   os.path.relpath(os.path.join(folder, file), pastaRoot),
#                                   compress_type=zipfile.ZIP_DEFLATED)
#
#     fantasy_zip.close()


janela = tk.Tk()
janela.geometry("500x300")
janela.resizable(0, 0)

janela.title("Gerador de Arquivos")

lb0 = tk.Label(janela, text="Remover Arquivos XML Desnecessários da Sefaz-PE")
lb0.place(x=30, y=10)
lb0["font"] = "Arial 10 bold"
lb0["foreground"] = "green"

lb1 = tk.Label(janela, text="Tipo de XMLs:")
lb1.place(x=30, y=30)

cVar1 = tk.IntVar()
cVar2 = tk.IntVar()
cVar3 = tk.IntVar()
cVar4 = tk.IntVar()
cVar5 = tk.IntVar()
cVar6 = tk.IntVar()
cVar7 = tk.IntVar()
cVar8 = tk.IntVar()
cVar9 = tk.IntVar()
cVar10 = tk.IntVar()
cVar11 = tk.IntVar()
cVar12 = tk.IntVar()

cBut1 = tk.Checkbutton(janela, text="_confirmOp.xml", variable=cVar1, onvalue=1, offvalue=0)
cBut1.place(x=30, y=50)
cBut1.select()

cBut2 = tk.Checkbutton(janela, text="_mdfAtz.xml", onvalue=1, offvalue=0, variable=cVar2)
cBut2.place(x=30, y=70)
cBut2.select()

cBut3 = tk.Checkbutton(janela, text="_canc.xml", onvalue=1, offvalue=0, variable=cVar3)
cBut3.place(x=30, y=90)
cBut3.select()

cBut4 = tk.Checkbutton(janela, text="_cteAtz.xml", onvalue=1, offvalue=0, variable=cVar4)
cBut4.place(x=30, y=110)
cBut4.select()

cBut5 = tk.Checkbutton(janela, text="_cteCanc.xml", onvalue=1, offvalue=0, variable=cVar5)
cBut5.place(x=30, y=130)
cBut5.select()

cBut6 = tk.Checkbutton(janela, text="_cc.xml", onvalue=1, offvalue=0, variable=cVar6)
cBut6.place(x=30, y=150)
cBut6.select()

cBut7 = tk.Checkbutton(janela, text="_ciencOp.xml", onvalue=1, offvalue=0, variable=cVar7)
cBut7.place(x=30, y=170)
cBut7.select()

cBut8 = tk.Checkbutton(janela, text="_RegPassag.xml", onvalue=1, offvalue=0, variable=cVar8)
cBut8.place(x=30, y=190)
cBut8.select()

cBut9 = tk.Checkbutton(janela, text="_mdfCanc.xml", onvalue=1, offvalue=0, variable=cVar9)
cBut9.place(x=30, y=210)
cBut9.select()

cBut10 = tk.Checkbutton(janela, text="_OpNRealiz.xml", onvalue=1, offvalue=0, variable=cVar10)
cBut10.place(x=30, y=230)
cBut10.select()

cBut11 = tk.Checkbutton(janela, text="_descOp.xml", onvalue=1, offvalue=0, variable=cVar11)
cBut11.place(x=30, y=250)
cBut11.select()

cBut12 = tk.Checkbutton(janela, text="_{n}.xml", onvalue=1, offvalue=0, variable=cVar12)
cBut12.place(x=30, y=270)
cBut12.select()



bt1 = tk.Button(janela, width=30, text="Selecionar Pasta Raiz:", command=selecion)
bt1.place(x=200, y=45)

tx1 = tk.Label(janela, width=33, text="teste", fg="blue")
tx1.place(x=200, y=75)


bt2 = tk.Button(janela, width=15, text="Excluir Arquivos!", command=excluir)
bt2.place(x=200, y=100)
bt2["background"] = "skyblue"


janela.mainloop()
