css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}

.stTextInput {
      position: fixed;
      bottom: 3rem;
    }
'''


user_template = """
<div style="background-color: #007bff; color: #fff; padding: 8px; border-radius: 8px; margin-bottom: 8px; max-width: 60%;">
    <p style="font-size: 14px; margin: 0;">{{MSG}}</p>
</div>
"""

bot_template = """
<div style="background-color: #f3f3f3; color: #000; padding: 8px; border-radius: 8px; margin-bottom: 8px; max-width: 60%;">
    <p style="font-size: 14px; margin: 0;">{{MSG}}</p>
</div>
"""