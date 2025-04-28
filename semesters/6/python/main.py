import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

class ExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система по подбору фильмов")
        self.root.geometry("900x700")
        self.style = ttk.Style(theme="cosmo")
        self.current_state = 0
        self.responses = []
        self.history = []
        self.help_messages = self.build_help_messages()
        self.setup_ui()

    def build_help_messages(self):
        return {
            0: "Выберите, сколько времени готовы уделить просмотру фильма — это влияет на масштаб и сложность сюжета.",
            1: "Выберите жанр — жанр определит основное настроение фильма.",
            2: {
                "Фантастика": "Какую тематику фантастики вы предпочитаете: далёкое будущее, киберпанк или инопланетные миры?",
                "Драма": "Хотите историю личной драмы или масштабную социальную проблему?",
                "Боевик": "Предпочитаете современный боевик, исторический или футуристический?",
                "Комедия": "Любите лёгкие комедии, чёрный юмор или сатиру?",
                "Военный": "Интересуют реальные исторические события или вымышленные истории?"
            },
            3: {
                "Фантастика": "Выберите, какой настрой вам ближе: философский, приключенческий или напряжённый.",
                "Драма": "Хотите, чтобы сюжет был медитативным, насыщенным событиями или шокирующим?",
                "Боевик": "Предпочтение к динамике: бесконечный экшен или развитие персонажей?",
                "Комедия": "Хотите более интеллектуальный юмор или что-то лёгкое и расслабляющее?",
                "Военный": "Фильм с акцентом на батальные сцены или на психологию персонажей?"
            },
            4: {
                "Фантастика": "И последнее: важна ли для вас зрелищность спецэффектов или сложность идеи?",
                "Драма": "Что важнее — развитие персонажей или социальная критика?",
                "Боевик": "Хотите неожиданную концовку или привычную героическую победу?",
                "Комедия": "Любите неожиданные повороты в комедии или классические шутки?",
                "Военный": "Хотите увидеть героизм или ужас войны?"
            }
        }

    def setup_ui(self):
        self.label = ttk.Label(self.root, text="Добро пожаловать в экспертную систему по подбору фильмов!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.questions_frame = ttk.Frame(self.root)
        self.questions_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(pady=10, fill=tk.X)

        self.start_button = ttk.Button(self.controls_frame, text="Начать опрос", command=self.start_survey, bootstyle=SUCCESS)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.help_button = ttk.Button(self.controls_frame, text="Помощь", command=self.show_help, bootstyle=INFO)
        self.help_button.pack(side=tk.LEFT, padx=5)

        self.back_button = ttk.Button(self.controls_frame, text="Назад", command=self.go_back, bootstyle=WARNING)
        self.back_button.pack(side=tk.LEFT, padx=5)

        self.restart_button = ttk.Button(self.controls_frame, text="Начать сначала", command=self.restart_survey, bootstyle=WARNING)
        self.restart_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = ttk.Button(self.controls_frame, text="Выход", command=self.confirm_exit, bootstyle=DANGER)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.explanation_label = ttk.Label(self.root, text="", font=("Helvetica", 12), wraplength=700)
        self.explanation_label.pack(pady=10)

    def start_survey(self):
        self.current_state = 0
        self.responses = []
        self.history = []
        self.explanation_label.config(text="")
        self.ask_question()

    def ask_question(self):
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        if self.current_state == 0:
            self.label.config(text="Готовы уделить фильму больше 2-х часов?")
            self.show_options(["Нет, короткий фильм", "Да, длинный фильм"])
        elif self.current_state == 1:
            self.label.config(text="Выберите жанр:")
            self.show_options(["Фантастика", "Драма", "Боевик", "Комедия", "Военный"])
        elif self.current_state == 2:
            genre = self.responses[1]
            if genre == "Фантастика":
                self.label.config(text="Какая тематика фантастики вам ближе?")
                self.show_options(["Далёкое будущее", "Киберпанк", "Инопланетные миры"])
            elif genre == "Драма":
                self.label.config(text="Какой тип драмы вам ближе?")
                self.show_options(["Личная драма", "Социальная драма"])
            elif genre == "Боевик":
                self.label.config(text="Какой тип боевика вам интереснее?")
                self.show_options(["Современный", "Исторический", "Футуристический"])
            elif genre == "Комедия":
                self.label.config(text="Какой стиль комедии вам нравится?")
                self.show_options(["Лёгкая", "Чёрная", "Сатира"])
            elif genre == "Военный":
                self.label.config(text="Какая тематика военного фильма вам ближе?")
                self.show_options(["Реальные события", "Вымышленные события"])
        elif self.current_state == 3:
            genre = self.responses[1]
            self.label.config(text=self.help_messages[3][genre])
            if genre == "Фантастика":
                self.show_options(["Философский", "Приключенческий", "Напряжённый"])
            elif genre == "Драма":
                self.show_options(["Медитативный", "Насыщенный событиями", "Шокирующий"])
            elif genre == "Боевик":
                self.show_options(["Бесконечный экшен", "Развитие персонажей"])
            elif genre == "Комедия":
                self.show_options(["Интеллектуальный юмор", "Классические шутки"])
            elif genre == "Военный":
                self.show_options(["Батальные сцены", "Психология персонажей"])
        elif self.current_state == 4:
            genre = self.responses[1]
            self.label.config(text=self.help_messages[4][genre])
            if genre == "Фантастика":
                self.show_options(["Зрелищность спецэффектов", "Сложность идеи"])
            elif genre == "Драма":
                self.show_options(["Развитие персонажей", "Социальная критика"])
            elif genre == "Боевик":
                self.show_options(["Неожиданная концовка", "Героическая победа"])
            elif genre == "Комедия":
                self.show_options(["Неожиданные повороты", "Классические шутки"])
            elif genre == "Военный":
                self.show_options(["Героизм", "Ужасы войны"])
        else:
            self.show_result()

    def show_options(self, options):
        for option in options:
            button = ttk.Button(self.questions_frame, text=option, command=lambda opt=option: self.record_response(opt), bootstyle=PRIMARY)
            button.pack(pady=5, fill=tk.X)

    def record_response(self, response):
        self.responses.append(response)
        self.history.append((self.current_state, response))
        self.current_state += 1
        self.ask_question()

    def go_back(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.responses.pop()
            self.history.pop()
            self.explanation_label.config(text="")
            self.ask_question()

    def show_result(self):
        result, explanation = self.get_recommendation()
        self.label.config(text=result)
        self.explanation_label.config(text=explanation)

    def get_recommendation(self):
        duration = self.responses[0]
        genre = self.responses[1]
        level1 = self.responses[2]
        level2 = self.responses[3]
        level3 = self.responses[4]

        explanation = f"Вы выбрали фильм в жанре {genre.lower()}, с особенностями: {level1.lower()}, {level2.lower()}, и предпочтением — {level3.lower()}."

        # Примеры выбора фильмов
        if genre == "Фантастика":
            if level1 == "Далёкое будущее":
                if level3 == "Сложность идеи":
                    return "Рекомендуем: 'Интерстеллар'", explanation
                else:
                    return "Рекомендуем: 'Аватар'", explanation
            elif level1 == "Киберпанк":
                return "Рекомендуем: 'Бегущий по лезвию 2049'", explanation
            else:
                return "Рекомендуем: 'Стражи Галактики'", explanation

        if genre == "Драма":
            if level1 == "Личная драма":
                return "Рекомендуем: 'Побег из Шоушенка'", explanation
            else:
                return "Рекомендуем: 'Три билборда на границе Эббинга, Миссури'", explanation

        if genre == "Боевик":
            if level1 == "Современный":
                return "Рекомендуем: 'Джон Уик'", explanation
            elif level1 == "Исторический":
                return "Рекомендуем: 'Гладиатор'", explanation
            else:
                return "Рекомендуем: 'Безумный Макс: Дорога ярости'", explanation

        if genre == "Комедия":
            if level1 == "Лёгкая":
                return "Рекомендуем: 'Очень плохие мамочки'", explanation
            elif level1 == "Чёрная":
                return "Рекомендуем: 'Кролик Джоджо'", explanation
            else:
                return "Рекомендуем: 'Диктатор'", explanation

        if genre == "Военный":
            if level1 == "Реальные события":
                return "Рекомендуем: 'Спасти рядового Райана'", explanation
            else:
                return "Рекомендуем: '1917'", explanation

        return "Не удалось подобрать фильм.", explanation

    def show_help(self):
        if self.current_state in self.help_messages:
            message = self.help_messages[self.current_state]
            if isinstance(message, dict):
                genre = self.responses[1]
                message = message.get(genre, "Помощь недоступна для этого выбора.")
        else:
            message = "Помощь недоступна для этого этапа."
        messagebox.showinfo("Помощь", message)

    def restart_survey(self):
        self.start_survey()

    def confirm_exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = ExpertSystem(root)
    root.mainloop()
