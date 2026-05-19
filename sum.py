def add(nums):  #매개변수 nums의 원소들을 더하는 함수
    total_nums = 0  #최종값 정의
    for n in nums:  #nums 의 각각의 원소들을 순서대로 n에 넣어서 실행
        if("." in n): total_nums += float(n)    #n에 .(소수점)이 있다면 n을 실수형으로 변환한 뒤에 total_nums에 더하기
        else: total_nums += int(n)    #아니라면 n을 정수형으로 변환하여 total_nums에 더하기
    return total_nums    #total_nums 출력(리턴)