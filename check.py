import json
import os

DB_DIR = "DB"
DATA_FILE = os.path.join(DB_DIR, "checklist.json")

# 파일 로드
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


# 파일 저장
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

checklist = load_data()

def get_user_list(user_id):
    user_id = str(user_id)

    if user_id not in checklist:
        checklist[user_id] = []
    return checklist[user_id]

# ✅ 추가
def add(user_id, item):
    user_list = get_user_list(user_id)
    user_list.append({"task": item, "done": False})
    save_data(checklist)
    return f"✅ 추가됨: {item}"

# ✅ 목록
def show(user_id):
    user_list = get_user_list(user_id)

    if not user_list:
        return "📋 체크리스트가 비어있습니다."

    msg = "📋 체크리스트\n"
    for i, item in enumerate(user_list, 1):
        status = "✅" if item["done"] else "❌"
        msg += f"{i}. {status} {item['task']}\n"

    return msg

# ✅ 완료
def done(user_id, index):
    user_list = get_user_list(user_id)

    if 0 < index <= len(user_list):
        user_list[index - 1]["done"] = True
        save_data(checklist)
        return f"✅ 완료: {user_list[index - 1]['task']}"

    return "❌ 번호 오류"

# ✅ 삭제
def remove(user_id, index):
    user_list = get_user_list(user_id)

    if 0 < index <= len(user_list):
        removed = user_list.pop(index - 1)
        save_data(checklist)
        return f"🗑 삭제: {removed['task']}"

    return "❌ 번호 오류"
