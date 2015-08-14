from django.contrib import admin

from .models import Puzzle, PuzzleBoard, Clue



class PuzzleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Puzzle, PuzzleAdmin)


class ClueAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clue, ClueAdmin)


class PuzzleBoardAdmin(admin.ModelAdmin):
    pass
admin.site.register(PuzzleBoard, PuzzleAdmin)