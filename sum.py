def add(a, b):  #매개변수 a와 b를 더하는 함수
    if("." in a or "." in b): return float(a) + float(b)    #a또는 b에 .(소수점)이 있다면 둘을 실수형으로 변환한 뒤에 더한 값을 리턴
    else: return int(a) + int(b)    #아니라면 정수형으로 변환하여 더한 값을 리턴