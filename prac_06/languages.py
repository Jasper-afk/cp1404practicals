"""
CP1404 Practical 6 languages exercise.
Estimate: 25 minutes
Actual: 21 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
programming_languages = [python, ruby, visual_basic]
print(python)

print("The dynamically typed languages are:")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)
