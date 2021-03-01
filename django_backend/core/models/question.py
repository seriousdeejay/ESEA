from __future__ import annotations
from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _

from .question_option import QuestionOption


class questionManager(models.Manager):
    def create(self, isMandatory, answertype, name, description=None, instruction=None, options=None):
        print("sssssss", options, 'dd')
        question = self.model(isMandatory=isMandatory, name=name, description=description, instruction=instruction, answertype=answertype)
        question.save()
        print(question.answertype)
        print(question.QUESTION_TYPES_WITH_OPTIONS)
        if question.answertype in (question.QUESTION_TYPES_WITH_OPTIONS):
            for option in options:
                print(option)
                questionoption = QuestionOption.objects.create(text=option, value=1, question=question)
                question.options.add(questionoption)
                #QuestionOption.create(question=question, text=option, value=1)
            question.save()
        return question

class Question(models.Model):
    objects = questionManager()
    isMandatory = models.BooleanField(default=True)
    # topic = models.ForeignKey('Topic', related_name="topic_questions", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    topics = models.ManyToManyField("Topic", through="DirectIndicator")
    options = models.ManyToManyField(QuestionOption, blank=True, related_name="ooo") 
    #options: QuestionOption

    TEXT = "TEXT"
    NUMBER = "NUMBER"
    RADIO = "RADIO"
    CHECKBOX = "CHECKBOX"
    # DROPDOWN = "DROPDOWN"
    QUESTION_TYPES = (
        (TEXT, "text"),
        (NUMBER, "number"),
        (RADIO, "radio"),
        (CHECKBOX, "checkbox")
    )
    QUESTION_TYPES_WITH_OPTIONS = [RADIO, CHECKBOX]
    answertype = models.CharField(max_length=100, blank=False, choices=QUESTION_TYPES, default="TEXT")

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return f"{self.name}({self.id})"

    def __repr__(self) -> str:  # -> str?
        return (
            f"<Question id='{self.id}' name='{self.name}' "
            f"answertype='{self.answertype}'>"
        )


# class questionManager(models.Manager):  # type: ignore
#     def create(
#         self,
#         name,
#         type,
#         options,
#         description=None,
#         prefix=None,
#         suffix=None,
#         default=None,
#     ):
#         question = self.model(
#             name=name,
#             type=type,
#             description=description,
#             prefix=prefix,
#             suffix=suffix,
#             default=default,
#         )
#         question.save()

#         if question.type in question.QUESTION_TYPES_WITH_OPTIONS:
#             for option in options:
#                 question.options.create(question=question, **option)
#             question.save()
#         return question

#     def get_or_create(self, **args):
#         question = self.model.findQuestion(**args)
#         if not question:
#             question = self.model.objects.create(**args)
#         return question


# class Question(models.Model):
#     objects = questionManager()
#     name = models.CharField(max_length=255, blank=False)
#     description = models.TextField(blank=True, null=True)
#     prefix = models.CharField(max_length=10, blank=True, default="")
#     suffix = models.CharField(max_length=10, blank=True, default="")
#     default = models.CharField(max_length=255, blank=True, default="")
#     topics = models.ManyToManyField("Topic", through="DirectIndicator")
#     options: QuestionOption

#     TEXT = "TEXT"
#     NUMBER = "NUMBER"
#     RADIO = "RADIO"
#     CHECKBOX = "CHECKBOX"
#     QUESTION_TYPES = (
#         (TEXT, "text"),
#         (NUMBER, "number"),
#         (RADIO, "radio"),
#         (CHECKBOX, "checkbox"),
#     )
#     QUESTION_TYPES_WITH_OPTIONS = [RADIO, CHECKBOX]
#     type = models.CharField(
#         max_length=100, blank=False, choices=QUESTION_TYPES, default="TEXT"
#     )

#     class Meta:
#         verbose_name = _("question")
#         verbose_name_plural = _("questions")

#     def __repr__(self) -> str:
#         return (
#             f"<Question id='{self.id}' name='{self.name}' "
#             f"prefix='{self.prefix}' suffix='{self.suffix}'"
#             f"default='{self.default}' type='{self.type}'>"
#         )

#     def hasOptions(self, options) -> bool:
#         if not self.options.count() == len(options):
#             return False

#         optionsExists = True
#         for inputOption in options:
#             for option in self.options.all():
#                 if inputOption["text"] == option.text:
#                     break
#             if not option.equal(inputOption):
#                 optionsExists = False

#         return optionsExists

#     # TODO: Improve typing of this function
#     def findQuestion(
#         name,
#         type,
#         options,
#         description=None,
#         prefix=None,
#         suffix=None,
#         default=None,
#     ) -> Any:
#         questions = Question.objects.filter(
#             name=name,
#             type=type,
#             description=description,
#             prefix=prefix,
#             suffix=suffix,
#             default=default,
#         )
#         for question in questions:
#             if question.hasOptions(options):
#                 return question
#         return False

#     def update(
#         self,
#         name,
#         type,
#         options,
#         description=None,
#         prefix=None,
#         suffix=None,
#         default=None,
#     ) -> "Question":
#         question: Question = Question.findQuestion(
#             name, type, options, description, prefix, suffix, default,
#         )

#         if question and question.id != self.id:
#             self.delete()
#             return question

#         self.name = name
#         self.type = type
#         self.description = description
#         self.prefix = prefix
#         self.suffix = suffix
#         self.default = default
#         self.save()

#         if not self.hasOptions(options):
#             self.options.all().delete()
#             for option in options:
#                 QuestionOption.objects.create(question=self, **option)

#         self.save()
#         return self