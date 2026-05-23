#데이터 저장을 위해 sqlite3 호출
import sqlite3  

#hours.db 불러오기
con_hour = sqlite3.connect("hours.db")   #hours.db 연결 (없으면 생성)
curH = con_hour.cursor() #hour.db 수정권한 지정

#hours.db가 최초 생성된거라면 양식 검사 후, 없다면 양식 추가
curH.execute("""   
    CREATE TABLE IF NOT EXISTS hours(
        user TEXT,
        time REAL
    )
    """)    ##user=문자열 , time=실수 형태의 목록 추가 (이미 있다면 실행하지 않음)
con_hour.commit()   #저장

#시수 추가
def add_hour(name, time):   #name(str), time(float) 매개변수를 hours.db에 추가하는 함수
    #받은 이름이 DB에 있는지 판별
    curH.execute(   
        "SELECT time FROM hours WHERE user=?",
        (name,)
    )
    result = curH.fetchone()    #결과값을 result에 넣기

    #기존에 있는 이름이라면
    if result:
        new_time = result[0] + time #기존 시간에 입력된 시간 추가하여 new_time 변수 추가
        curH.execute(   #해당 이름에 new_time값을 time에 넣기
            "UPDATE hours SET time=? WHERE user=?",
            (new_time, name)
        )
        con_hour.commit()   #저장
        return(f"추가 완료 되었습니다.\n{name}의 시수에 {time}만큼 추가하여 {new_time}시간이 되었습니다.") #완료 출력 return
    
    #기존에 있는 이름이 아니라면
    else:
        curH.execute(
            "INSERT INTO hours VALUES (?, ?)",
            (name, time)
        )   #name, time 변수를 hours에 넣기
        con_hour.commit()   #저장
        return(f"추가 완료 되었습니다.\n{name}은(는) 없던 사람이므로 {time}시간과 함께 추가되었습니다.") #완료 출력 return

#시수 차감
def sub_hour(name, time):
    #받은 이름이 있는지 판별
    curH.execute(
        "SELECT time FROM hours WHERE user=?",
        (name,)
    )
    result = curH.fetchone()    #결과값 result에 대입

    #없다면 없다고 출력 return
    if not result: return f"{name}은(는) 기록되어있지 않습니다."

    #기존 이름이 있다면
    old_time = result[0]    #옛 시간을 입력
    new_time = old_time - time  #옛 시간에 입력된 시간을 빼서 new_time에 넣기

    #기존 시간이 입력받은 시간보다 작다면 안된다고 출력 return
    if new_time < 0: return f"{old_time}에서 해당 값을 뺴면 0이하로 내려가기에 뺄 수 없습니다."

    #기존 시간이 입력받은 시간보다 크다면
    else:
        #계산된 시간(new_time)을 해당 이름의 time으로 수정하기
        curH.execute(
            "UPDATE hours SET time=? WHERE user=?",
            (new_time, name)
        )
        con_hour.commit()   #저장
        return f"{name}의 시수에 {time}만큼 차감하여 {new_time}시간이 되었습니다."  #완료 출력 return

#시수 수정
def edit_hour(name, time):
    #기존에 있는 이름인지 판별
    curH.execute(
        "SELECT time FROM hours WHERE user=?",
        (name,)
    )
    result = curH.fetchone()    #결과값을 result에 넣기

    #기존에 없는 이름이면 출력 return
    if not result: return f"{name}은(는) 기록되어있지 않습니다."    

    #기존에 있는 이름이면 해당 이름에 time값을 넣어 출력
    curH.execute(
        "UPDATE hours SET time=? WHERE user=?",
        (time, name)
    )
    con_hour.commit()   #저장
    return f"{name}의 시수를 {time}시간으로 수정하였습니다."    #완료 출력 return

#시수 제거
def del_hour(name):
    #기존에 있는 이름인지 판별
    curH.execute(
        "SELECT time FROM hours WHERE user=?",
        (name,)
    )
    result = curH.fetchone()    #결과값을 result에 넣기

    #기존에 없는 이름이면 출력 return
    if not result: return f"{name}은(는) 원래 기록되어있지 않습니다."

    #기존에 있는 이름이면 해당 이름의 항목 제거
    curH.execute(
        "DELETE FROM hours WHERE user=?",
        (name,)
    )  
    con_hour.commit()   #저장
    return f"{name}을(를) 시수 목록에서 제거하였습니다."    #완료 출력 return

#시수 찾기
def find_hour(name):
    #받은 값이 시간이면
    try:    #아래 명령어들을 실행해본다
        name = float(name)  #값을 실수 형태로 변경한다(이름같이 문자열이면 오류로 인해 except로 넘어감)

        #해당 시간(name)과 일치하는 이름들을 찾는다
        curH.execute(
            "SELECT user FROM hours WHERE time=?",
            (name,)
        )
        result = curH.fetchall()    #결과값을 result에 넣는다
        names = []  #출력을 위한 names 리스트 생성

        for row in result:  #result의 값을들 row에 차례대로 넣으면서 반복
            names.append(row[0])    #names 리스트에 순서대로 값들을 넣는다

        #입력되는 이름이 없으면 없다고 return
        if not result: return f"{name}시간의 시수가 기록된 이는 없습니다."

        #있다면 names를 포함한 결과 return
        else: return f"{name}시간 만큼의 시수인 사람들은 {names}가 있습니다."

    #받은 값이 이름이면
    except ValueError: #name = float(name)이 실패하면 실행
        #해당 이름을 찾고 시간을 찾는다
        curH.execute(
            "SELECT SUM(time) FROM hours WHERE user=?",
            (name,)
        )
        result = curH.fetchone()    #결과값을 result에 넣는다

        #입력되는 이름이 없으면 없다고 return
        if result[0]==None: return f"{name}은(는) 기록되어 있지 않습니다."

        #있다면 결과 return
        else: return f"{name}의 시수는 {result[0]}시간 입니다."