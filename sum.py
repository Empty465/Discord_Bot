def add(nums):  #매개변수 nums의 원소(항)들을 더하는 함수 (str 형태의 리스트를 입력받아야 함)
    total_nums = 0  #최종값 정의

    #각 항들을 계산
    for n in nums:  #nums 의 각각의 원소들을 순서대로 n에 넣어서 실행

        #항 내부의 곱셈 실행
        if "·" in n: n = n.replace("·", "*")    #gpt같은 애들이 곱셈 부호라고 던져주는 ·를 *로 변환
        if "*" in n:    #곱셈 부호(*)가 포함된 경우
            a, b = n.split("*") #항의 부호(*)를 기준으로 나누어 a, b 변수에 각각 대입
            
            if "." in a or "." in b: n = float(a) * float(b)    #a또는 b에 소수점(.)이 있으면 실수로 변환하고 곱하기
            else: n = int(a) * int(b)   #소수점이 없으면 정수로 변환하고 곱하기

        #항 내부의 나눗셈 실행
        elif "/" in n:  #나누기 부호(/)가 포함된 경우
            a, b = n.split("/") #항(n)의 값을 /을 기준으로 나누어 a, b에 각각 대입
            n = float(a) / float(b) #a,b를 실수로 변환하고 나눈 값을 n에 대입
            if(float(a)%float(b)==0): n = int(n)    #a/b의 나머지가 없을 경우(.0) n을 인트로 변환

        #부호가 없는 항이면
        else:
            if "." in n: n = float(n)   #소수점이 있는 항이면 실수로 변환
            else: n = int(n)    #소수점이 없으면 정수로 변환

        #항들 더하기
        total_nums += n #최종값에 항들을 더하기

    return total_nums    #total_nums 출력(리턴)