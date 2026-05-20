def add(nums):  #매개변수 nums의 원소들을 더하는 함수 (str 형태의 리스트를 입력받아야 함)
    total_nums = 0  #최종값 정의

    #각 항들을 계산
    for n in nums:  #nums 의 각각의 원소들을 순서대로 n에 넣어서 실행
        if "." in n: n = float(n)   #소수점이 있는 항이면 실수로 변환
        else: n = int(n)    #소수점이 없으면 정수로 변환

        #항들 더하기
        total_nums += n #최종값에 항들을 더하기

    return total_nums    #total_nums 출력(리턴)