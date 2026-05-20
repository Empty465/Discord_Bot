#매개변수 nums의 원소들을 빼는 함수 (str 형태의 리스트를 입력받아야 함)
def sub(nums):  

    #실수 또는 정수로 변환
    if("." in nums[0]): total_nums = float(nums[0])  #첫번째 num 원소가 소수점이 있으면, 첫 수(최종값)를 실수형으로 변형뒤, 값 대입
    else: total_nums = int(nums[0])  #아니면 정수값 대입

    #각 수를 빼서 최종값에 넣기
    for n in nums[1:]:  #nums 의 각각의 원소들을 순서대로 n에 넣어서 실행 (첫 번째 원소 제외)
        if("." in n): total_nums -= float(n)    #n에 .(소수점)이 있다면 n을 실수형으로 변환한 뒤에 total_nums에서 빼기
        else: total_nums -= int(n)    #아니라면 n을 정수형으로 변환하여 total_nums에서 빼기
        
    return total_nums    #total_nums 출력(리턴)