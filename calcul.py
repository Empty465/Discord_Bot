import sum  #더하기 모듈 호출
import sub  #더하기 모듈 호출

def calcul(formula):    #매개변수 formula 설정 (str 형태의 리스트)

    parts = []  #받은 값을 수(항)과 기호를 분리하여 보관할 리스트 생성
    numBuffer = ""   #항 단위로 숫자만 임시로 저장할 버퍼 생성

    for ch in formula:  #formula의 원소들을 하나씩 ch에 넣어서 반복
        if ch in "+-−": #기호가 있을 경우 (-,−: 전자는 키보드 자판에 있는 중간 막대, 후자는 GPT가 쓰는 뺄셈 기호. 구분할 것)
            parts.append(numBuffer)  #parts에 순서대로 numBuffer값 대입 (아래 else: numBuffer += ch에서 한 항의 숫자를 모두 받으면 추가됨)
            parts.append(ch)    #parts에 순서대로 ch값 대입
            numBuffer = ""   #기호가 왔기 때문에 numBuffer의 값을 없애서 다음 항의 수를 받을 준비
        else: numBuffer += ch    #숫자가 들어올 경우, numBuffer에 추가(str이기에 두자리 이상의 숫자일 경우 필요함) (계속 숫자가 들어오면 계속 연결해서 입력되고, 기호가 오면 위의 parts.append(numBuffer)가 작동하여 parts에 한 원소로 숫자를 추가)

    parts.append(numBuffer)  #parts에 순서대로 numBuffer값 추가 (마지막 항은 이렇게 따로 처리해야 함)

    if("." in parts[0]): firstNum = float(parts[0]) #소수점이 있는 원소가 있을 경우 fistNum(계산할 앞 항)을 실수로 처리하여 실수값 대입
    else: firstNum = int(parts[0])  #아니면 정수값으로 처리하여 정수값 대입

    for i in range(1, len(parts), 2):   #첫 항(firstNum)을 건너띄고 parts의 원소들을 1칸 씩 띄어서 i 대입하며 반복 (항들 사이의 기호만 인식)

        simbol = parts[i]   #i번째 parts의 원소(기호) simbol 변수에 대입 (위의 for문으로 기호만 인식하여 덧,뺄셈 기호만 들어감)
        
        if("." in parts[i+1]): lastNum = float(parts[i + 1])  #기호 뒤에 있는 항에 소수점이 있으면 firstNum과 계산할 lastNum(계산할 뒤 항)을 실수로 처리하여 실수값 대입
        else: lastNum = int(parts[i + 1])   #아니면 lastNum을 정수로 처리하여 정수값 대입

        if simbol == "+":   #simbol(기호)가 +라면
            firstNum = sum.add([str(firstNum), str(lastNum)])   #두 항을 sum에 넣고 return된 값을 firstNum에 다시 대입하여 다음 계산 준비

        elif simbol == "-" or simbol == "−":    #simbol(기호)가 -(또는 −)이라면
            firstNum = sub.sub([str(firstNum), str(lastNum)])   #두 항을 sub에 넣고 return된 값을 firstNum에 다시 대입하여 다음 계산 준비

    return firstNum #기호가 더이상 없다면 최종 firstNum을 return