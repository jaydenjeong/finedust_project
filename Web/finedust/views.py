from django.shortcuts import render, redirect
from predictions.models import Predictions

def main(request):
    # main페이지의 지역선택에서 loc으로 지역번호를 get요청으로 받아와서 처리
    # 처음 loc이 없을경우(get 요청이 없을경우) 서울("108")을 기본값으로 설정
    loc = request.GET.get("loc", "108")

    # 선택된 loc의 지역의 object를 불러옴
    predict = Predictions.objects.filter(loc = loc)

    # 시간이 int타입으로 데이터베이스에 저장되어있는데 웹에서 ??:00 시 로 표시하기위하여 str타입으로 변경하며 3, 6, 9 시 같이 한자리수인경우 zfill을 통해 앞에 0을 채워넣음
    # str로 변경하고 0을 채워넣어 2자리로 만든 time컬럼 저장
    for pred in predict:
        if isinstance(pred.time, int):
            pred.time = str(pred.time).zfill(2)
            pred.save()

    # 우리가 사용하게될 요일(날짜)를 li로 리스트 저장
    # distinct를 사용하여 중복제거
    li = predict.values_list("date", flat=True).distinct()

    pred1 = []
    pred2 = []
    pred3 = []

    # predict로 가져온 지역의 데이터를 날짜기준으로 pred1, 2, 3에 저장
    for pred in predict:
        if pred.date == li[0]:
            pred1.append(pred)
        elif pred.date == li[1]:
            pred2.append(pred)
        elif pred.date == li[2]:
            pred3.append(pred)

    # context로 지역의 해당요일의 기상정보와 날짜를 가져옴
    context = {
        "pred1" : pred1,
        "pred2" : pred2,
        "pred3" : pred3,
        "li" : li
    }

    return render(request, "main.html", context)
