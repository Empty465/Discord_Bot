#모듈 불러오기
from asyncio import wait
import discord  #디스코드 라이브러리(모듈) 불러오기 (별도 설치 필요. README 참고 바람)
import sum  #sum.py 모듈 불러오기
import sub  #sub.py 모듈 불러오기
import calcul  #calcul.py 모듈 불러오기
import HourDB   #시수(Hour)DB 모듈 불러오기
import AttDB   #출석(Att)DB 모듈 불러오기
import check    #체크리스트 모듈 불러오기

#디스코드 채팅과 반응할 수 있도록 설정
intents = discord.Intents.all()
intents.message_content = True #봇이 모든 이벤트를 받을 수 있도록 설정 (메시지, 멤버, 반응 등)
client = discord.Client(intents=intents)    #디스코드 봇 클라이언트 생성

#DB들 우선 연결
HourDB
AttDB

#입력된 메시지에 따른 반응 출력
@client.event   #아래 함수를 디스코드 이벤트로 등록
async def on_message(message):  #메시지에 반응하는 함수 (매개변수는 message)
    
    if message.author == client.user:
        return

    #봇(자신 포함)의 메시지는 무시
    if message.author.bot: return

    #ㅋㅋ
    if message.content.startswith("ㅋㅋ") or message.content.endswith("ㅋ"):
        await message.channel.send("ㅋㅋㅋ")

    #엄준식
    if message.content == "엄": #'엄' 이라는 메시지를 받을 때.
        await message.channel.send("준식")  #'준식' 출력

    #!로 시작하는 명령어
    if message.content.startswith("!"):
        #사칙연산
        if message.content.startswith("!더하기"):   #!더하기 공백 후, 공백으로 구분된 숫자들을 받을 때
            parts = message.content.split() #공백으로 나뉜 수들을 각각 parts 리스트에 각 원소로 넣기
            sum2nums = parts[1:]    #!더하기가 있는 첫번째 원소들을 제외한 모든 원소를 sum2nums 리스트에 넣기
            await message.channel.send(sum.add(sum2nums))   #sum.py 모듈에 sum2nums 넣어 나온 'return' 값 출력
        elif message.content.startswith("!빼기"):   #!빼기 공백 후, 공백으로 구분된 숫자들을 받을 때
            parts = message.content.split() #공백으로 나뉜 수들을 각각 parts 리스트에 각 원소로 넣기
            sub2nums = parts[1:]    #!빼기가 있는 첫번째 원소들을 제외한 모든 원소를 sub2nums 리스트에 넣기
            await message.channel.send(sub.sub(sub2nums))   #sub.py 모듈에 sub2nums 넣어 나온 'return' 값 출력
        elif message.content.startswith("!계산"): #!계산 공백 후, 사칙연산 식을 받을 때
            formula = message.content[4:] #!계산 글자를 제외(4번째 글자 이전 글자들 제외)하고 남은 문자열을 그대로 formula에 대입
            await message.channel.send(calcul.calcul(formula)) #calcul.py 모듈에 formula을 넣어 나온 'return' 값 출력

        #시수
        elif message.content.startswith("!시수추가"):
            parts = message.content.split() #뒤에 들어오는 메시지(공백으로 구분)하여 parts 리스트에 추가
            name = parts[1] #두번째(첫번째는 명령어)를 name 변수에 대입
            time = float(parts[2])  #세번째를 time 변수에 대입
            await message.channel.send(HourDB.add_hour(name, time)) #시수추가 함수(add_hour)에 두 값을 넣고 결과 출력
        elif message.content.startswith("!시수차감"):
            parts = message.content.split() #뒤에 들어오는 메시지(공백으로 구분)하여 parts 리스트에 추가
            name = parts[1] #두번째(첫번째는 명령어)를 name 변수에 대입
            time = float(parts[2])  #세번째를 time 변수에 대입
            await message.channel.send(HourDB.sub_hour(name, time)) #시수차감 함수(sub_hour)에 두 값을 넣고 결과 출력
        elif message.content.startswith("!시수수정"):  
            parts = message.content.split() #뒤에 들어오는 메시지(공백으로 구분)하여 parts 리스트에 추가
            name = parts[1] #두번째(첫번째는 명령어)를 name 변수에 대입
            time = float(parts[2])  #세번째를 time 변수에 대입
            await message.channel.send(HourDB.edit_hour(name, time))    #시수수정 함수(edit_hour)에 두 값을 넣고 결과 출력    
        elif message.content.startswith("!시수제거"):
            parts = message.content.split() #뒤에 들어오는 메시지(공백으로 구분)하여 parts 리스트에 추가
            name = parts[1] #두번째(첫번째는 명령어)를 name 변수에 대입
            await message.channel.send(HourDB.del_hour(name))   #시수제거 함수(del_hour)에 값을 넣고 결과 출력
        elif message.content.startswith("!시수"):
            parts = message.content.split() #뒤에 들어오는 메시지(공백으로 구분)하여 parts 리스트에 추가
            name = parts[1] #두번째(첫번째는 명령어)를 name 변수에 대입
            await message.channel.send(HourDB.find_hour(name))  #시수찾기 함수(find_hour)에 값을 넣고 결과 출력

        #출석
        elif message.content.startswith("!출석조회"):
            parts = message.content.split() #뒤에 들어오는 메시지를 공백을 기준으로 나누어 parts리스트에 넣기
            if len(parts) == 1: user = message.author.id    #parts에 명령어만 들어왔다면 명령어 작성자 id를 user에 넣기
            else: user = parts[1]   #아니면 명령어 다음 원소(두번째 원소)를 user에 넣기
            await message.channel.send(AttDB.attendance_check(user))    #출석조회 함수(attendance_check)에 user를 넣어 결과값을 대답으로 출력
        elif message.content.startswith("!출석순위"):
            await message.channel.send(AttDB.attendance_rank(message.author.id))    #출석순위 함수(attendance_rank)에 명령어 작성자 id를 넣고 결과값을 대답으로 출력
        elif message.content.startswith("!출석"):
            await message.channel.send(AttDB.attendance(message.author.id, message.author.display_name))    #출석 함수(attendance)에 명령어 작성자 id와 표시 이름을 넣어 결과값을 대답으로 출력

        # 체크리스트
        elif message.content.startswith("!추가"):
            parts = message.content.split(maxsplit=1)

            if len(parts) < 2:
                await message.channel.send("❌ 내용을 입력하세요")
                return

            item = parts[1]
            await message.channel.send(check.add(message.author.id, item))
        elif message.content == "!목록":
            await message.channel.send(check.show(message.author.id))
        elif message.content.startswith("!완료"):
            parts = message.content.split()

            if len(parts) < 2 or not parts[1].isdigit():
                await message.channel.send("❌ 번호 입력")
                return

            index = int(parts[1])
            await message.channel.send(check.done(message.author.id, index))
        elif message.content.startswith("!삭제"):
            parts = message.content.split()

            if len(parts) < 2 or not parts[1].isdigit():
                await message.channel.send("❌ 번호 입력")
                return

            index = int(parts[1])
            await message.channel.send(check.remove(message.author.id, index))

        #도움말
        elif message.content.startswith("!도움"):
            await message.channel.send("아래는 입력 가능한 명령어와 설명 입니다." \
            "\n[사칙연산]" \
            "\n!더하기 숫자1 숫자2 숫자n   : 해당 숫자들을 더합니다." \
            "\n!빼기 숫자1 숫자2 숫자n  : 해당 숫자들을 뺍니다." \
            "\n!계산 (사칙연산식) : 입력받은 식을 계산합니다." \
            "\n\n[시수]" \
            "\n!시수 이름(또는 시간)   : 해당 이름의 대상의 시간을 출력합니다.(시간이 입력되면 해당 시간의 이름들을 출력합니다)" \
            "\n!시수추가 이름 숫자 : 해당 이름의 대상의 시간을 추가하여 기록합니다." \
            "\n!시수차감 이름 숫자   : 해당 이름의 대상의 시간을 차감하여 기록합니다." \
            "\n!시수수정 이름 숫자   : 해당 이름의 대상의 시간을 수정하여 기록합니다." \
            "\n!시수제거 이름 : 해당 이름의 대상의 기록을 제거합니다." \
            "\n\n[출석]" \
            "\n!출석   : 출석합니다." \
            "\n!출석조회 (이름) : 본인의 출석 횟수를 출력합니다. (대상의 이름을 적을 시 대상의 출석 횟수를 출력합니다)" \
            "\n!출석순위   : 출석순위가 가장 높은 5명을 출력합니다.")
            
        #존재하지 않은 명령어
        else: await message.channel.send("존재하지 않는 명령어 입니다. !도움 을 입력하여 입력 가능한 명령어들을 확인하세요")

#원하는 봇 토큰을 token.txt파일을 만들어서 거기에 적으면 됨 (token.txt가 없다면 같은 파일에 새로 만들어 추가)
with open("token.txt", "r", encoding="utf-8") as f: #token.txt 파일을 읽기
    token = f.read().strip()    #token.txt 내용을 token변수에 넣기
client.run(token)  #봇 토큰을 넣고 실행