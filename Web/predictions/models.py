from django.db import models

class Predictions(models.Model):
    date = models.DateField("예측일", auto_now_add=False)
    time = models.IntegerField("예측시간")
    loc = models.CharField("지점번호", max_length = 5) # 서울 : 108, 부산 : 159, 대전 : 133, 광주 : 156, 강릉 : 105
    pm10 = models.FloatField("PM-10")
    pm25 = models.FloatField("PM-2.5")
    temperature = models.IntegerField("기온")
    percipitation = models.FloatField("강수량")
