import sqlite3
from datetime import date

con_att = sqlite3.connect("attendance.db")
curA = con_att.cursor()

curA.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    user_id INTEGER,
    user_name TEXT,
    count INTEGER,
    last_date TEXT
)
""")

con_att.commit()
def attendance(user_id, user_name):
    today = str(date.today())

    curA.execute(
        "SELECT count, last_date FROM attendance WHERE user_id=?",
        (user_id,)
    )
    result = curA.fetchone()

    if not result:
        curA.execute(
            "INSERT INTO attendance VALUES (?, ?, ?, ?)",
            (user_id, user_name, 1, today)
        )
        con_att.commit()

        return f"{user_name}님의 첫 출석 입니다! (총 출석 횟수: 1회)"
    
    elif result[1] == today:
        return f"{user_name}님은 이미 오늘 출석하였습니다. 다음날 00시에 다시 시도하세요."
    
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

        user_id = int(user)

        curA.execute(
            "SELECT user_name, count FROM attendance WHERE user_id=?",
            (user_id,)
        )

        result = curA.fetchone()

    #문자열이면 이름 조회
    except:

        curA.execute(
            "SELECT user_name, count FROM attendance WHERE user_name=?",
            (user,)
        )

        result = curA.fetchone()

    #없는 유저
    if not result:

        return f"해당 이름의 출석 기록이 없습니다."

    #있는 유저
    else:

        return f"{result[0]}님의 총 출석 횟수는 {result[1]}회 입니다."
    
def attendance_rank(user_id):
    curA.execute("""
        SELECT user_id, user_name, count
        FROM attendance
        ORDER BY count DESC
        LIMIT 5
    """)
    top5 = curA.fetchall()

    msg = "=== 출석 순위 TOP 5 ===\n"

    for i, row in enumerate(top5, start=1):
        msg += f"{i}위 - {row[1]} ({row[2]}회)\n"
    
    curA.execute("""
        SELECT user_id, user_name, count
        FROM attendance
        ORDER BY count DESC
    """)
    all_users = curA.fetchall()

    my_rank = None

    for i, row in enumerate(all_users, start=1):
        if row[0] == user_id:
            my_rank = i
            my_name = row[1]
            my_count = row[2]

            break
    
    if my_rank and my_rank > 5:
        msg += f"\n=== 내 순위 ===\n{my_rank}위 - {my_name} ({my_count}회)"

    return msg