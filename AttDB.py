#필요한 모듈 호출
import sqlite3  #.db를 위해 sqlite3 호출
from datetime import date   #출석 일자를 기록하기 위해 datetime의 date 클래스 호출

#attendance.db 불러오기
con_att = sqlite3.connect("DB/attendance.db")  #attendance.db 불러와 con_att로 지정 (없으면 생성)
curA = con_att.cursor() #con_att에 수정권한을 curA로 지정

#최초생성된 attendane.db라면 해당 양식 입력
curA.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    user_id INTEGER,
    user_name TEXT,
    count INTEGER,
    last_date TEXT
)
""")
con_att.commit()    #양식 추가 후 저장

#출석
def attendance(user_id, user_name): #받은 값들을 매개변수 user_id, user_name에 넣는 함수
    today = str(date.today())   #오늘 일자를 today 함수에 넣기

    #기존에 있는 id인지 판별후, 결과를 result에 넣기
    curA.execute(
        "SELECT count, last_date FROM attendance WHERE user_id=?",
        (user_id,)
    )
    result = curA.fetchone()

    #기존에 없는 id면 새로 기록하고, 첫 출석 메시지 리턴
    if not result:
        curA.execute(
            "INSERT INTO attendance VALUES (?, ?, ?, ?)",
            (user_id, user_name, 1, today)
        )
        con_att.commit()
        return f"{user_name}님의 첫 출석 입니다! (총 출석 횟수: 1회)"
    
    #이미 오늘 출석한 id면 안내 메시지 리턴
    elif result[1] == today:
        return f"{user_name}님은 이미 오늘 출석하였습니다. 다음날 00시에 다시 시도하세요."
    
    #기존에 있는 id고 오늘 출석하지 않았다면 출석 점수 갱신 및 출석 완료 메시지 출력
    else:
        new_count = result[0] + 1

        curA.execute(
            "UPDATE attendance SET count=?, last_date=?, user_name=? WHERE user_id=?",
            (new_count, today, user_name, user_id)
        )
        con_att.commit()

        return f"{user_name}님 출석 완료! (총 출석 횟수: {new_count}회)"
    
def attendance_check(user):
    #숫자로 변환 가능하면 ID 조회
    try:
        user_id = int(user) #id 형태(숫자)라면 user_id 변수에 넣기

        #기존에 있는 id면 결과값을 result에 넣기
        curA.execute(
            "SELECT user_name, count FROM attendance WHERE user_id=?",
            (user_id,)
        )
        result = curA.fetchone()

    #문자열이면 이름을 조회
    except:
        #user(표시 이름)을 찾고, 기존에 있다면 result에 넣기
        curA.execute(
            "SELECT user_name, count FROM attendance WHERE user_name=?",
            (user,)
        )
        result = curA.fetchone()

    #없는 유저라면 알림 메시지 출력
    if not result: return f"해당 이름의 출석 기록이 없습니다."

    #기존에 있는 유저면 해당 유저의 이름과 result(출석 횟수)를 return
    else: return f"{result[0]}님의 총 출석 횟수는 {result[1]}회 입니다."

#출석순위
def attendance_rank(user_id):
    #출석 점수가 가장 높은 이들 5을 top5 리스트에 넣기
    curA.execute("""
        SELECT user_id, user_name, count
        FROM attendance
        ORDER BY count DESC
        LIMIT 5
    """)
    top5 = curA.fetchall()

    #리턴할 메시지의 첫째줄 지정
    msg = "=== 출석 순위 TOP 5 ===\n"

    #리턴할 메시지의 첫쨰줄 다음에 들어갈 줄에 순위 및 이름, 출석 횟수를 반복하여 추가 (1~5위)
    for i, row in enumerate(top5, start=1):
        msg += f"{i}위 - {row[1]} ({row[2]}회)\n"
    
    #모든 출석 기록이 있는 인원들의 수를 all_users 변수에 넣기
    curA.execute("""
        SELECT user_id, user_name, count
        FROM attendance
        ORDER BY count DESC
    """)
    all_users = curA.fetchall()

    #명령어 작성자의 랭킹을 일단 my_rank로 지정하기 위해 초기화
    my_rank = None

    #명령어 작성자의 순위 및 이름, 출석 횟수를 찾고 기록
    for i, row in enumerate(all_users, start=1):
        if row[0] == user_id:
            my_rank = i
            my_name = row[1]
            my_count = row[2]
            break
    
    #만약 명령어 작성자의 순위가 5위 밖이라면 작성자의 정보도 함께 메시지에 넣기
    if my_rank and my_rank > 5:
        msg += f"\n=== 내 순위 ===\n{my_rank}위 - {my_name} ({my_count}회)"

    #최종값 메시지 리턴
    return msg