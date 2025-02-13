from app import app
from app.chatbot import ask, append_interaction_to_chat_log
from app.forms import ChatForm
from app.conversation import GPTConversation, init_prompt

from flask import Flask, request, session, jsonify, render_template, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
# import run_with_ngrok from flask_ngrok to run the app using ngrok
# from flask_ngrok import run_with_ngrok

from datetime import datetime, timezone

import sqlite3


# run_with_ngrok(app)

USER = "Person"
CHATBOT = "AI"
WARNING = "warning"
END = "end"
NOTI = "notification"

conversation = [
    {
        "from": CHATBOT,
        "to": WARNING,
        "message": "The following is a conversation with a therapist. The therapist is helpful, creative, empathetic, and very friendly.",
        "send_time": datetime(2022, 6, 20, 0, 0, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": NOTI,
        "message": "Yesterday",
        "send_time": datetime(2022, 6, 20, 0, 0, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "Hello, who are you?",
        "send_time": datetime(2022, 6, 20, 0, 0, 1, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I am an AI created by OpenAI. How can I help you today?",
        "send_time": datetime(2022, 6, 20, 0, 1, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "I need help.",
        "send_time": datetime(2022, 6, 20, 0, 2, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I'm sorry to hear that. What's going on?",
        "send_time": datetime(2022, 6, 20, 0, 3, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": NOTI,
        "message": "Today",
        "send_time": datetime(2022, 6, 20, 0, 4, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "I had an argument with my family today.",
        "send_time": datetime(2022, 6, 20, 0, 4, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I'm sorry to hear that. Can you tell me more about what happened?",
        "send_time": datetime(2022, 6, 20, 0, 5, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "I told my mom that I want to buy a computer but she was very upset about that.",
        "send_time": datetime(2022, 6, 20, 0, 6, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I'm sorry to hear that she was upset. Can you tell me more about why you want to buy a computer?",
        "send_time": datetime(2022, 6, 20, 0, 7, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "I told her that I need a computer to complete my assignment.",
        "send_time": datetime(2022, 6, 20, 0, 8, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I see. And she was upset because she doesn't think you need a computer for that?",
        "send_time": datetime(2022, 6, 20, 0, 9, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "No, she doesn't 😥.",
        "send_time": datetime(2022, 6, 20, 0, 10, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "I'm sorry to hear that. Can you tell me more about your assignment? Maybe there's a way to do it without a computer.",
        "send_time": datetime(2022, 6, 20, 0, 11, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": USER,
        "to": CHATBOT,
        "message": "There is NO WAY to finish that assignment without a computer. Why didn't she understand that??? 😡",
        "send_time": datetime(2022, 6, 20, 0, 12, 0, tzinfo=timezone.utc)
    }, 
    {
        "from": CHATBOT,
        "to": USER,
        "message": "It sounds like you're feeling frustrated because you feel like your mom doesn't understand your needs. Can you tell me more about that?",
        "send_time": datetime(2022, 6, 20, 0, 13, 0, tzinfo=timezone.utc)
    },
    {
        "from": CHATBOT,
        "to": END,
        "message": "This conversation ended by the system.",
        "send_time": datetime(2022, 6, 20, 0, 14, 0, tzinfo=timezone.utc)
    }
]

# @app.route('/', methods=['GET', 'POST'])
@app.route('/conversation', methods=['GET', 'POST'])
def start_conversation():
    chat_log = session.get('chat_log')
    print("{} CONVO START {}".format("-"*12, "-"*12))
    print(f"chat_log::: {chat_log}")
    print(f"request.remote_addr::: {request.remote_addr}")
    
    if chat_log is None:
        arm_no = session.get("arm_no")
        if arm_no is None:
            select_prompt = init_prompt(random=True)
        else:
            select_prompt = init_prompt(arm_no=arm_no)
        session["chat_log"] = select_prompt["prompt"] + select_prompt["message_start"]
        session["chatbot"] = select_prompt["chatbot"]
        session["user"] = request.remote_addr
        session["start"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        
    convo = GPTConversation(session.get("user"), session.get("chatbot"), session.get("chat_log"))
    print(f"convo.chat_log::: {convo.chat_log}")
    print(f"convo.user::: {convo.user_name}")
    print(f"convo.chatbot::: {convo.chatbot_name}")
    print(f"convo.get_conversation()::: {convo.get_conversation()}")

    form = ChatForm()
    if form.validate_on_submit():
        print("{} NEW MESSAGE {}".format("-"*12, "-"*12))
        user_message = form.message.data
        answer = convo.ask(user_message)
        chat_log = convo.append_interaction_to_chat_log(user_message, answer)
        
        print(f"user_message::: {user_message}")
        print(f"answer::: {answer}")
        print(f"chat_log::: {chat_log}")
        
        session["chat_log"] = chat_log
        
        try:
            sqliteConnection = sqlite3.connect('/var/www/html/acaidb/database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            sqlite_insert_query = """INSERT INTO chats
                                  (user_id, chat_log) 
                                   VALUES 
                                  (?,?);"""
            param_tuple = (session["user"],session["chat_log"])
            count = cursor.execute(sqlite_insert_query,param_tuple)
            sqliteConnection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        
        return redirect(url_for('start_conversation'))
    
    print("{} RENDER WEBVIEW {}".format("-"*12, "-"*12))
    
    return render_template(
        '/dialogue/conversation_card.html', 
        user=convo.get_user(), 
        bot=convo.get_chatbot(), 
        warning=convo.WARNING, 
        end=convo.END,
        notification=convo.NOTI,
        conversation=convo.get_conversation(test=True),
        form=form
    )

@app.route('/qualtrics', methods=['GET', 'POST'])
def start_qualtrics_conversation():
    
    # TODO: First checking if user existed in database
    # TODO: [In Qualtrics] Second, check contextual variables in MOOClet Engine
    # TODO: [In Qualtrics] check if this user has an arm
    # TODO: [In Qualtrics] If user doesn't have an arm, run MOOClet Engine -> get one arm
    # TODO: arm -> get chat log : The following is a conversation with a friend. The friend is funny, shy, empathetic, and introverted.\n\nPerson: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?
    # TODO: chat log -> OpenAI API -> get the generated responses for the bot
    # TODO: chat log + genrated responses -> conversation
    # TODO: otherwise, get all conversation from the database
    # TODO: [NOT in this API] user can give us responses <- not from this API
    # TODO: [NOT in this API] storing/updating this conversation to database
    
    chat_log = session.get('chat_log')
    print("{} CONVO START {}".format("-"*12, "-"*12))
    print(f"chat_log::: {chat_log}")
    print(f"request.remote_addr::: {request.remote_addr}")
    
    if chat_log is None:
        arm_no = session.get("arm_no")
        if arm_no is None:
            select_prompt = init_prompt(random=True)
        else:
            select_prompt = init_prompt(arm_no=arm_no)
        session["chat_log"] = select_prompt["prompt"] + select_prompt["message_start"]
        session["chatbot"] = select_prompt["chatbot"]
        session["user"] = request.remote_addr
        session["start"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        
    convo = GPTConversation(session.get("user"), session.get("chatbot"), session.get("chat_log"))
    print(f"convo.chat_log::: {convo.chat_log}")
    print(f"convo.user::: {convo.user_name}")
    print(f"convo.chatbot::: {convo.chatbot_name}")
    print(f"convo.get_conversation()::: {convo.get_conversation()}")

    start = session.get('start')
    if start is None:
        session["start"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    stop = session.get('stop')
    if stop is None:
        session["stop"] = 5*60

    now = datetime.now()
    difference = now - datetime.strptime(session.get('start'), "%m/%d/%Y, %H:%M:%S")
    difference_seconds = difference.total_seconds()
    
    end = session.get('end')
    if end is None or not end:
        session["end"] = (difference_seconds >= session.get('stop'))
    
    print("start::: {}".format(session.get('start')))
    print("stop::: {}".format(session.get('stop')))
    print(f"difference_seconds::: {difference_seconds}")
    print("end::: {}".format(session.get('end')))

    form = ChatForm()
    if form.validate_on_submit() and not session.get('end'):
        print("{} NEW MESSAGE {}".format("-"*12, "-"*12))
        user_message = form.message.data
        answer = convo.ask(user_message)
        chat_log = convo.append_interaction_to_chat_log(user_message, answer)

        print(f"user_message::: {user_message}")
        print(f"answer::: {answer}")
        print(f"chat_log::: {chat_log}")

        session['chat_log'] = chat_log
        
        try:
            sqliteConnection = sqlite3.connect('/var/www/html/acaidb/database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            sqlite_insert_query = """INSERT INTO chats
                                  (user_id, chat_log) 
                                   VALUES 
                                  (?,?);"""
            param_tuple = (session["user"],session["chat_log"])
            count = cursor.execute(sqlite_insert_query,param_tuple)
            sqliteConnection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
        return redirect(url_for('start_qualtrics_conversation'))
    
    print("{} RENDER WEBVIEW {}".format("-"*12, "-"*12))
    
    return render_template(
        '/dialogue/qualtrics_card.html', 
        user=convo.get_user(), 
        bot=convo.get_chatbot(), 
        warning=convo.WARNING, 
        end=convo.END,
        notification=convo.NOTI,
        conversation=convo.get_conversation(end=session.get('end')),
        form=form
    )


@app.route('/chatsms', methods=['POST'])
def chatsms():
    incoming_msg = request.values['Body']
    print("request: ")
    print(request)
    print()

    print("incoming_msg: {}".format(incoming_msg))
    print()
    chat_log = session.get('chat_log')
    print("chat_log: {}".format(chat_log))
    print()

    answer = ask(incoming_msg, chat_log)
    print("answer: {}".format(answer))
    print()

    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,chat_log)
    
    msg = MessagingResponse()
    msg.message(answer)

    print("message: {}".format(msg))
    print()
    return str(msg)


@app.route('/chatweb', methods=['POST'])
def chatweb():
    input_json = request.get_json(force=True) 
    incoming_msg = str(input_json['response'])
    print("session: ")
    print(session)
    print()
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    dictToReturn = {
        "answer": answer,
        "chat_log": session['chat_log']
    }
    return jsonify(dictToReturn)

@app.route('/clear', methods=['GET'])
def clear_session():
    session['chat_log'] = None
    session['start'] = None
    session['end'] = None
    session['arm_no'] = None
    session["start"] = None
    return "cleared!"

@app.route('/end', methods=['GET'])
def end():
    session['end'] = True
    return "ended!"

@app.route('/arm', methods=['GET'])
def select_arm():
    args = request.args
    location = int(args['location'])
    if location == 12345:
        arm_no = 0
    elif location == 23456:
        arm_no = 1
    elif location == 34567:
        arm_no = 2
    elif location == 45678:
        arm_no = 3
    elif location == 56789:
        arm_no = 4
    elif location == 67891:
        arm_no = 5
    elif location == 78910:
        arm_no = 6
    elif location == 89101:
        arm_no = 7
    elif location == 91011:
        arm_no = 8
    elif location == 10111:
        arm_no = 9
    elif location == 11121:
        arm_no = 10
    elif location == 12131:
        arm_no = 11
    elif location == 13141:
        arm_no = 12
    elif location == 14151:
        arm_no = 13
    elif location == 15161:
        arm_no = 14
    elif location == 16171:
        arm_no = 15
    elif location == 17181:
        arm_no = 16
    elif location == 18192:
        arm_no = 16
    session['arm_no'] = arm_no
    return redirect(url_for('start_qualtrics_conversation'))
    # input_json = request.get_json(force=True)
    # if 'arm' not in input_json:
    #     return "Arm not found", 400
    # arm_no = int(input_json['arm'])
    # session['arm_no'] = arm_no
    # return jsonify(init_prompt(arm_no=arm_no)), 200
