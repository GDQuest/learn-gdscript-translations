Hi there! 

If you'd like to help translate, please use any file in `▶️ To Do` status from the table below (`⏳ Translation progress` section).

If you want to test the translation in the app, read the instructions in the `🧪 How to test Russian translation in Godot` section.

Also, be sure to check out the `📜 Translation` guide section before you get started.

Any help is welcome!

## Click the title below to expand the text:

---

<details>
<summary>⏳ Translation progress: ⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜ 30,18%</summary>

✅ = Done  
⏳ = Currently In Progress  
▶️ = To Do  

|  № |                    File                    |  Lenght  |   %  |   Complete    |
|:--:|--------------------------------------------|:--------:|:----:|:---------------:|
|  1 |application.po                              |  17 227  | 6,53 |    ✅ Done     |
|  2 |classref_database.po                        |   4 618  | 1,75 |    ✅ Done     |
|  3 |error_database.po                           |  17 779  | 6,74 |    ✅ Done     |
|  4 |glossary_database.po                        |  13 464  | 5,10 |    ✅ Done     |
|  5 |lesson-1-what-code-is-like.po               |  10 178  | 3,86 |    ✅ Done     |
|  6 |lesson-2-your-first-error.po                |   4 224  | 1,60 |    ✅ Done     |
|  7 |lesson-3-standing-on-shoulders-of-giants.po |  12 151  | 4,61 |    ✅ Done     |
|  8 |lesson-4-drawing-a-rectangle.po             |   6 532  | 2,48 | ⏳ In Progress |
|  9 |lesson-5-your-first-function.po             |  10 045  | 3,81 |    ▶️ To Do   |
| 10 |lesson-6-multiple-function-parameters.po    |  13 253  | 5,02 |    ▶️ To Do   |
| 11 |lesson-7-member-variables.po                |  10 045  | 3,81 |    ▶️ To Do   |
| 12 |lesson-8-defining-variables.po              |   6 619  | 2,51 |    ▶️ To Do   |
| 13 |lesson-9-adding-and-subtracting.po          |   5 216  | 1,98 |    ▶️ To Do   |
| 14 |lesson-10-the-game-loop.po                  |   5 577  | 2,11 |    ▶️ To Do   |
| 15 |lesson-11-time-delta.po                     |   9 696  | 3,67 |    ▶️ To Do   |
| 16 |lesson-12-using-variables.po                |   6 974  | 2,64 |    ▶️ To Do   |
| 17 |lesson-13-conditions.po                     |   8 458  | 3,21 |    ▶️ To Do   |
| 18 |lesson-14-multiplying.po                    |   6 601  | 2,50 |    ▶️ To Do   |
| 19 |lesson-15-modulo.po                         |   7 659  | 2,90 |    ▶️ To Do   |
| 20 |lesson-16-2d-vectors.po                     |   7 190  | 2,73 |    ▶️ To Do   |
| 21 |lesson-17-while-loops.po                    |   7 081  | 2,68 |    ▶️ To Do   |
| 22 |lesson-18-for-loops.po                      |   6 537  | 2,48 |    ▶️ To Do   |
| 23 |lesson-19-creating-arrays.po                |   6 447  | 2,44 |    ▶️ To Do   |
| 24 |lesson-20-looping-over-arrays.po            |   7 217  | 2,74 |    ▶️ To Do   |
| 25 |lesson-21-strings.po                        |   4 869  | 1,85 |    ▶️ To Do   |
| 26 |lesson-22-functions-return-values.po        |   5 749  | 2,18 |    ▶️ To Do   |
| 27 |lesson-23-append-to-arrays.po               |   7 429  | 2,82 |    ▶️ To Do   |
| 28 |lesson-24-access-array-indices.po           |   6 828  | 2,59 |    ▶️ To Do   |
| 29 |lesson-25-creating-dictionaries.po          |   7 807  | 2,96 |    ▶️ To Do   |
| 30 |lesson-26-looping-over-dictionaries.po      |   5 112  | 1,94 |    ▶️ To Do   |
| 31 |lesson-27-value-types.po                    |   8 103  | 3,07 |    ▶️ To Do   |
| 32 |lesson-28-specifying-types.po               |   7 167  | 2,72 |    ▶️ To Do   |
</details>

---

<details>
<summary>🧪 How to test Russian translation in Godot</summary>

1. Copy the latest version of `learn-gdscript` app code [from the GitHub repository](https://github.com/GDQuest/learn-gdscript/) in any way you like by cloning repository or simply downloading from GitHub WebPage (`Code-Download ZIP`). If you downloaded ZIP unpack `learn-gdscript-main` folder.
2. Copy the contents of the `ru` folder [from the translation repository](https://github.com/GDQuest/learn-gdscript-translations/tree/main/ru) to the `learn-gdscript-main/i18n/ru` folder.
3. Import the `learn-gdscript-main/project.godot` into Godot.
4. Open the `res://autoload/TranslationManager.gd` script in the Godot file manager and add `ru` language code to its `SUPPORTED_LOCALES` constant. The order of languages in `SUPPORTED_LOCALES` defines the order they'll appear in the settings menu. Example code fragment from `TranslationManager.gd`:

```Python
const SUPPORTED_LOCALES := [
	"en", "ru"
]
```
5. Run the app by pressing F5, open the settings menu, and select the Russian language. The app will remember your choice when you reopen it.
</details>

---

<details>
<summary>📜 Translation guide for Russian-speaking editors</summary>

## 📜 Краткий справочник по переводу на русский язык

_Шпаргалка для будущих редакторов._

### ⭐ Основыные правила перевода:

- В английском языке в цитатах последняя точка ставится внутри кавычек. В русском — снаружи.

- В английских названиях номенклатурных единиц все слова пишутся С Большой Буквы (капитализация). Калькировать капитализацию при переводе на русский язык нельзя.

- При переводе «вы» пишется с маленькой буквы. «Вы» с большой буквы обычно используется только в деловой или личной переписке с одним человеком.

- В качестве кавычек используются строго «кавычки-елочки».

- Где необходимо по правилам русского языка, используется символ тире «—», а не дефис «-».

- Буква «ё» при переводе не используется, чтобы избежать проблем со шрифтами и вылезанием за пределы полей интерфейса.  

### 📑 Пояснения конкретных ситуациий при переводе:

- Смысловой англицизм «этот» (this, it) по возможности заменен на слово, о котором говорится (для более красивой стилистики).

- «эта» (ошибка, функция) — переведено как «данная» (ошибка, функция).

- «decimal number» — переведено как «десятичная дробь», а не «десятичное число» или «число с десятичной дробью».

- «increment» — переведено как «инкремент», а не «приращение», т.к. инкремент — это математический термин и такой перевод устоялся в русской компьютерной литературе.
  
- «bits» of code (data) — переведено как «фрагменты» кода (данных), а не «блоки», «части» или «биты».

- «type hint» — переведено как «обозначение типа переменной», т.к. «подсказка типа» звучит странно и некрасиво по-русски. Речь идет о статической типизации — ручном указании типа при инициализации переменной (var имя : тип = значение). Лексически более верный перевод «определение типа переменной» не подходит, т.к. имеет второе значение — получение типа уже существующей переменной с помощью функции GDScript typeof(имя), а не только обозначение (задание, установку) типа новой переменной.

- «hint»  — так же переведено в большинстве случаев как «обозначение».

- «opening and a closing parenthesis» — переведено как «открывающая и закрывающая круглые скобки». Перевод: «открывающаяся и закрывающаяся» неверный и означает, что скобка открывает и закрывает сама себя.

- «Why does that happen?» — переведено как «Почему так происходит?», а не «Почему это происходит?».

### 📋 Список задач для будущих улучшений:

- На свежую голову вычитать весь перевод в запущенном приложении на предмет опечаток, англицизмов (английского построения предложений) и вылезаний за пределы полей интерфейса.

- Проверить автопоиском, чтобы везде правильно были закрыты теги, самая частая ошибка — лишний пробел в закрывающих тегах: `[ /i]` и `[ /b]`. Должно быть: `[/i]` и `[/b]`.

- «you tell it (computer) to» — в разных местах переведено по-разному: «вы указываете ему (компьютеру)», «вы говорите ему (компьютеру)», «вы приказываете ему (компьютеру)». Хотелось бы подобрать одно максимально лаконичное слово, которое бы хорошо вписывалось во все контексты.  
Вариант «вы сообщаете ему (компьютеру)» везде заменен на «вы указываете ему (компьютеру)».
</details>

---

<details>
<summary>👦🏻 About me (Paul Argent)</summary>

Hi there! My name is Paul Argent. I'm a Russian native speaker with good knowledge of Russian grammar and programming context.

I really would like to popularize Godot among Eastern European students and novice developers despite the craziness going now in my brotherhood Russian-speaking countries.

I will try to translate the lessons using a good Russian style of text (avoiding anglicisms where possible). Where it is impossible to translate terms, I will use explanations in parentheses and generally accepted terms in the Russian programming literature.

I have translation experience for story games and some software before.

I'm working on the translation in my free time from my main job and therefore it is not going very fast. Any help is welcome!
</details>

---

