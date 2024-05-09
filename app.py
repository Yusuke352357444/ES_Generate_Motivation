import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
import google.generativeai as genai

# APIキーの設定
api_key = st.secrets["gemini_api_key"]
genai.configure(api_key=api_key)

# モデルの設定
model = genai.GenerativeModel('gemini-pro')

# タイトル
st.title('志望動機ジェネレータ')

# ユーザー入力
industry_or_occupation = st.text_input("志望する業界または業種を教えてください。　例ー広告業界、営業、事務（任意）")
mbti_result = st.text_input("MBTI診断結果を教えてください。　例ーISFJ、ESFP（任意）")
industry_motivation = st.text_input("志望動機を教えてください。（必須）")
strengths_and_abilities= st.text_input("あなたの強みを教えてください。（必須）")
experiences = st.text_input("その志望先を目指すようになったきっかけを教えてください。（必須）")

if st.button('自己PRを生成'):
    # テキスト生成
    pr_template = """以下はESに書く志望動機を作成してもらう為の情報です。{industry}と{mbti}タイプの性格特性の業界や業種と性格特性は志望動機には書かず、精度の高い志望動機を作るのに活用してください。私が志望する理由は{motivation}だからです。{experiences}という経験から{industry}に興味を持ちました。私は{strengths}という強みを活かした働き方をして貴社で活躍したいと考えています。。私のスキルと経験が貴社の要求にどのようにマッチするかを詳しく説明した志望動機を作成してください。"""

    question_text = pr_template.format(
        industry=industry_or_occupation,
        mbti=mbti_result,
        strengths=strengths_and_abilities,
        motivation=industry_motivation,
        experiences=experiences
    )

    response = model.generate_content(question_text)
    st.write("作成された志望動機:", response.text)
