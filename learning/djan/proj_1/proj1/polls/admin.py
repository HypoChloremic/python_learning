from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


# The Question model
class QuestionAdmin(admin.ModelAdmin):
    # The order of this list will determine the presentation
    # in the admin page for the given model, Question. 
    # fields = ["question_text", "pub_date"]
    fieldsets = [
        (None,                  {"fields": ["question_text"]}), 
        ("Date information",    {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)

# The Chocie model
# admin.site.register(Choice)