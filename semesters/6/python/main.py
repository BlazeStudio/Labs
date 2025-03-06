import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

class ExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система по подбору фильмов")
        self.root.geometry("800x600")
        self.style = ttk.Style(theme="cosmo")
        self.current_state = 0
        self.responses = []
        self.help_messages = {
            0: "Выберите, сколько времени вы готовы уделить просмотру фильма. Это поможет системе подобрать подходящий вариант.",
            1: "Выберите жанр фильма, который вам интересен. Это может быть фантастика, драма, боевик, военный или комедия.",
            2: {
                "Нет, у меня мало времени": {
                    "Фантастика": "Выберите, хотите ли вы фильм с необычным сюжетом.",
                    "Драма": "Выберите, хотите ли вы фильм с глубоким смыслом.",
                    "Боевик": "Выберите, хотите ли вы фильм с динамичным сюжетом.",
                    "Комедия": "Выберите, хотите ли вы лёгкий и весёлый фильм.",
                    "Военный": "Выберите, хотите ли вы фильм на основе реальных событий."
                },
                "У меня много времени": {
                    "Есть": "Выберите, хотите ли вы что-то новое или классическое.",
                    "Нет": "Выберите, хотите ли вы классику или что-то современное."
                }
            }
        }
        self.setup_ui()

    def setup_ui(self):
        # Основной заголовок
        self.label = ttk.Label(self.root, text="Добро пожаловать в экспертную систему по подбору фильмов!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Фрейм для вопросов и ответов (сверху)
        self.questions_frame = ttk.Frame(self.root)
        self.questions_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Фрейм для кнопок управления (снизу)
        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(pady=10, fill=tk.X)

        # Кнопка "Начать опрос"
        self.start_button = ttk.Button(self.controls_frame, text="Начать опрос", command=self.start_survey, bootstyle=SUCCESS)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Кнопка "Помощь"
        self.help_button = ttk.Button(self.controls_frame, text="Помощь", command=self.show_help, bootstyle=INFO)
        self.help_button.pack(side=tk.LEFT, padx=5)

        # Кнопка "Начать сначала"
        self.restart_button = ttk.Button(self.controls_frame, text="Начать сначала", command=self.restart_survey, bootstyle=WARNING)
        self.restart_button.pack(side=tk.LEFT, padx=5)

        # Кнопка "Выход"
        self.exit_button = ttk.Button(self.controls_frame, text="Выход", command=self.confirm_exit, bootstyle=DANGER)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Текстовое поле для обоснования
        self.explanation_label = ttk.Label(self.root, text="", font=("Helvetica", 12), wraplength=700)
        self.explanation_label.pack(pady=10)

    def start_survey(self):
        self.current_state = 0
        self.responses = []
        self.explanation_label.config(text="")
        self.ask_question()

    def ask_question(self):
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        if self.current_state == 0:
            self.label.config(text="Сколько времени вы готовы уделить просмотру фильма?")
            self.show_options(["Нет, у меня мало времени", "У меня много времени"])
        
        # Логика для "мало времени"
        elif self.current_state == 1 and self.responses[0] == "Нет, у меня мало времени":
            self.label.config(text="Какой жанр вы предпочитаете?")
            self.show_options(["Фантастика", "Драма", "Боевик", "Военный", "Комедия"])
        
        # Логика для "много времени"
        elif self.current_state == 1 and self.responses[0] == "У меня много времени":
            self.label.config(text="Есть ли у вас предпочтения по жанру?")
            self.show_options(["Есть", "Нет"])
        
        # Логика для "мало времени" (после выбора жанра)
        elif self.current_state == 2 and self.responses[0] == "Нет, у меня мало времени":
            if self.responses[1] == "Фантастика":
                self.label.config(text="Хотите ли вы фильм с необычным сюжетом?")
                self.show_options(["Да", "Нет"])
            elif self.responses[1] == "Драма":
                self.label.config(text="Хотите ли вы фильм с глубоким смыслом?")
                self.show_options(["Да", "Нет"])
            elif self.responses[1] == "Боевик":
                self.label.config(text="Хотите ли вы фильм с динамичным сюжетом?")
                self.show_options(["Да", "Нет"])
            elif self.responses[1] == "Комедия":
                self.label.config(text="Хотите ли вы лёгкий и весёлый фильм?")
                self.show_options(["Да", "Нет"])
            elif self.responses[1] == "Военный":
                self.label.config(text="Хотите ли вы фильм на основе реальных событий?")
                self.show_options(["Да", "Нет"])
        
        # Логика для "много времени" (после выбора предпочтений)
        elif self.current_state == 2 and self.responses[0] == "У меня много времени":
            if self.responses[1] == "Есть":
                self.label.config(text="Хотите ли вы что-то новое?")
                self.show_options(["Да", "Нет"])
            else:
                self.label.config(text="Хотите ли вы классику?")
                self.show_options(["Да", "Нет"])
        
        else:
            self.show_result()

    def show_options(self, options):
        for option in options:
            button = ttk.Button(self.questions_frame, text=option, command=lambda opt=option: self.record_response(opt), bootstyle=PRIMARY)
            button.pack(pady=5, fill=tk.X)
            self.animate_button(button)

    def animate_button(self, button):
        def flash():
            for _ in range(5):
                button.config(bootstyle=random.choice([PRIMARY, SUCCESS, INFO, WARNING, DANGER]))
                button.update_idletasks()
                button.after(100)
            button.config(bootstyle=PRIMARY)
        flash()

    def record_response(self, response):
        self.responses.append(response)
        self.current_state += 1
        self.ask_question()

    def show_result(self):
        result, explanation = self.get_recommendation()
        self.label.config(text=result)
        self.explanation_label.config(text=explanation)
        self.animate_text()

    def animate_text(self):
        def change_color():
            colors = ["red", "blue", "green", "purple", "orange"]
            self.label.config(foreground=random.choice(colors))
            self.root.after(500, change_color)
        change_color()

    def get_recommendation(self):
        # Логика для "мало времени"
        if self.responses[0] == "Нет, у меня мало времени":
            if self.responses[1] == "Фантастика":
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Начало'", "Вы выбрали фильм с необычным сюжетом. 'Начало' — это фильм с захватывающим и сложным сюжетом, который идеально подходит для любителей фантастики."
                else:
                    return "Рекомендуем: 'Интерстеллар'", "Вы выбрали классическую фантастику. 'Интерстеллар' — это эпический фильм о космических путешествиях и человеческих ценностях."
            elif self.responses[1] == "Драма":
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Побег из Шоушенка'", "Вы выбрали фильм с глубоким смыслом. 'Побег из Шоушенка' — это история о надежде и дружбе, которая оставляет сильное впечатление."
                else:
                    return "Рекомендуем: 'Крёстный отец'", "Вы выбрали классическую драму. 'Крёстный отец' — это культовый фильм о семье, власти и морали."
            elif self.responses[1] == "Боевик":
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Бегущий по лезвию 2049'", "Вы выбрали фильм с динамичным сюжетом. 'Бегущий по лезвию 2049' — это визуально потрясающий боевик с глубоким смыслом."
                else:
                    return "Рекомендуем: 'Матрица'", "Вы выбрали классический боевик. 'Матрица' — это фильм, который изменил представление о жанре."
            elif self.responses[1] == "Комедия":
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Мальчишник в Вегасе'", "Вы выбрали лёгкий и весёлый фильм. 'Мальчишник в Вегасе' — это комедия, которая поднимет вам настроение."
                else:
                    return "Рекомендуем: 'Джокер'", "Вы выбрали более серьёзный фильм. 'Джокер' — это драма с элементами комедии, которая заставляет задуматься."
            elif self.responses[1] == "Военный":
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Спасти рядового Райана'", "Вы выбрали фильм на основе реальных событий. 'Спасти рядового Райана' — это мощная военная драма."
                else:
                    return "Рекомендуем: '1917'", "Вы выбрали современный военный фильм. '1917' — это уникальный фильм, снятый в стиле одного дубля."
        
        # Логика для "много времени"
        else:
            if self.responses[1] == "Есть":
                if self.responses[2] == "Да":
                    return "Рекомендуем: '1917'", "Вы выбрали что-то новое. '1917' — это современный военный фильм с уникальной съёмкой."
                else:
                    return "Рекомендуем: 'Интерстеллар'", "Вы выбрали классику. 'Интерстеллар' — это эпический фильм о космосе и человеческих ценностях."
            else:
                if self.responses[2] == "Да":
                    return "Рекомендуем: 'Властелин колец'", "Вы выбрали классику. 'Властелин колец' — это эпическая трилогия, которая стала эталоном жанра."
                else:
                    return "Рекомендуем: 'Матрица'", "Вы выбрали что-то современное. 'Матрица' — это культовый фильм, который изменил представление о кино."

    def show_help(self):
        if self.current_state == 0:
            message = self.help_messages[0]
        elif self.current_state == 1:
            if self.responses[0] == "Нет, у меня мало времени":
                message = self.help_messages[1]
            else:
                message = self.help_messages[2][self.responses[0]][self.responses[1]]
        elif self.current_state == 2:
            if self.responses[0] == "Нет, у меня мало времени":
                message = self.help_messages[2][self.responses[0]][self.responses[1]]
            else:
                message = self.help_messages[2][self.responses[0]][self.responses[1]]
        else:
            message = "На этом этапе подсказки нет."
        
        messagebox.showinfo("Помощь", message)

    def restart_survey(self):
        self.current_state = 0
        self.responses = []
        self.explanation_label.config(text="")
        self.ask_question()

    def confirm_exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = ExpertSystem(root)
    root.mainloop()