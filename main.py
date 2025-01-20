import flet as ft

def main(page: ft.Page):
    page.title = "Roma Fitness"
    page.theme = ft.Theme(color_scheme_seed="purple")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.scroll = ft.ScrollMode.ALWAYS

    # Header with logo and title
    header = ft.Row(
        [
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/711/711769.png", width=50, height=50),
            ft.Text("Roma Fitness", size=32, weight="bold", color="purple"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Dados simulados de treinos com mais exercícios
    treinos_db = {
        "Emagrecimento": {
            "Segunda-feira": ["Caminhada", "Abdominais", "Jumping jacks", "Corrida leve"],
            "Terça-feira": ["Corrida", "Flexões", "Mountain climbers", "Pular corda"],
            "Quarta-feira": ["Ciclismo", "Alongamento", "HIIT", "Burpees"],
            "Quinta-feira": ["Corrida leve", "Pular corda", "Aeróbicos", "Plank"],
            "Sexta-feira": ["HIIT", "Dança", "Stepper", "Zumba"],
            "Sábado": ["Yoga", "Pilates", "Alongamento", "Caminhada leve"],
            "Domingo": ["Descanso ativo", "Caminhada leve", "Meditação", "Tai chi"]
        },
        "Ganho de Massa": {
            "Segunda-feira": ["Levantamento de peso", "Agachamento", "Flexões com peso", "Tríceps banco"],
            "Terça-feira": ["Supino", "Flexões", "Rosca direta", "Deadlift"],
            "Quarta-feira": ["Rosca direta", "Tríceps banco", "Pull-ups", "Dips"],
            "Quinta-feira": ["Agachamento sumô", "Desenvolvimento de ombros", "Clean and press", "Leg press"],
            "Sexta-feira": ["Levantamento terra", "Abdominais com peso", "Lunges", "Power cleans"],
            "Sábado": ["Caminhada com peso", "Alongamento", "Barra fixa", "Push press"],
            "Domingo": ["Descanso", "Meditação", "Foam rolling", "Caminhada leve"]
        },
        "Idosos": {
            "Segunda-feira": ["Caminhada leve", "Alongamento", "Exercícios com elástico", "Tai chi"],
            "Terça-feira": ["Yoga", "Exercícios de respiração", "Dança moderada", "Alongamento leve"],
            "Quarta-feira": ["Pilates", "Alongamento de coluna", "Mobilidade articular", "Caminhada leve"],
            "Quinta-feira": ["Caminhada", "Exercícios de equilíbrio", "Alongamento leve", "Respiração guiada"],
            "Sexta-feira": ["Alongamento leve", "Dança moderada", "Exercícios de fortalecimento", "Meditação"],
            "Sábado": ["Exercícios de mobilidade", "Yoga leve", "Caminhada leve", "Alongamento"],
            "Domingo": ["Descanso ativo", "Meditação", "Exercícios de respiração", "Tai chi"]
        }
    }

    # Função para exibir treinos
    def exibir_treinos(prioridade, dias_selecionados, horarios_selecionados):
        page.controls.clear()
        page.controls.append(header)

        if nome_input.value and idade_input.value:
            page.controls.append(
                ft.Row(
                    [
                        ft.Text(f"Nome: {nome_input.value}", size=18, weight="bold", color="purple"),
                        ft.Text(f"Idade: {idade_input.value}", size=18, weight="bold", color="purple"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

        if not dias_selecionados:
            page.controls.append(ft.Text("Nenhum dia selecionado.", color="red"))
        else:
            for dia in dias_selecionados:
                if dia in treinos_db[prioridade]:
                    for horario in horarios_selecionados:
                        page.controls.append(
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(f"{dia} - {horario}", size=24, weight="bold", color="white"),
                                        ft.Text("Exercícios:", size=18, weight="bold", color="white"),
                                        ft.Text("\n".join(treinos_db[prioridade][dia]), size=16, color="white"),
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="purple",
                                border_radius=10,
                                padding=20,
                                expand=True,
                            )
                        )
                else:
                    page.controls.append(
                        ft.Text(f"Sem treinos cadastrados para {dia}.", color="gray")
                    )

        page.controls.append(ft.ElevatedButton("Voltar", on_click=lambda _: exibir_menu(), bgcolor="purple", color="white"))
        page.update()

    # Função para selecionar dias
    def selecionar_dias(prioridade):
        dias_selecionados = []

        def atualizar_dias(e):
            dias_selecionados.clear()
            for chk in checkboxes_dias:
                if chk.value:
                    dias_selecionados.append(chk.label)
            confirmar_button.disabled = len(dias_selecionados) == 0
            page.update()

        checkboxes_dias = [
            ft.Checkbox(label=dia, value=False, on_change=atualizar_dias)
            for dia in ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        ]

        confirmar_button = ft.ElevatedButton(
            "Confirmar",
            on_click=lambda _: selecionar_horarios(prioridade, dias_selecionados),
            bgcolor="purple",
            color="white",
            disabled=True,
        )

        page.controls.clear()
        page.controls.append(header)
        page.controls.append(ft.Text(f"Selecione os dias para treinar ({prioridade}):", size=20, weight="bold", color="purple"))
        page.controls.extend(checkboxes_dias)
        page.controls.append(confirmar_button)
        page.update()

    # Função para selecionar horários
    def selecionar_horarios(prioridade, dias_selecionados):
        horarios_selecionados = []

        def atualizar_horarios(e):
            horarios_selecionados.clear()
            for chk in checkboxes_horarios:
                if chk.value:
                    horarios_selecionados.append(chk.label)
            confirmar_button.disabled = len(horarios_selecionados) == 0
            page.update()

        checkboxes_horarios = [
            ft.Checkbox(label=horario, value=False, on_change=atualizar_horarios)
            for horario in ["Manhã", "Tarde", "Noite"]
        ]

        confirmar_button = ft.ElevatedButton(
            "Confirmar",
            on_click=lambda _: exibir_treinos(prioridade, dias_selecionados, horarios_selecionados),
            bgcolor="purple",
            color="white",
            disabled=True,
        )

        page.controls.clear()
        page.controls.append(header)
        page.controls.append(ft.Text(f"Selecione os horários para treinar:", size=20, weight="bold", color="purple"))
        page.controls.extend(checkboxes_horarios)
        page.controls.append(confirmar_button)
        page.update()

    # Função para exibir menu principal
    def exibir_menu():
        page.controls.clear()
        page.controls.append(header)
        
        if nome_input.value and idade_input.value:
            page.controls.append(
                ft.Row(
                    [
                        ft.Text(f"Nome: {nome_input.value}", size=18, weight="bold", color="purple"),
                        ft.Text(f"Idade: {idade_input.value}", size=18, weight="bold", color="purple"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

        page.controls.append(ft.Text("Escolha sua prioridade:", size=20, weight="bold", color="purple"))
        page.controls.append(
            ft.Column(
                [
                    ft.ElevatedButton("Emagrecimento", on_click=lambda _: selecionar_dias("Emagrecimento"), bgcolor="purple", color="white"),
                    ft.ElevatedButton("Ganho de Massa", on_click=lambda _: selecionar_dias("Ganho de Massa"), bgcolor="purple", color="white"),
                    ft.ElevatedButton("Idosos", on_click=lambda _: selecionar_dias("Idosos"), bgcolor="purple", color="white"),
                ],
                spacing=10,
            )
        )
        page.update()


    def criar_perfil(e):
        if nome_input.value and idade_input.value:
            exibir_menu()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos."), bgcolor="red")
            page.snack_bar.open = True
            page.update()


    nome_input = ft.TextField(label="Nome", autofocus=True, color="purple")
    idade_input = ft.TextField(label="Idade", keyboard_type=ft.KeyboardType.NUMBER, color="purple")
    confirmar_button = ft.ElevatedButton("Confirmar", on_click=criar_perfil, bgcolor="purple", color="white")
    

    page.controls.append(header)
    page.controls.append(nome_input)
    page.controls.append(idade_input)
    page.controls.append(confirmar_button)
    page.update()

ft.app(target=main)
           