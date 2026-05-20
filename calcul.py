import sum  #항들을 더하기 위해 sum 모듈 호출

def calcul(formula):    #str형태로 한글자씩이 원소인 리스트를 formula에 넣기

    parts = []  #항들만 저장할 리스트 parts 생성
    numBuffer = ""  #임시로 항을 저장할 numBuffer 생성

    #formula 형태를 parts에 항 별로 구분하여 추가
    for i, ch in enumerate(formula):    #formula의 원소 번호는 i, 원소 내용은 ch에 순서대로 넣어 반복

        #+로 항 구분
        if ch == "+":   #ch가 +면
            parts.append(numBuffer) #numBuffer에 있던 내용(항)을 parts의 새 원소로 넣기(없다면 무시)
            numBuffer = ""  #다음 항을 받기 위해 numBuffer 초기화
        
        #-로 항 구분
        elif ch in "-−": #ch가 +가 아니고 -이면 (gpt등에서 수식을 받으면 −(미들바 아님)로 받기에 이 경우도 추가)

            #부호 앞에 부호가 있다면 뒤 부호도 항에 추가
            if i == 0 or formula[i-1] in "+-":  #부호 앞에 또다른 부호가 있다면 (예: 5'+-'1)
                numBuffer += ch #ch에 있는 해당 기호도 numBuffer에 넣어 연산자로 쓰지 않기
            else:   #부호 앞에 부호가 없다면
                parts.append(numBuffer) #numBuffer에 있는 항을 parts의 새 원소로 넣기
                numBuffer = "-" #현재 항 앞에 -기호 추가
        else:   #ch가 부호가 아니라면
            numBuffer += ch #numBuffer에 ch(숫자) 추가
    
    #마지막 항은 뒤에 오는 연산자가 없기에 따로 parts에 추가 (버퍼가 비어있지 않을 때만)
    if numBuffer != "": parts.append(numBuffer) #마지막 항을 마지막으로 parts의 새 원소로 넣기

    #완성된 parts(예: ['5', '-1, '3.1'])를 sum 모듈에 넣어 다항식 계산
    return sum.add(parts)   #완성된 parts에 sum 모듈에 넣어 return