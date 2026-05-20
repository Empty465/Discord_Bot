#괄호 계산 처리를 위한 정규식 모듈 호출
import re   

#문자열 변수(수식)를 받는 매개변수 formula를 계산하는 함수
def calcul(formula):   
    if "−" in formula: formula = formula.replace("−", "-")  #gpt같은 애들이 뺄셈 부호라고 던져주는 −를 -로 변환
    if "·" in formula: formula = formula.replace("·", "*")  #gpt같은 애들이 곱셈 부호라고 던져주는 ·를 *로 변환
    if "×" in formula: formula = formula.replace("×", "*")  #gpt같은 애들이 곱셈 부호라고 던져주는 ×를 *로 변환
    if "÷" in formula: formula = formula.replace("÷", "/")  #gpt같은 애들이 나눗셈 부호라고 던져주는 ÷를 /로 변환

    #일반적인 사칙연산 요소들만 허용
    allowed = "0123456789+-*/(). "  #허용 문자들이 있는 문자열 생성
    for ch in formula:  #formula의 내용물을 ch에 넣으며 반복
        if ch not in allowed:   #허용 문자들이 아닌 것이 인식되면
            return "숫자와 사칙연산 기호, 소수점, 괄호만 허가 됩니다."  #경고 메시지 return
    
    # 붙어있는 숫자와 괄호를 곱셈 형태로 변환
    # 예:
    # 2(3+5) -> 2*(3+5)
    # (1+2)(3+4) -> (1+2)*(3+4)
    formula = re.sub(r'(\d|\))\(', r'\1*(', formula)   #re.sub(찾을 패턴, 바꿀 문자열, 원본 문자열) 방식으로 작동
    # r'문자열' = 문자열을 그대로 처리 , \d = 숫자 , (내용물) = 괄호 안 내용을 저장 , \1 = 첫 저장(1) 값을 불러오기

    #실제 계산
    try:    #문제가 발생하는지 검사
        answer = eval(formula, {"__builtins__": None}, {})  #eval에 formula 문자열 수식을 넣어 계산된 값을 결과 변수 answer에 대입, 불필요한 명령어 호출을 방지({"__builtins__": None}). (eval은 다른 명령어도 실행할 수 있기 때문)

        if answer % 1 == 0: answer = int(answer)    #결과값이 .0형태의 실수라면 정수로 변환

        return answer   #답 answer를 return
    
    except: return "계산 중 문제가 발생했습니다. (예: 어떤 수를 0으로 나누려는 경우)"  #계산 문제 발생시, 오류 메시지 return