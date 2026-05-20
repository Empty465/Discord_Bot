import discord  #디스코드 라이브러리 불러오기   (bash 터미널에서 pip install discord.py 명령어로 디코 모듈 설치 필요)

import sum  #sum.py 모듈 불러오기
import sub  #sub.py 모듈 불러오기
import calcul  #calcul.py 모듈 불러오기

intents = discord.Intents.all() #봇이 모든 이벤트를 받을 수 있도록 설정 (메시지, 멤버, 반응 등)
client = discord.Client(intents=intents)    #디스코드 봇 클라이언트 생성

@client.event   #아래 함수를 디스코드 이벤트로 등록
async def on_message(message):  #메시지에 반응하는 함수 (매개변수는 message)
    if message.content == "엄": #'엄' 이라는 메시지를 받을 때.
        await message.channel.send("준식")  #'준식' 출력

    if message.content.startswith("!더하기"):   #'!더하기 공백 후, 공백으로 구분된 숫자들을 받을 때
        parts = message.content.split() #공백으로 나뉜 수들을 각각 parts 리스트에 각 원소로 넣기
        sum2nums = parts[1:]    #!더하기가 있는 첫번째 원소들을 제외한 모든 원소를 sum2nums 리스트에 넣기
        await message.channel.send(sum.add(sum2nums))   #sum.py 모듈에서 sum2nums 넣어 나온 'return' 값 출력

    if message.content.startswith("!빼기"):   #'!빼기 공백 후, 공백으로 구분된 숫자들을 받을 때
        parts = message.content.split() #공백으로 나뉜 수들을 각각 parts 리스트에 각 원소로 넣기
        sub2nums = parts[1:]    #!빼기가 있는 첫번째 원소들을 제외한 모든 원소를 sub2nums 리스트에 넣기
        await message.channel.send(sub.sub(sub2nums))   #sub.py 모듈에서 sub2nums 넣어 나온 'return' 값 출력

    if message.content.startswith("!계산"):
        parts = list(message.content)   #받은 명령어를 한글자씩 원소화하여 parts 리스트에 넣음 (예: 12+3을 "1","2","+","3"로 변환)
        formula = parts[4:] #!계산 (공백 포함) 4글자(원소)를 제외하고 남은 원소들을 그대로 formula에 대입
        await message.channel.send(calcul.calcul(formula)) #calcul.py 모듈에서 formula을 넣어 나온 'return' 값 출력

#원하는 봇 토큰을 token.txt파일을 만들어서 거기에 적으면 됨 (token.txt가 없다면 같은 파일에 새로 만들어 추가)
with open("token.txt", "r", encoding="utf-8") as f: #token.txt 파일을 읽기
    token = f.read().strip()    #token.txt 내용을 token변수에 넣기
client.run(token)  #봇 토큰을 넣고 실행