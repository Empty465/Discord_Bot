import discord  #디스코드 라이브러리 불러오기

import sum  #sum.py 모듈 불러오기
import sub  #sub.py 모듈 불러오기

intents = discord.Intents.all() #봇이 모든 이벤트를 받을 수 있도록 설정 (메시지, 멤버, 반응 등)
client = discord.Client(intents=intents)    #디스코드 봇 클라이언트 생성

@client.event   #아래 함수를 디스코드 이벤트로 등록
async def on_message(message):  #메시지에 반응하는 함수 (매개변수는 message)
    if message.content == "엄": #'엄' 이라는 메시지를 받을 때.
        await message.channel.send("준식")  #'준식' 출력

    if message.content.startswith("!더하기"):   #'!더하기 a b' 를 입력받을 때
        parts = message.content.split() #!더하기 뒤에 온 두 수를 공백을 기준으로 각각 쪼개기
        a = int(parts[1])   #첫번째 숫자를 정수형으로 변환한 뒤에 a변수에 넣기
        b = int(parts[2])   #두번쨰 수는 정수형으로 변환한 뒤에 b변수에 넣기
        await message.channel.send(sum.add(a, b))   #sum.py 모듈에서 a와 b를 넣어 나온 'return' 값 출력

    if message.content.startswith("!빼기"):   #'!빼기 a b' 를 입력받을 때
        parts = message.content.split() #!빼기 뒤에 온 두 수를 공백을 기준으로 각각 쪼개기
        a = int(parts[1])   #첫번째 숫자를 정수형으로 변환한 뒤에 a변수에 넣기
        b = int(parts[2])   #두번쨰 수는 정수형으로 변환한 뒤에 b변수에 넣기
        await message.channel.send(sub.sub(a, b))   #sub.py 모듈에서 a와 b를 넣어 나온 'return' 값 출력

client.run(" ")  #봇 토큰