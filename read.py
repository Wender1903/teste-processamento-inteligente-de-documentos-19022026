# Desenvolva aqui sua atividade

import pdfplumber as pdftool
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


class FaturaCPFL:
    def __init__(self, file_path):
        self.file_path = file_path
        self.texto = ""
        self.dados_lidos = {}

    def ler_pdf(self):
        textos_paginas = []
        with pdftool.open(self.file_path) as pdf:
            for pagina in pdf.pages:
                dados_pag = pagina.extract_text()
                if dados_pag:
                    textos_paginas.append(dados_pag)
        self.texto = "\n".join(textos_paginas)
        self.texto = self.texto.split("\n")

    def extrair_dados(self):
        texto = self.texto

        # Inicializar todas as variáveis para evitar erros
        nome_cpf = endereco = classificacao = instalacao = valor_distribuidora = mes_vencimento = mes_pagamento = valor_tributo = consumo_kwh = saldo_kwh = linha_digitavel_pagamento = None
        tusd = te = total_aneel = 0.0
        soma_energia_injetada = 0

        for i, t in enumerate(texto):

            # Titular e CPF
            if "CPF:" in t:
                nome_cpf = t

            # Endereço e classificação
            if "CLASSIFICAÇÃO" in t:
                endereco, classificacao = t.split("CLASSIFICAÇÃO: ", 1)
                endereco = endereco.strip()
                classificacao = classificacao.strip()

            # Dados de instalação
            if "INSTALAÇÃO" in t:
                dados_conta = t.split("INSTALAÇÃO")[1]
                dados = dados_conta.split()
                mes_pagamento = dados[0]
                mes_vencimento = dados[1]
                valor_tributo = float(dados[2].replace(",", "."))

            # Número da instalação
            if ".com.br" in t:
                if t.split()[1].isdigit():
                    instalacao = int(t.split()[1])

            # Valor distribuidora
            if "Total Distribuidora" in t:
                dados = t.split()
                valor_distribuidora = float(dados[-1].replace(",", "."))
                print("Valor para a distribuidora:", valor_distribuidora)

            # Tarifa total Aneel
            if "Consumo kWh" in t:
                dados = t.split('kWh')[1]
                tusd = float(dados.split()[0].replace(',', '.'))
                te = float(dados.split()[1].replace(',', '.'))
                total_aneel = tusd + te
                print(total_aneel)

            # Quantidade em kWh do Consumo da fatura
            if "2023 OUT" in t:
                print(i, t)
                consumo_kwh = t.split()[3]

            # Saldo em kWh acumulado na Instalação
            if "Instalação" in t:
                saldo_kwh = t.split()[-2]

            # Somatório das quantidades das energias compensadas (injetadas)
            if "Energ Atv Inj. oUC mPT" in t:
                dados = t.split()
                for num, dado in enumerate(dados):
                    if num == 8:
                        print(dado)
                        soma_energia_injetada += float(dado.replace('.', '').replace(',', '.'))

            # Contribuição de iluminação Pública
            if "Contrib. Custeio IP-CIP Municipal" in t:
                contribuicao_iluminacao_publica = t.split()[-1]


            # Linha digitável para pagamento
            if "Autenticação Mecânica" in t:
                linha_digitavel_pagamento = t.split("Autenticação Mecânica")[0]

        self.dados_lidos = {
            "Titular da Fatura e Documento": nome_cpf,
            "Endereço": endereco,
            "Classificação": classificacao,
            "Número de Instalação": instalacao,
            "Valor a Pagar para a distribuidora": valor_distribuidora,
            "Vencimento": mes_vencimento,
            "Mês da Fatura": mes_pagamento,
            "Tarifa total com tributos": valor_tributo,
            "Tarifa total Aneel": total_aneel,
            "Quantidade em kWh do Consumo da fatura": consumo_kwh,
            "Saldo em kWh acumulado na Instalação": saldo_kwh,
            "Somatório das quantidades das energias compensadas (injetadas)": soma_energia_injetada,
            "Somatório dos Valores Totais das Operações R$": None,
            "Contribuição de iluminação Pública": contribuicao_iluminacao_publica,
            "Alíquotas do ICMS, PIS e COFINS em %": None,
            "Linha digitável para pagamento": linha_digitavel_pagamento
        }

    def processar(self):
        self.ler_pdf()
        self.extrair_dados()
        return self.dados_lidos

    def exibir_dados(self):
        print("\n===== DADOS DA FATURA =====\n")
        for chave, valor in self.dados_lidos.items():
            if isinstance(valor, dict):
                print(f"{chave}:")
                for subchave, subvalor in valor.items():
                    print(f"  {subchave}: {subvalor}")
            else:
                print(f"{chave}: {valor}")
        print("\n===========================\n")


    def gerar_pdf_organizado(self, nome_pdf="fatura_organizada.pdf"):
        doc = SimpleDocTemplate(nome_pdf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm)
        elementos = []
        estilos = getSampleStyleSheet()
        estilo_titulo = estilos['Title']
        estilo_normal = estilos['Normal']
        estilo_subtitulo = estilos['Heading2']

        elementos.append(Paragraph("Fatura CPFL - Dados Organizados", estilo_titulo))
        elementos.append(Spacer(1, 12))

        for chave, valor in self.dados_lidos.items():
            if valor is None:
                valor = "None"
            texto = f"<b>{chave}:</b> {valor}"
            elementos.append(Paragraph(texto, estilo_normal))
            elementos.append(Spacer(1, 6))  

        elementos.append(Spacer(1, 10))
        elementos.append(Paragraph(
            "Obs: os valores 'None' é porque não consegui realizar a busca.",
            estilo_subtitulo
        ))

        doc.build(elementos)
        print(f"PDF organizado gerado com sucesso: {nome_pdf}")


fatura = FaturaCPFL("fatura_cpfl.pdf")
resultado = fatura.processar()
fatura.exibir_dados()
fatura.gerar_pdf_organizado("fatura_cpfl_organizada.pdf")