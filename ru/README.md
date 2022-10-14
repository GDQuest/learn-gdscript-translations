Hi there! 

If you want to test the translation in the app, read the instructions in the `🧪 How to test Russian translation in Godot` section.

Also, be sure to check out the `📜 Translation` guide section before you get started.

Any help is welcome!

## Click the title below to expand the text:

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

- При переводе «вы» пишется с маленькой буквы. «Вы» с большой буквы обычно используется только в деловой или личной переписке с одним человеком.

- Где необходимо по правилам русского языка, используется символ тире «—», а не дефис «-».

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

