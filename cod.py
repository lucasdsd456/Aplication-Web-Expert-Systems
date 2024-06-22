import streamlit as st

base_conhecimento_jogadores = [
("portugal", "al_nassr", "arabia_saudita", "atacante", 38, "cristiano_ronaldo", 100000000, 1.87, 83, 3, 1, 2, "Finalização, Cabeceio, Pênaltis", "Liderança, Disciplina, Determinação"),
("argentina", "inter_miami", "estados_unidos", "atacante", 36, "lionel_messi", 120000000, 1.70, 72, 2, 0, 1, "Finalização, Dribles, Visão de jogo, Precisão nos passes", "Liderança, Trabalho em equipe, Humildade"),
("brasil", "al_hilal", "arabia_saudita", "atacante", 31, "neymar_jr", 150000000, 1.75, 68, 4, 1, 3, "Dribles, Criatividade no ataque", "Determinação, Confiança, Carisma"),
("franca", "psg", "franca", "atacante", 24, "kylian_mbappe", 180000000, 1.78, 73, 1, 0, 1, "Finalização, Velocidade", "Ambição, Mentalidade vencedora"),
("portugal", "barcelona", "espanha", "atacante", 23, "joao_felix", 90000000, 1.81, 70, 2, 0, 2, "Controle de bola", "Determinação"),
("belgica", "manchester_city", "inglaterra", "atacante", 32, "kevin_de_bruyne", 100000000, 1.81, 70, 3, 0, 2, "Visão de jogo, Precisão nos passes, Chutes de longa distância", "Liderança"),
("italia", "psg", "franca", "goleiro", 24, "donnarumma", 80000000, 1.96, 90, 1, 0, 0, "Reflexos, Defesas", "Serenidade sob pressão"),
("brasil", "liverpool", "inglaterra", "goleiro", 29, "alisson_becker", 75000000, 1.93, 91, 2, 0, 1, "Habilidades de um contra um, Comando da área", "Liderança"),
("alemanha", "barcelona", "espanha", "goleiro", 30, "ter_stegen", 90000000, 1.87, 85, 1, 0, 0, "Reflexos, Distribuição", "Confiabilidade, Calma"),
("brasil", "manchester_city", "inglaterra", "goleiro", 28, "ederson_moraes", 80000000, 1.88, 90, 2, 0, 1, "Habilidades de passe longo", "Destreza"),
("espanha", "real_madrid", "espanha", "goleiro", 27, "kepa", 60000000, 1.86, 82, 3, 1, 1, "Reflexos, Distribuição", "Calma"),
("argentina", "aston_villa", "inglaterra", "goleiro", 29, "emiliano_martinez", 50000000, 1.95, 88, 2, 0, 1, "Defesas, Pênaltis, Comando da área", "Confiança"),
("holanda", "liverpool", "inglaterra", "defensor", 30, "virgil_van_dijk", 90000000, 1.93, 92, 4, 0, 1, "Marcação, Jogo aéreo", "Liderança"),
("portugal", "manchester_city", "inglaterra", "defensor", 25, "ruben_dias", 80000000, 1.87, 86, 2, 0, 2, "Defesa sólida", "Liderança"),
("franca", "manchester_united", "inglaterra", "defensor", 29, "raphael_varane", 70000000, 1.91, 80, 3, 1, 2, "Defesa sólida, Calma", "Experiência"),
("escocia", "liverpool", "inglaterra", "defensor", 28, "andrew_robertson", 60000000, 1.78, 67, 2, 0, 1, "Cruzamentos, Resistência", "Trabalho em equipe, Determinação"),
("alemanha", "bayern_de_munique", "alemanha", "defensor", 27, "joshua_kimmich", 80000000, 1.76, 73, 3, 1, 2, "Versatilidade", "Inteligência tática"),
("franca", "psg", "franca", "defensor", 26, "presnel_kimpembe", 60000000, 1.83, 82, 2, 0, 1, "Jogo aéreo, Concentração", "Determinação"),
("brasil", "arsenal", "inglaterra", "defensor", 25, "gabriel_magalhaes", 50000000, 1.91, 87, 4, 0, 1, "Marcação, Jogo aéreo", "Determinação"),
("brasil", "chelsea", "inglaterra", "defensor", 39, "thiago_silva", 20000000, 1.83, 79, 1, 0, 2, "Posicionamento", "Liderança, Experiência"),
("uruguai", "flamengo", "brasil", "meio_campista", 30, "giorgian_de_arrascaeta", 30000000, 1.80, 75, 3, 1, 3, "Criatividade no ataque", ""),
("argentina", "bayer_leverkusen", "alemanha", "meio_campista", 25, "exequiel_palacios", 40000000, 1.78, 70, 2, 0, 2, "Precisão nos passes, Controle de bola", "Trabalho em equipe"),
("espanha", "inter_miami", "estados_unidos", "meio_campista", 35, "sergio_busquets", 50000000, 1.89, 76, 1, 0, 1, "Visão de jogo, Precisão nos passes", "Liderança, Inteligência tática"),
("italia", "inter_milao", "italia", "meio_campista", 27, "nicolo_barella", 60000000, 1.72, 68, 3, 1, 2, "Resistência", "Trabalho em equipe"),
("brasil", "real_madrid", "espanha", "atacante", 23, "vinicius_junior", 150000000, 1.76, 73, 2, 0, 1, "Finalização, Dribles, Velocidade", "Confiança"),
("franca", "barcelona", "espanha", "defensor", 24, "jules_kounde", 65000000, 1.78, 70, 3, 0, 2, "Defesa sólida, Versatilidade, Concentração", ""),
("inglaterra", "bayern_de_munique", "alemanha", "atacante", 30, "harry_kane", 110000000, 1.88, 86, 2, 0, 2, "Finalização, Cabeceio", "Liderança"),
("argentina", "inter_milao", "italia", "atacante", 26, "lautaro_martinez", 70000000, 1.74, 72, 3, 1, 2, "Finalização, Controle de bola", "Trabalho em equipe, Determinação"),
("alemanha", "real_madrid", "espanha", "meio_campista", 20, "jude_bellingham", 180000000, 1.86, 75, 1, 0, 1, "Visão de jogo, Controle de bola", "Inteligência tática"),
("belgica", "real_madrid", "espanha", "meio_campista", 30, "eden_hazard", 50000000, 1.75, 74, 3, 1, 3, "Dribles, Precisão nos passes", "Confiança"),
("portugal", "liverpool", "inglaterra", "atacante", 27, "diogo_jota", 60000000, 1.78, 70, 2, 0, 1, "Finalização, Velocidade", "Trabalho em equipe"),
("espanha", "manchester_city", "inglaterra", "meio_campista", 31, "rodri", 80000000, 1.91, 82, 3, 0, 2, "Visão de jogo, Precisão nos passes", "Liderança"),
("franca", "chelsea", "inglaterra", "meio_campista", 32, "ngolo_kante", 55000000, 1.68, 70, 2, 0, 1, "Precisão nos passes, Controle de bola", "Trabalho em equipe, Determinação"),
("brasil", "real_madrid", "espanha", "atacante", 22, "rodrigo", 100000000, 1.75, 71, 1, 0, 1, "Dribles, Velocidade", "Confiança"),
("egito", "liverpool", "inglaterra", "atacante", 29, "mohamed_salah", 120000000, 1.75, 71, 2, 0, 2, "Finalização, Velocidade", "Trabalho em equipe, Determinação"),
("italia", "paris_saint_germain", "franca", "meio_campista", 30, "marco_verratti", 70000000, 1.65, 60, 2, 0, 1, "Precisão nos passes, Visão de jogo", "Trabalho em equipe, Inteligência tática"),
("espanha", "manchester_united", "inglaterra", "meio_campista", 28, "bruno_fernandes", 90000000, 1.79, 70, 3, 0, 2, "Precisão nos passes, Finalização de longe", "Liderança, Determinação"),
("alemanha", "borussia_dortmund", "alemanha", "meio_campista", 24, "julian_brandt", 50000000, 1.85, 83, 2, 0, 1, "Dribles, Precisão nos passes", "Trabalho em equipe, Determinação"),
("argentina", "sevilla", "espanha", "defensor", 25, "marcos_acuña", 45000000, 1.72, 69, 3, 0, 1, "Cruzamentos, Resistência", "Trabalho em equipe, Determinação"),
("brasil", "barcelona", "espanha", "atacante", 21, "raphinha", 60000000, 1.76, 71, 2, 0, 1, "Dribles, Finalização", "Confiança, Determinação"),
("franca", "milan", "italia", "defensor", 27, "theo_hernandez", 80000000, 1.84, 81, 4, 0, 1, "Velocidade, Cruzamentos", "Confiança, Determinação"),
("brasil", "real_madrid", "espanha", "meio_campista", 27, "casemiro", 80000000, 1.85, 84, 3, 0, 2, "Marcação, Passe longo", "Liderança, Trabalho em equipe"),
("argentina", "paris_saint_germain", "franca", "atacante", 26, "mauro_icardi", 65000000, 1.81, 75, 2, 0, 1, "Finalização, Cabeceio", "Determinação, Confiança"),
("espanha", "chelsea", "inglaterra", "defensor", 32, "cesar_azpilicueta", 20000000, 1.78, 72, 4, 0, 1, "Marcação, Cruzamentos", "Liderança, Determinação"),
("franca", "manchester_united", "inglaterra", "defensor", 26, "lucas_hernandez", 60000000, 1.82, 79, 3, 0, 1, "Marcação, Velocidade", "Confiança, Determinação"),
("italia", "juventus", "italia", "defensor", 30, "leonardo_bonucci", 30000000, 1.90, 85, 3, 0, 2, "Jogo aéreo, Posicionamento", "Experiência, Liderança"),
("argentina", "paris_saint_germain", "franca", "meio_campista", 25, "leandro_paredes", 45000000, 1.80, 75, 2, 0, 1, "Precisão nos passes, Visão de jogo", "Trabalho em equipe, Determinação"),
("alemanha", "bayern_de_munique", "alemanha", "meio_campista", 29, "leon_goretzka", 70000000, 1.89, 84, 3, 0, 2, "Marcação, Passe longo", "Trabalho em equipe, Determinação"),
("brasil", "manchester_united", "inglaterra", "defensor", 25, "alex_telles", 35000000, 1.81, 72, 2, 0, 1, "Cruzamentos, Marcação", "Trabalho em equipe, Determinação"),
("franca", "psg", "franca", "defensor", 24, "dayot_upamecano", 65000000, 1.86, 82, 3, 0, 2, "Jogo aéreo, Marcação", "Confiança, Determinação"),
("brasil", "aston_villa", "inglaterra", "meio_campista", 28, "douglas_luiz", 40000000, 1.75, 75, 2, 0, 1, "Passe longo, Marcação", "Determinação, Trabalho em equipe")
]

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def encontrar_jogador(orcamento, posicoes, idade_min, idade_max, nacionalidades, pais_clube, tecnicas, soft_skills):
    jogadores_disponiveis = []
    if "Nenhuma específica" in nacionalidades:
        nacionalidades = [jogador[0] for jogador in base_conhecimento_jogadores]
    if "Nenhuma específica" in pais_clube:
        pais_clube = [jogador[2] for jogador in base_conhecimento_jogadores]
    if "Nenhuma específica" in tecnicas:
        tecnicas = set()
        for jogador in base_conhecimento_jogadores:
            tecnicas.update(jogador[12].lower().split(", "))
    if "Nenhuma específica" in soft_skills:
        soft_skills = set()
        for jogador in base_conhecimento_jogadores:
            soft_skills.update(jogador[13].lower().split(", "))
    for jogador in base_conhecimento_jogadores:
        tecnicas_jogador = jogador[12].lower().split(", ")
        soft_skills_jogador = jogador[13].lower().split(", ")

        if (
            jogador[6] <= orcamento and
            jogador[4] >= idade_min and
            jogador[4] <= idade_max and
            jogador[3] in posicoes and
            jogador[0] in nacionalidades and
            jogador[2] in pais_clube and
            any(tecnica.lower() in tecnicas_jogador for tecnica in tecnicas) and
            any(soft_skill.lower() in soft_skills_jogador for soft_skill in soft_skills)
        ):
            imc = calcular_imc(jogador[8], jogador[7])
            if 18.5 <= imc <= 24.9:
                forma = "em forma"
            elif imc < 18.5:
                forma = "abaixo do peso"
            else:
                forma = "acima do peso"
            informacoes_jogador = {
                "Nome": jogador[5],
                "País de Origem": jogador[0],
                "País do Clube": jogador[2],
                "Clube Atual": jogador[1],
                "Idade": jogador[4],
                "Forma física": forma,
                "Posição": jogador[3],
                "Valor de mercado": jogador[6],
                "Qtd amarelo": jogador[9],
                "Qtd vermelho": jogador[10],
                "lesão": jogador[11],
                "tecnicas": jogador[12],
                "softskills": jogador[13]
            }
            jogadores_disponiveis.append(informacoes_jogador)
    return jogadores_disponiveis

# Interface Streamlit
st.title("Escolha de Jogadores para serem contratados")
st.sidebar.header("Critérios de Seleção")
orcamento = st.number_input("Digite o orçamento disponível", min_value=0, step=10000000)
posicoes = st.multiselect("Selecione as posições desejada(s)", ["atacante", "goleiro", "defensor", "meio_campista"])
idade_min = st.slider("Selecione a idade mínima", 16, 40, 20)
idade_max = st.slider("Selecione a idade máxima", 16, 40, 30)
nacionalidades = st.multiselect("Selecione o(s) país(es) de origem desejado(s)", ["portugal", "argentina", "brasil", "franca", "alemanha", "belgica", "italia", "espanha", "holanda", "uruguai", "escocia", "inglaterra", "Nenhuma específica"])
pais_clube = st.multiselect("Selecione os país(es) desejado(s) que o jogador deve jogar", ["arabia_saudita", "estados_unidos", "franca", "espanha", "inglaterra", "alemanha", "italia", "brasil", "Nenhuma específica"])
tecnicas = st.multiselect("Selecione a(s) qualidades técnica(s) desejada(s) do jogador", [
"Finalização",
"Cabeceio",
"Pênaltis",
"Dribles",
"Visão de jogo",
"Precisão nos passes",
"Criatividade no ataque",
"Velocidade",
"Controle de bola",
"Chutes de longa distância",
"Reflexos",
"Defesas",
"Habilidades de passe longo",
"Defesa sólida",
"Marcação",
"Jogo aéreo",
"Cruzamentos",
"Resistência",
"Versatilidade",
"Distribuição",
"Habilidades de um contra um",
"Comando da área",
"Posicionamento",
"Interceptações",
"Nenhuma específica"
])
soft_skills = st.multiselect("Selecione as soft skills desejadas", [
"Liderança",
"Disciplina",
"Determinação",
"Trabalho em equipe",
"Humildade",
"Confiança",
"Ambição",
"Mentalidade vencedora",
"Serenidade sob pressão",
"Confiabilidade",
"Calma",
"Destreza",
"Carisma",
"Concentração",
"Experiência",
"Inteligência tática",
"Nenhuma específica"
])
if st.button("Encontrar Jogadores"):
    jogadores_encontrados = encontrar_jogador(orcamento, posicoes, idade_min, idade_max, nacionalidades, pais_clube, tecnicas, soft_skills)
    if jogadores_encontrados:
        st.write("Jogadores encontrados:")
        for jogador in jogadores_encontrados:
            expander_text = f"""
            Nome: {jogador['Nome']}
            Idade: {jogador['Idade']}
            Valor de Mercado: {jogador['Valor de mercado']}
            País de Origem: {jogador['País de Origem']}
            Clube Atual: {jogador['Clube Atual']}
            País do Clube: {jogador['País do Clube']}
            Posição: {jogador['Posição']}
            Qualidades Técnicas: {jogador['tecnicas']}
            Soft Skills: {jogador['softskills']}
            """
            with st.expander(expander_text):
                st.markdown(f"**Quantidade de cartões amarelos na última temporada:** {jogador['Qtd amarelo']}", unsafe_allow_html=True)
                st.markdown(f"**Quantidade de cartões vermelhos na última temporada:** {jogador['Qtd vermelho']}", unsafe_allow_html=True)
                st.markdown(f"**Quantidade de lesões na última temporada:** {jogador['lesão']}", unsafe_allow_html=True)
                st.markdown(f"**Forma física baseado no IMC:** {jogador['Forma física']}", unsafe_allow_html=True)


    else:
        st.write("Nenhum jogador encontrado com os critérios fornecidos.")
st.markdown(
"""
<style>
div.stButton > button:first-child {
display: block;
margin: 0 auto;
}
</style>
""",
unsafe_allow_html=True
)