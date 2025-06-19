import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont

class IMCCalculatorUltimate:
    def __init__(self, root):
        self.root = root
        self.root.title("IMC Expert")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f7fa")
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Fontes
        self.title_font = tkFont.Font(family="Segoe UI", size=22, weight="bold")
        self.subtitle_font = tkFont.Font(family="Segoe UI", size=10)
        self.label_font = tkFont.Font(family="Segoe UI", size=11)
        self.entry_font = tkFont.Font(family="Segoe UI", size=12)
        self.button_font = tkFont.Font(family="Segoe UI", size=12, weight="bold")
        self.imc_font = tkFont.Font(family="Segoe UI", size=42, weight="bold")
        self.class_font = tkFont.Font(family="Segoe UI", size=14)
        self.advice_font = tkFont.Font(family="Segoe UI", size=11)
        
        # Cores
        self.colors = {
            "bg": "#f5f7fa",
            "card": "#ffffff",
            "text": "#2b2d42",
            "accent": "#4361ee",
            "underweight": "#4cc9f0",
            "normal": "#38b000",
            "overweight": "#ffaa00",
            "obesity1": "#f8961e",
            "obesity2": "#f72585",
            "obesity3": "#d00000",
            "highlight": "#3a0ca3"
        }
        
        self.configure_styles()
        self.create_widgets()
        
        # Valores iniciais para teste
        self.weight_entry.insert(0, "82.5")
        self.height_entry.insert(0, "1.75")
    
    def configure_styles(self):
        self.style.configure('TFrame', background=self.colors["bg"])
        self.style.configure('Card.TFrame', background=self.colors["card"], relief=tk.FLAT, borderwidth=0)
        self.style.configure('TButton', font=self.button_font, background=self.colors["accent"], 
                          foreground="white", borderwidth=0)
        self.style.map('TButton', background=[('active', '#3a56d5')])
    
    def create_widgets(self):
        # Frame principal com scroll
        self.main_canvas = tk.Canvas(self.root, bg=self.colors["bg"], highlightthickness=0)
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.main_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.main_canvas.configure(yscrollcommand=scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        
        self.main_frame = ttk.Frame(self.main_canvas, style='TFrame')
        self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        
        # Título
        tk.Label(
            self.main_frame,
            text="CALCULADORA DE IMC",
            font=self.title_font,
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=(20, 5))
        
        tk.Label(
            self.main_frame,
            text="Descubra seu peso ideal e metas de saúde",
            font=self.subtitle_font,
            bg=self.colors["bg"],
            fg="#6c757d"
        ).pack(pady=(0, 30))
        
        # Seção de entrada de dados
        input_frame = ttk.Frame(self.main_frame, style='Card.TFrame', padding=25)
        input_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Peso
        weight_frame = ttk.Frame(input_frame)
        weight_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            weight_frame,
            text="PESO ATUAL (kg)",
            font=self.label_font,
            bg=self.colors["card"],
            fg="#6c757d"
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.weight_entry = ttk.Entry(
            weight_frame,
            font=self.entry_font
        )
        self.weight_entry.pack(fill=tk.X)
        
        # Altura
        height_frame = ttk.Frame(input_frame)
        height_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            height_frame,
            text="ALTURA (m)",
            font=self.label_font,
            bg=self.colors["card"],
            fg="#6c757d"
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.height_entry = ttk.Entry(
            height_frame,
            font=self.entry_font
        )
        self.height_entry.pack(fill=tk.X)
        
        # Botão de cálculo
        ttk.Button(
            input_frame,
            text="CALCULAR IMC",
            command=self.calculate_imc,
            style='TButton'
        ).pack(fill=tk.X, pady=(15, 5))
        
        # Seção de resultados
        self.result_frame = ttk.Frame(self.main_frame, style='Card.TFrame', padding=25)
        self.result_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Resultado do IMC
        result_top_frame = ttk.Frame(self.result_frame)
        result_top_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            result_top_frame,
            text="SEU IMC",
            font=self.label_font,
            bg=self.colors["card"],
            fg="#6c757d"
        ).pack(anchor=tk.W)
        
        self.imc_value_frame = ttk.Frame(result_top_frame)
        self.imc_value_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.imc_label = tk.Label(
            self.imc_value_frame,
            text="--",
            font=self.imc_font,
            bg=self.colors["card"],
            fg=self.colors["accent"]
        )
        self.imc_label.pack(side=tk.LEFT)
        
        self.class_label = tk.Label(
            self.imc_value_frame,
            text="",
            font=self.class_font,
            bg=self.colors["card"],
            fg=self.colors["text"],
            padx=10
        )
        self.class_label.pack(side=tk.LEFT, padx=(20, 0), pady=10)
        
        # Divisor
        ttk.Separator(self.result_frame).pack(fill=tk.X, pady=10)
        
        # Metas de peso
        self.goals_frame = ttk.Frame(self.result_frame)
        self.goals_frame.pack(fill=tk.X)
        
        tk.Label(
            self.goals_frame,
            text="METAS DE PESO",
            font=self.label_font,
            bg=self.colors["card"],
            fg="#6c757d"
        ).pack(anchor=tk.W, pady=(0, 10))
        
        # Grid para metas
        self.goal_grid = ttk.Frame(self.goals_frame)
        self.goal_grid.pack(fill=tk.X)
        
        # Cabeçalhos do grid
        tk.Label(
            self.goal_grid,
            text="OBJETIVO",
            font=self.label_font,
            bg=self.colors["card"],
            fg=self.colors["highlight"],
            width=15,
            anchor=tk.W
        ).grid(row=0, column=0, sticky=tk.W)
        
        tk.Label(
            self.goal_grid,
            text="PESO IDEAL",
            font=self.label_font,
            bg=self.colors["card"],
            fg=self.colors["highlight"],
            width=10,
            anchor=tk.W
        ).grid(row=0, column=1, sticky=tk.W)
        
        tk.Label(
            self.goal_grid,
            text="DIFERENÇA",
            font=self.label_font,
            bg=self.colors["card"],
            fg=self.colors["highlight"],
            width=15,
            anchor=tk.W
        ).grid(row=0, column=2, sticky=tk.W)
        
        # Linhas de resultados (serão preenchidas dinamicamente)
        self.goal_rows = []
        for i in range(3):
            row = []
            for j in range(3):
                lbl = tk.Label(
                    self.goal_grid,
                    text="--",
                    font=self.advice_font,
                    bg=self.colors["card"],
                    fg=self.colors["text"],
                    anchor=tk.W if j == 0 else tk.CENTER,
                    width=15 if j == 0 else 10
                )
                lbl.grid(row=i+1, column=j, sticky=tk.W, pady=2)
                row.append(lbl)
            self.goal_rows.append(row)
        
        # Seção de recomendações
        self.advice_frame = ttk.Frame(self.main_frame, style='Card.TFrame', padding=25)
        self.advice_frame.pack(fill=tk.X, padx=20, pady=(0, 30))
        
        tk.Label(
            self.advice_frame,
            text="RECOMENDAÇÕES",
            font=self.label_font,
            bg=self.colors["card"],
            fg="#6c757d"
        ).pack(anchor=tk.W, pady=(0, 10))
        
        self.advice_label = tk.Label(
            self.advice_frame,
            text="Preencha seus dados para ver recomendações personalizadas",
            font=self.advice_font,
            bg=self.colors["card"],
            fg=self.colors["text"],
            wraplength=400,
            justify=tk.LEFT
        )
        self.advice_label.pack(fill=tk.X)
    
    def calculate_imc(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            
            if weight <= 0 or height <= 0:
                raise ValueError("Valores devem ser positivos")
            
            imc = weight / (height ** 2)
            classification, color = self.classify_imc(imc)
            
            # Atualizar resultados
            self.imc_label.config(text=f"{imc:.1f}", fg=color)
            self.class_label.config(text=classification, fg=color)
            
            # Calcular e mostrar metas
            self.show_weight_goals(weight, height, imc)
            
            # Mostrar recomendações
            self.show_recommendations(weight, height, imc)
            
            # Atualizar o scroll
            self.main_canvas.yview_moveto(0)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos\npara peso e altura")
    
    def classify_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso", self.colors["underweight"]
        elif 18.5 <= imc < 25:
            return "Peso normal", self.colors["normal"]
        elif 25 <= imc < 30:
            return "Sobrepeso", self.colors["overweight"]
        elif 30 <= imc < 35:
            return "Obesidade Grau I", self.colors["obesity1"]
        elif 35 <= imc < 40:
            return "Obesidade Grau II", self.colors["obesity2"]
        else:
            return "Obesidade Grau III", self.colors["obesity3"]
    
    def show_weight_goals(self, weight, height, imc):
        # Limpar linhas anteriores
        for row in self.goal_rows:
            for lbl in row:
                lbl.config(text="--")
        
        # Definir metas baseadas no IMC atual
        if imc < 18.5:
            # Abaixo do peso - mostrar metas para ganho
            targets = [
                ("Peso mínimo saudável", 18.5),
                ("Meta recomendada", 20.0)
            ]
        elif imc > 25:
            # Acima do peso - mostrar metas para perda
            targets = [
                ("Limite saudável", 24.9),
                ("Meta recomendada", 22.0),
                ("Peso ideal", 21.0)
            ]
        else:
            # Peso normal - mostrar manutenção
            targets = [
                ("Manter abaixo de", 24.9),
                ("Meta ideal", 22.0),
                ("Peso excelente", 21.0)
            ]
        
        # Preencher o grid com as metas
        for i, (label, target_imc) in enumerate(targets):
            target_weight = target_imc * (height ** 2)
            difference = weight - target_weight
            
            self.goal_rows[i][0].config(text=label)
            self.goal_rows[i][1].config(text=f"{target_weight:.1f} kg")
            
            if difference > 0:
                self.goal_rows[i][2].config(text=f"-{difference:.1f} kg", fg="#2ecc71")
            elif difference < 0:
                self.goal_rows[i][2].config(text=f"+{abs(difference):.1f} kg", fg="#3498db")
            else:
                self.goal_rows[i][2].config(text="✔️ Alcançado", fg="#38b000")
    
    def show_recommendations(self, weight, height, imc):
        if imc < 18.5:
            advice = (
                "Você está abaixo do peso ideal. Recomendamos:\n"
                "• Aumentar a ingestão calórica com alimentos nutritivos\n"
                "• Praticar exercícios de força para ganho muscular\n"
                "• Consultar um nutricionista para plano personalizado"
            )
        elif 18.5 <= imc < 25:
            advice = (
                "Você está na faixa de peso saudável! Recomendamos:\n"
                "• Manter hábitos alimentares balanceados\n"
                "• Praticar exercícios regularmente (150min/semana)\n"
                "• Monitorar seu peso mensalmente"
            )
        elif 25 <= imc < 30:
            advice = (
                "Você está com sobrepeso. Recomendamos:\n"
                "• Reduzir 250-500 calorias diárias para perda gradual\n"
                "• Aumentar atividade física (caminhadas, natação)\n"
                "• Priorizar alimentos integrais e reduzir processados"
            )
        else:
            advice = (
                "Você está na faixa de obesidade. Recomendamos:\n"
                "• Consultar médico e nutricionista para avaliação\n"
                "• Iniciar programa de exercícios supervisionados\n"
                "• Focar em mudanças sustentáveis a longo prazo"
            )
        
        self.advice_label.config(text=advice)

if __name__ == "__main__":
    root = tk.Tk()
    
    # Centralizar a janela
    window_width = 500
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = IMCCalculatorUltimate(root)
    root.mainloop()