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
        self.result_text = ""
        self.questions = []
        self.explanations = []
        self.setup_ui()
        self.film_db = {
    # Фантастика
    ("Короткий (до 2 часов)", "Фантастика", "Космос", "Научная достоверность"): ("Луна 2112", "фантастика про космос с реалистичной атмосферой", "1 ч 37 мин"),
    ("Длинный (больше 2 часов)", "Фантастика", "Космос", "Научная достоверность"): ("Интерстеллар", "эпическая фантастика про космос с реализмом", "2 ч 49 мин"),
    ("Короткий (до 2 часов)", "Фантастика", "Космос", "Приключения и экшен"): ("ВАЛЛ-И", "приключенческая фантастика с ярким миром", "1 ч 38 мин"),
    ("Длинный (больше 2 часов)", "Фантастика", "Космос", "Приключения и экшен"): ("Стражи Галактики", "весёлый космический экшен с фантастикой", "2 ч 1 мин"),
    ("Длинный (больше 2 часов)", "Фантастика", "Будущее на Земле", "Социальные идеи"): ("Робот по имени Чаппи", "реалистичная фантастика о будущем", "2 ч"),
    ("Короткий (до 2 часов)", "Фантастика", "Будущее на Земле", "Визуальные миры"): ("Бегущий по лезвию 2049", "мрачная картина о будущем", "1 ч 44 мин"),
    ("Короткий (до 2 часов)", "Фантастика", "Будущее на Земле", "Социальные идеи"): ("Обливион", "захватывающее будущее в вымышленном мире", "1 ч 56 мин"),
    ("Длинный (больше 2 часов)", "Фантастика", "Будущее на Земле", "Визуальные миры"): ("Матрица", "фантастика с философией и боевыми сценами", "2 ч 16 мин"),

    # Драма
    ("Короткий (до 2 часов)", "Драма", "Личные переживания", "Индивидуальная трагедия"): ("Король говорит!", "драма о преодолении на основе реальных событий", "1 ч 58 мин"),
    ("Длинный (больше 2 часов)", "Драма", "Личные переживания", "Индивидуальная трагедия"): ("Корейское братство", "трогательная история на реальных событиях", "2 ч 5 мин"),
    ("Короткий (до 2 часов)", "Драма", "Личные переживания", "Семейные отношения"): ("Одержимость", "драма о самоотдаче и цели", "1 ч 47 мин"),
    ("Длинный (больше 2 часов)", "Драма", "Личные переживания", "Семейные отношения"): ("Манчестер у моря", "тяжёлая драма о потере", "2 ч 17 мин"),
    ("Короткий (до 2 часов)", "Драма", "Социальные конфликты", "Острая и тяжёлая"): ("Фрукты надежды", "малая социальная драма", "1 ч 32 мин"),
    ("Длинный (больше 2 часов)", "Драма", "Социальные конфликты", "Острая и тяжёлая"): ("12 лет рабства", "основанная на реальности драма о рабстве", "2 ч 14 мин"),
    ("Короткий (до 2 часов)", "Драма", "Социальные конфликты", "Мягкая и вдохновляющая"): ("Комната", "драма о выживании и семье", "1 ч 58 мин"),
    ("Длинный (больше 2 часов)", "Драма", "Социальные конфликты", "Мягкая и вдохновляющая"): ("Бойцовский клуб", "сильная драма с социальным подтекстом", "2 ч 19 мин"),

    # Боевик
    ("Короткий (до 2 часов)", "Боевик", "Экшен", "Масштаб"): ("Адреналин", "динамичный боевик с Джейсоном Стэйтемом", "1 ч 28 мин"),
    ("Длинный (больше 2 часов)", "Боевик", "Экшен", "Масштаб"): ("Безумный Макс: Дорога ярости", "взрывной боевик с визуальным стилем", "2 ч"),
    ("Короткий (до 2 часов)", "Боевик", "Экшен", "Интенсивность"): ("Рейд", "интенсивный индонезийский боевик", "1 ч 41 мин"),
    ("Длинный (больше 2 часов)", "Боевик", "Экшен", "Интенсивность"): ("Апгрейд", "фантастический боевик с новыми актёрами", "2 ч"),
    ("Короткий (до 2 часов)", "Боевик", "Сюжет", "Линейный"): ("Грань будущего", "боевик с Томом Крузом и петлёй времени", "1 ч 53 мин"),
    ("Длинный (больше 2 часов)", "Боевик", "Сюжет", "Нелинейный"): ("Начало", "интеллектуальный боевик с Ди Каприо", "2 ч 28 мин"),
    ("Короткий (до 2 часов)", "Боевик", "Сюжет", "Линейный"): ("Поезд в Пусан", "боевик с социальной темой", "1 ч 58 мин"),
    ("Длинный (больше 2 часов)", "Боевик", "Сюжет", "Нелинейный"): ("Драйв", "стильный и напряжённый сюжетный боевик", "2 ч 10 мин"),

    # Военный
    ("Короткий (до 2 часов)", "Военный", "Вторая мировая", "Переживания героев"): ("Жизнь прекрасна", "военная драма с юмором и трагедией", "1 ч 56 мин"),
    ("Длинный (больше 2 часов)", "Военный", "Вторая мировая", "Историческая точность"): ("Список Шиндлера", "великая драма о Холокосте", "3 ч 15 мин"),
    ("Короткий (до 2 часов)", "Военный", "Вторая мировая", "Историческая точность"): ("Дюнкерк", "напряжённая история эвакуации", "1 ч 46 мин"),
    ("Длинный (больше 2 часов)", "Военный", "Вторая мировая", "Историческая точность"): ("Спасти рядового Райана", "реализм войны в большом масштабе", "2 ч 49 мин"),
    ("Короткий (до 2 часов)", "Военный", "Современные войны", "Психология солдата"): ("Братья", "драма о ПТСР и семье", "1 ч 45 мин"),
    ("Длинный (больше 2 часов)", "Военный", "Современные войны", "Тактика и технологии"): ("Повелитель бури", "война в Ираке через призму сапёра", "2 ч 11 мин"),
    ("Короткий (до 2 часов)", "Военный", "Современные войны", "Психология солдата"): ("Телохранитель киллера", "экшн в военной стилистике", "1 ч 58 мин"),
    ("Длинный (больше 2 часов)", "Военный", "Современные войны", "Тактика и технологии"): ("Падение Чёрного ястреба", "масштабная операция в Сомали", "2 ч 24 мин"),

    # Комедия
    ("Короткий (до 2 часов)", "Комедия", "Лёгкая", "Ситуационный юмор"): ("Василий Островский", "лёгкая политическая сатира", "1 ч 47 мин"),
    ("Длинный (больше 2 часов)", "Комедия", "Лёгкая", "Остроумные диалоги"): ("Доктор Стрейнджлав", "чёрная комедия о ядерной войне", "2 ч 3 мин"),
    ("Короткий (до 2 часов)", "Комедия", "Лёгкая", "Ситуационный юмор"): ("Мы - Миллеры", "забавная комедия о фальшивой семье", "1 ч 50 мин"),
    ("Длинный (больше 2 часов)", "Комедия", "Лёгкая", "Ситуационный юмор"): ("Тупой и ещё тупее", "абсурдная комедия в стиле 90-х", "2 ч 1 мин"),
    ("Короткий (до 2 часов)", "Комедия", "С элементами драмы", "Социально-критический"): ("Охота", "драма с сатирическим оттенком", "1 ч 55 мин"),
    ("Длинный (больше 2 часов)", "Комедия", "С элементами драмы", "Социально-критический"): ("Паразиты", "социальная драма с элементами сатиры", "2 ч 12 мин"),
    ("Короткий (до 2 часов)", "Комедия", "С элементами драмы", "Тёплый и человечный"): ("Ларри Краун", "лёгкая жизнеутверждающая драма", "1 ч 38 мин"),
    ("Длинный (больше 2 часов)", "Комедия", "С элементами драмы", "Тёплый и человечный"): ("1+1", "история дружбы, трогающая до слёз", "2 ч 5 мин"),
}



    def setup_ui(self):
        self.label = ttk.Label(self.root, text="Добро пожаловать в экспертную систему по подбору фильмов!", font=("Helvetica", 16))
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

        self.explanation_label = ttk.Label(self.root, text="", font=("Helvetica", 12), wraplength=800)
        self.explanation_label.pack(pady=10)

    def start_survey(self):
        self.current_state = 0
        self.responses = []
        self.questions = []
        self.explanations = []
        self.result_text = ""
        self.explanation_label.config(text="")
        self.ask_question()

    def ask_question(self):
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        if self.current_state == 0:
            self.questions.append("Какой длительности предпочитаете фильм?")
            self.explanations.append("ЭС начинает с длительности — это поможет разделить фильмы на короткие и длинные, чтобы предложить тот, который вам будет удобно посмотреть.")
            self.label.config(text=self.questions[-1])
            self.show_options(["Короткий (до 2 часов)", "Длинный (больше 2 часов)"])

        elif self.current_state == 1:
            self.questions.append("Какой жанр фильма вас интересует?")
            self.explanations.append("Жанр — ключевой параметр. Он формирует стиль, темп, и эмоциональное восприятие фильма.")
            self.label.config(text=self.questions[-1])
            self.show_options(["Фантастика", "Драма", "Боевик", "Военный", "Комедия"])

        elif self.current_state == 2:
            genre = self.responses[1]

            if genre == "Фантастика":
                self.questions.append("Вас больше привлекает масштабность или близость к реальности?")
                self.explanations.append("Это помогает понять, хотите ли вы грандиозные космические путешествия или более реалистичную научную фантастику.")
                self.label.config(text=self.questions[-1])
                self.show_options(["Космос", "Будущее на Земле"])

            elif genre == "Драма":
                self.questions.append("Какие темы вам ближе в драме?")
                self.explanations.append("ЭС уточняет, интересует ли вас личная трагедия героя или проблемы в обществе — это важный ориентир в выборе драмы.")
                self.label.config(text=self.questions[-1])
                self.show_options(["Личные переживания", "Социальные конфликты"])

            elif genre == "Боевик":
                self.questions.append("Что для вас важнее в боевике?")
                self.explanations.append("Кто-то хочет непрерывного действия, а кто-то — внятного и интересного сюжета.")
                self.label.config(text=self.questions[-1])
                self.show_options(["Экшен", "Сюжет"])

            elif genre == "Военный":
                self.questions.append("Какие исторические периоды вам интересны?")
                self.explanations.append("Выбор периода — ключ к стилю фильма: от реконструкций Второй мировой до современного кино о ближневосточных конфликтах.")
                self.label.config(text=self.questions[-1])
                self.show_options(["Вторая мировая", "Современные войны"])

            elif genre == "Комедия":
                self.questions.append("Какой стиль комедии вам ближе?")
                self.explanations.append("Лёгкие комедии ориентированы на отдых, а драмы с юмором дают повод задуматься.")
                self.label.config(text=self.questions[-1])
                self.show_options(["Лёгкая", "С элементами драмы"])

        elif self.current_state == 3:
            genre = self.responses[1]
            subgenre = self.responses[2]

            if genre == "Фантастика":
                if subgenre == "Космос":
                    self.questions.append("Что для вас важнее в космической фантастике?")
                    self.explanations.append("Некоторые зрители ценят реализм и научную достоверность, а другие — дух приключений и захватывающее действие.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Научная достоверность", "Приключения и экшен"])
                else:
                    self.questions.append("Какой главный мотив вам интереснее в будущем на Земле?")
                    self.explanations.append("Этот вопрос помогает понять, хотите ли вы размышлений о будущем общества или зрелищных визуальных миров.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Социальные идеи", "Визуальные миры"])

            elif genre == "Драма":
                if subgenre == "Личные переживания":
                    self.questions.append("Какой тип драмы вам ближе?")
                    self.explanations.append("Некоторые предпочитают интимные истории одного героя, другие — драмы о семье или взаимоотношениях.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Индивидуальная трагедия", "Семейные отношения"])
                else:
                    self.questions.append("Какая тональность социальной драмы вам ближе?")
                    self.explanations.append("Выбор между тяжёлой, остросоциальной драмой и мягкой, вдохновляющей — влияет на эмоциональное восприятие.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Острая и тяжёлая", "Мягкая и вдохновляющая"])

            elif genre == "Боевик":
                if subgenre == "Экшен":
                    self.questions.append("Что важнее: масштаб действия или интенсивность сцен?")
                    self.explanations.append("Фильмы с масштабом часто включают разрушения и спецэффекты, тогда как интенсивность означает плотность событий и динамику.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Масштаб", "Интенсивность"])
                else:
                    self.questions.append("Какая структура сюжета вам интереснее?")
                    self.explanations.append("Линейный сюжет даёт простую и ясную историю, а нелинейный требует вовлечения и анализа.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Линейный", "Нелинейный"])

            elif genre == "Военный":
                if subgenre == "Вторая мировая":
                    self.questions.append("Что для вас важнее в фильмах о Второй мировой?")
                    self.explanations.append("Это поможет понять, хотите ли вы увидеть историческую реконструкцию событий или сосредоточиться на судьбах конкретных людей.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Историческая точность", "Переживания героев"])
                else:
                    self.questions.append("Какой фокус предпочтительнее в современных военных фильмах?")
                    self.explanations.append("Современные военные фильмы могут сосредоточиться на технических аспектах или на психологических портретах солдат.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Тактика и технологии", "Психология солдата"])

            elif genre == "Комедия":
                if subgenre == "Лёгкая":
                    self.questions.append("Какой тип юмора вы предпочитаете?")
                    self.explanations.append("Лёгкие комедии могут быть гэговыми или более диалоговыми. Это влияет на стиль подачи и сценарий.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Ситуационный юмор", "Остроумные диалоги"])
                else:
                    self.questions.append("Насколько глубокий подтекст вы ожидаете от комедии с элементами драмы?")
                    self.explanations.append("Комедийные драмы могут быть лёгкими и трогательными или поднимать тяжёлые темы в ироничной форме.")
                    self.label.config(text=self.questions[-1])
                    self.show_options(["Тёплый и человечный", "Социально-критический"])

        elif self.current_state == 4:
            self.show_result()


    def show_options(self, options):
        for option in options:
            button = ttk.Button(self.questions_frame, text=option, command=lambda opt=option: self.record_response(opt), bootstyle=PRIMARY)
            button.pack(pady=5, fill=tk.X)

    def record_response(self, response):
        self.responses.append(response)
        self.current_state += 1
        self.ask_question()

    def go_back(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.responses.pop()
            self.questions.pop()
            self.explanations.pop()
            self.explanation_label.config(text="")
            self.ask_question()

    def show_result(self):
        self.result_text, explanation = self.get_recommendation()
        self.label.config(text="Результат:")
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        result_label = ttk.Label(self.questions_frame, text=self.result_text, font=("Helvetica", 14), wraplength=800, justify="left")
        result_label.pack(pady=10)

        explanation_label = ttk.Label(self.questions_frame, text=explanation, font=("Helvetica", 12), wraplength=800, justify="left")
        explanation_label.pack(pady=10)

    def get_recommendation(self):
        duration = self.responses[0]
        genre = self.responses[1]
        detail1 = self.responses[2]
        detail2 = self.responses[3]

        is_short = duration == "Короткий (до 2 часов)"
        time_phrase = "короткий" if is_short else "длинный"

        key = (duration, genre, detail1, detail2)
        print(key)
        film = self.film_db.get(key)

        if film:
            film_title, film_desc, film_length = film

            reasoning = f"""
Вы выбрали {time_phrase} фильм в жанре {genre.lower()}.

На втором этапе ЭС уточнила направление в жанре — это позволило выделить интересующую вас подкатегорию.

На третьем этапе ЭС проанализировала ваши предпочтения по стилю и подходу к сюжету — это ключевой фильтр, позволивший выбрать подходящий тон повествования.

В результате система определила, что вам подойдёт фильм **{film_title}** — это {film_desc}.
Продолжительность: {film_length}.
"""
            return film_title, reasoning.strip()
        else:
            return "Фильм не найден", "К сожалению, не удалось подобрать фильм по вашему выбору."


    def show_help(self):
        if self.current_state < len(self.explanations):
            message = self.explanations[self.current_state]
        else:
            message = "На этом этапе помощь не требуется."
        messagebox.showinfo("Помощь", message)

    def restart_survey(self):
        self.start_survey()

    def confirm_exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

    def copy_result(self):
        if self.result_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.result_text)
            self.root.update()
            messagebox.showinfo("Копирование", "Результат скопирован в буфер обмена!")

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = ExpertSystem(root)
    root.mainloop()
