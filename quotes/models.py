# Copyright (c) 2019-2020 Eugene Davies All Rights Reserved. Some HTML pages are purely created for test purpose and are not the best views I would suggest

from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


