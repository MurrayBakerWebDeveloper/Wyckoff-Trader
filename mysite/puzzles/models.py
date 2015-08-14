from django.db import models


class Puzzle(models.Model):
    """
    Model representing a crossword puzzle
    """
    DIFFICULTY_CHOICES = (
        ('EA', 'Easy'),
        ('INT', 'Intermediate'),
        ('HA', 'Hard'),
        ('DE', 'Devilish'),
    )

    name = models.CharField(max_length=25, null=False, blank=False)
    difficulty = models.CharField(max_length=3, choices=DIFFICULTY_CHOICES)

    clues = models.ManyToManyField('Clue')
    puzzle_board = models.ForeignKey('PuzzleBoard', null=False, blank=False)

    def __unicode__(self):
        return self.name


class Clue(models.Model):
    """
    Represents one clue in a crossword puzzle
    """
    DIRECTION_CHOICES = (
        ('A', 'Across'),
        ('D', 'Down'),
    )

    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES)
    text = models.CharField(max_length=255, null=False, blank=False)
    number = models.IntegerField(help_text='The location of the clue on the board')

    def __unicode__(self):
        return '{} {}'.format(self.number, self.get_direction_display())


class PuzzleBoard(models.Model):
    """
    The layout of the blank spaces on the board
    """
    width = models.IntegerField(null=False, blank=False, default=15)
    height = models.IntegerField(null=False, blank=False, default=15)

    def __unicode__(self):
        return '{} by {} Board'.format(self.width, self.height)

    class Meta:
        unique_together = ('width', 'height')