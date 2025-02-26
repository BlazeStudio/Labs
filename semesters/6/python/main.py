import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система по подбору фильмов")
        self.style = ttk.Style(theme="cosmo")  # Выбор темы (можно изменить на другую)
        self.current_state = 0
        self.responses = []
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

    def start_survey(self):
        self.current_state = 0
        self.responses = []
        self.ask_question()

    def ask_question(self):
        # Очистка предыдущих кнопок
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        if self.current_state == 0:
            self.label.config(text="Сколько времени вы готовы уделить просмотру фильма?")
            self.show_options(["Нет, у меня мало времени", "У меня много времени"])
        elif self.current_state == 1:
            self.label.config(text="Какой жанр вы предпочитаете?")
            self.show_options(["Фантастика", "Драма", "Боевик", "Комедия"])
        elif self.current_state == 2:
            self.label.config(text="Есть ли у вас предпочтения по жанру?")
            self.show_options(["Ограничений по жанру нет", "Есть предпочтения по жанру"])
        elif self.current_state == 3:
            self.label.config(text="Хотите ли вы посмотреть классический фильм?")
            self.show_options(["Нет, хочу что-то новое", "Да, хочу классику"])
        else:
            self.show_result()

    def show_options(self, options):
        for option in options:
            button = ttk.Button(self.questions_frame, text=option, command=lambda opt=option: self.record_response(opt), bootstyle=PRIMARY)
            button.pack(pady=5, fill=tk.X)

    def record_response(self, response):
        self.responses.append(response)
        self.current_state += 1
        self.ask_question()

    def show_result(self):
        result = self.get_recommendation()
        self.label.config(text=result)
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

    def get_recommendation(self):
        if self.responses[0] == "Нет, у меня мало времени":
            if self.responses[1] == "Фантастика":
                if self.responses[3] == "Нет, хочу что-то новое":
                    return "Мы рекомендуем вам фильм 'Бегущий по лезвию 2049'."
                else:
                    return "Мы рекомендуем вам фильм 'Интерстеллар'."
            else:
                return "Мы рекомендуем вам фильм 'Побег из Шоушенка'."
        else:
            if self.responses[2] == "Ограничений по жанру нет":
                return "Мы рекомендуем вам фильм 'Крёстный отец'."
            else:
                if self.responses[3] == "Нет, хочу что-то новое":
                    return "Мы рекомендуем вам фильм 'Матрица'."
                else:
                    return "Мы рекомендуем вам фильм 'Властелин колец: Братство кольца'."

    def show_help(self):
        messagebox.showinfo("Помощь", "Эта система поможет вам выбрать фильм на основе ваших предпочтений.")

    def restart_survey(self):
        self.current_state = 0
        self.responses = []
        self.ask_question()

    def confirm_exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Выбор темы (можно изменить на другую)
    app = ExpertSystem(root)
    root.mainloop()