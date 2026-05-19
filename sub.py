def sub(nums):  #매개변수 nums의 원소들을 빼는 함수 (str 형태의 리스트를 입력받아야 함)
    if("." in nums[0]):  #첫 번째 원소에 .(소수점)이 있다면
        total_nums = float(nums[0])  #최종값 정의 (첫 번째 원소를 실수형으로 변환)
    else:
        total_nums = int(nums[0])  #최종값 정의 (첫 번째 원소를 정수형으로 변환)

    for n in nums[1:]:  #nums 의 각각의 원소들을 순서대로 n에 넣어서 실행 (첫 번째 원소 제외)
        if("." in n): total_nums -= float(n)    #n에 .(소수점)이 있다면 n을 실수형으로 변환한 뒤에 total_nums에서 빼기
        else: total_nums -= int(n)    #아니라면 n을 정수형으로 변환하여 total_nums에서 빼기
    return total_nums    #total_nums 출력(리턴)