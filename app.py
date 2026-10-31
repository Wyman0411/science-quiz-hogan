import streamlit as st

# 網頁標題與設定
st.set_page_config(page_title="小五自然科挑戰", page_icon="🌟")
st.title("🌟 小五自然科挑戰：太陽與植物的秘密")
st.write("各位同學好！請仔細閱讀題目，選出或填入正確答案，最後點擊最下方的「交卷」來看成績喔！")

# 題目資料庫 (這裡示範幾題，你可以將前面的題目依此格式貼上)
mcq_questions = [
    {
        "question": "1. 小華在下午兩點時測量太陽的位置，請問此時他的影子最有可能朝向哪一個方位？",
        "options": ["(A) 東偏南", "(B) 東偏北", "(C) 西偏南", "(D) 西偏北"],
        "answer": "(B) 東偏北",
        "explanation": "下午兩點太陽在西偏南，影子方向與太陽相反，所以朝向東偏北。"
    },
    {
        "question": "2. 下列哪一種現象與「地球自轉」直接相關？",
        "options": ["(A) 四季溫度的變化", "(B) 一天之中太陽東升西落", "(C) 夏天和冬天的太陽高度角不同", "(D) 每年夏至的日照時間比冬至長"],
        "answer": "(B) 一天之中太陽東升西落",
        "explanation": "地球自轉一圈是一天，這讓我們看到太陽東升西落。"
    }
]

fill_questions = [
    {
        "question": "1. 有些植物的葉脈像網子一樣交錯，我們稱它為「____脈」。",
        "answer": "網狀",
        "explanation": "像網子交錯的葉脈稱為網狀脈，通常配有主根的軸根。"
    }
]

# 建立測驗表單
with st.form("quiz_form"):
    st.subheader("📝 第一部分：選擇題")
    mcq_user_answers = []
    for i, q in enumerate(mcq_questions):
        ans = st.radio(q["question"], q["options"], index=None, key=f"mcq_{i}")
        mcq_user_answers.append(ans)
        st.write("---")

    st.subheader("📝 第二部分：填空題")
    fill_user_answers = []
    for i, q in enumerate(fill_questions):
        ans = st.text_input(q["question"], key=f"fill_{i}")
        fill_user_answers.append(ans)
        st.write("---")

    submitted = st.form_submit_button("✅ 交卷看成績")

# 評分與解答邏輯
if submitted:
    score = 0
    total_questions = len(mcq_questions) + len(fill_questions)
    
    st.header("📊 你的測驗結果")
    
    # 批改選擇題
    for i, q in enumerate(mcq_questions):
        if mcq_user_answers[i] == q["answer"]:
            score += 1
            st.success(f"✅ {q['question']} \n\n **答對了！** 解析：{q['explanation']}")
        else:
            st.error(f"❌ {q['question']} \n\n **正確答案是：{q['answer']}** \n\n 解析：{q['explanation']}")
            
    # 批改填空題
    for i, q in enumerate(fill_questions):
        # 移除空白以防學生多打空格
        user_ans = fill_user_answers[i].strip() if fill_user_answers[i] else ""
        if user_ans == q["answer"]:
            score += 1
            st.success(f"✅ {q['question']} \n\n **答對了！** 解析：{q['explanation']}")
        else:
            st.error(f"❌ {q['question']} \n\n **正確答案是：{q['answer']}** \n\n 解析：{q['explanation']}")

    # 顯示總分與特效
    final_score = int((score / total_questions) * 100)
    st.metric(label="總分", value=f"{final_score} 分")
    
    if final_score == 100:
        st.balloons()
        st.success("太厲害了！你是自然科小達人！")
    elif final_score >= 60:
        st.info("表現不錯喔！把錯的題目再複習一下就完美了！")
    else:
        st.warning("沒關係，這只是練習！看看下方的解析，弄懂核心觀念最重要！")