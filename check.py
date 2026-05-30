checklist = {}

def get_user_list(user_id):
    if user_id not in checklist:
        checklist[user_id] = []
    return checklist[user_id]

def add(user_id, item):
    user_list = get_user_list(user_id)
    user_list.append({"task": item, "done": False})
    return f"✅ 추가됨: {item}"

def show(user_id):
    user_list = get_user_list(user_id)

    if not user_list:
        return "📋 체크리스트가 비어있습니다."

    msg = "📋 체크리스트\n"
    for i, item in enumerate(user_list, 1):
        status = "✅" if item["done"] else "❌"
        msg += f"{i}. {status} {item['task']}\n"

    return msg

def done(user_id, index):
    user_list = get_user_list(user_id)

    if 0 < index <= len(user_list):
        user_list[index - 1]["done"] = True
        return f"✅ 완료: {user_list[index - 1]['task']}"
    return "❌ 번호 오류"

def remove(user_id, index):
    user_list = get_user_list(user_id)

    if 0 < index <= len(user_list):
        removed = user_list.pop(index - 1)
        return f"🗑 삭제: {removed['task']}"
    return "❌ 번호 오류"