from dotenv import load_dotenv
from random import choice
import os
import openai

from typing import Dict

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

MESSAGE_START = "\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How are you doing today?"

def _init_prompt_behavior(arm_no: int=0, random: bool=False) -> Dict:
    arm_default = {
        "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach has strong interpersonal skills.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    arm_1 = {
        "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach is optimistic, flexible, and empathetic.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    arm_2 = {
        "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach is trustworthy, is an active listener, and is empathetic. The coach offers supportive and helpful attention, with no expectation of reciprocity.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    
    if random:
        return choice([arm_default, arm_1, arm_2])
    if arm_no == 1:
        return arm_1
    if arm_no == 2:
        return arm_2
    return arm_default


def _init_prompt_identity(arm_no: int=0, random: bool=False) -> Dict:
    arm_default = {
        "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach has strong interpersonal skills.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    arm_1 = {
        "prompt": "The following is a conversation with a friend. The friend asks open-ended reflection questions and helps the Human develop coping skills. The friend has strong interpersonal skills.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    arm_2 = {
        "prompt": "The following is a conversation with a mental health professional. The mental health professional asks open-ended reflection questions and helps the Human develop coping skills. The mental health professional has strong interpersonal skills.",
        "message_start": MESSAGE_START,
        "chatbot": "AI"
    }
    
    if random:
        return choice([arm_default, arm_1, arm_2])
    if arm_no == 1:
        return arm_1
    if arm_no == 2:
        return arm_2
    return arm_default


def _init_prompt_field(arm_no: int=0, random: bool=False) -> Dict:
    arms = [
        # arm 0 
        {
            "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 1
        {
            "prompt": "The following is a conversation with a friend. The friend asks open-ended reflection questions and helps the Human develop coping skills. The friend has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 2
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the coach helps the Human replace them with more realistic beliefs. The coach has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 3
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the friend helps the Human replace them with more realistic beliefs. The friend has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 4
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The coach has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 5
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The friend has strong interpersonal skills.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 6
        {
            "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach is trustworthy, is an active listener, and is empathetic. The coach offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 7
        {
            "prompt": "The following is a conversation with a friend. The friend asks open-ended reflection questions and helps the Human develop coping skills. The friend is trustworthy, is an active listener, and is empathetic. The friend offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 8
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the coach helps the Human replace them with more realistic beliefs. The coach is trustworthy, is an active listener, and is empathetic. The coach offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 9
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the friend helps the Human replace them with more realistic beliefs. The friend is trustworthy, is an active listener, and is empathetic. The friend offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 10
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The coach is trustworthy, is an active listener, and is empathetic. The coach offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 11
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The friend is trustworthy, is an active listener, and is empathetic. The friend offers supportive and helpful attention, with no expectation of reciprocity.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 12
        {
            "prompt": "The following is a conversation with a coach. The coach asks open-ended reflection questions and helps the Human develop coping skills. The coach is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 13
        {
            "prompt": "The following is a conversation with a friend. The friend asks open-ended reflection questions and helps the Human develop coping skills. The friend is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 14
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the coach helps the Human replace them with more realistic beliefs. The coach is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 15
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human understand how their thoughts, feelings, and behaviors influence each other. If the Human demonstrates negative thoughts, the friend helps the Human replace them with more realistic beliefs. The friend is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 16
        {
            "prompt": "The following is a conversation with a coach. The coach helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The coach is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 17
        {
            "prompt": "The following is a conversation with a friend. The friend helps the Human define their personal problems, generates multiple solutions to each problem, helps select the best solution, and develops a systematic plan for this solution. The friend is optimistic, flexible, and empathetic.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        }
    ]
    
    if random:
        return choice(arms)
    if arm_no < len(arms):
        return arms[arm_no]
    return arms[0]


def _init_prompt_field_psyc(arm_no: int=0, random: bool=False) -> Dict:
    arms = [
        # arm 0 
        {
            "prompt": "The following is a conversation with a client-centered therapist. The client-centered therapist provides the conditions for the human to express their own inherent growth tendency and self-realization. The client-centered therapist empathizes with the human and empowers the human to pursue his own goals in a nondirective way.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 1
        {
            "prompt": "The following is a conversation with a psychoanalyst. The psychoanalyst facilitates awareness of unconscious motivations, thereby increasing choice. The psychoanalyst explores the ways in which the human avoids painful or threatening feelings, fantasies, and thoughts. The psychoanalyst makes reflections and interpretations to make the human more aware of unconscious experiences and relational patterns. The psychoanalyst pays attention to the therapeutic relationship, including transference and countertransference.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        },
        # arm 2
        {
            "prompt": "The following is a conversation with a cognitive-behavioral therapist. The cognitive-behavioral therapist aims to help the human think about situations in more balanced, helpful ways and promote behavioral flexibility. The cognitive-behavioral therapist highlights the relations among thoughts, behaviors, and feelings. The cognitive-behavioral therapist uses Socratic questioning to uncover core beliefs. The cognitive-behavioral therapist encourages the human to restructure negative automatic thoughts to be more helpful, and to approach situations that elicit anxiety rather than avoiding them.",
            "message_start": MESSAGE_START,
            "chatbot": "AI"
        }
    ]
    
    if random:
        return choice(arms)
    if arm_no < len(arms):
        return arms[arm_no]
    return arms[0]
    

def init_prompt(arm_no: int=0, random: bool=False) -> Dict:
    return _init_prompt_field_psyc(arm_no, random)


class Conversation:
    CONVO_START = MESSAGE_START
    BOT_START = "Hello. I am an AI agent designed to help you manage your mood and mental health. How can I help you?"
    USER = "Human"
    CHATBOT = "AI"
    WARNING = "Warning"
    END = "End"
    NOTI = "Notification"
    
    def __init__(self, user: str, chatbot: str, chat_log: str) -> None:
        self.user_name = user
        self.chatbot_name = chatbot
        self.chat_log = chat_log
        self.prompt = chat_log.split(self.CONVO_START)[0]
    
    def get_user(self) -> str:
        return self.user_name
    
    def get_chatbot(self) -> str:
        return self.chatbot_name
    
    def get_conversation(self, end: bool=False, test: bool=False) -> Dict:
        chat_log_clean = self.chat_log.split("".join([self.prompt, self.CONVO_START]))[1]
        dialogs = chat_log_clean.split("\n\n")
        
        converation = []
        converation.append({
            "from": self.chatbot_name,
            "to": self.user_name,
            "message": self.BOT_START,
            "send_time": None
        })

        for i in range(1, len(dialogs)):
            messages = dialogs[i].split("\n")
            
            for message in messages:
                identifier_message = message.split(":")
                from_identity = identifier_message[0].strip()
                convo_message = identifier_message[1].strip()
                
                if from_identity == self.USER:
                    convo = {
                        "from": self.user_name,
                        "to": self.chatbot_name,
                        "message": convo_message,
                        "send_time": None
                    }
                else:
                    convo = {
                        "from": self.chatbot_name,
                        "to": self.user_name,
                        "message": convo_message,
                        "send_time": None
                    }

                converation.append(convo)
        
        return converation


class GPTConversation(Conversation):
    CONFIGS = {
        "engine": "text-davinci-002",
        "temperature": 0.9,
        "max_tokens": 300,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6,
    }
    
    def __init__(self, user: str, chatbot: str, chat_log: str) -> None:
        super().__init__(user, chatbot, chat_log)
        
        self.start_sequence = f"\n{self.CHATBOT}:"
        self.restart_sequence = f"\n\n{self.USER}: "
    
    def ask(self, question: str) -> str:
        prompt_text = f"{self.chat_log}{self.restart_sequence}{question}{self.start_sequence}"
        response = openai.Completion.create(
            prompt=prompt_text,
            stop=[" {}:".format(self.USER), " {}:".format(self.CHATBOT)],
            **self.CONFIGS
        )
        
        story = response['choices'][0]['text']
        # print(f"{'=' * 12} CHECKING STORY {'=' * 12}")
        # print(story)
        # print(f"{'-' * 12} ANSWER {'-' * 12}")
        answer = str(story).strip().split(self.restart_sequence.rstrip())[0]
        # print(answer)
        # print(f"{'=' * 12} CHECKING STORY END {'=' * 12}")
        
        return answer
    
    def append_interaction_to_chat_log(self, question: str, answer: str) -> str:
            return f"{self.chat_log}{self.restart_sequence}{question}{self.start_sequence} {answer}".strip()
    
    def get_conversation(self, end: bool=False, test: bool=False) -> Dict:
        chat_log_clean = self.chat_log.split("".join([self.prompt, self.CONVO_START]))[1]
        dialogs = chat_log_clean.split(self.restart_sequence)
        
        converation = []
        
        if test:
            converation.append({
                "from": self.chatbot_name,
                "to": self.WARNING,
                "message": self.prompt,
                "send_time": None
            })
        
        converation.append({
            "from": self.chatbot_name,
            "to": self.user_name,
            "message": self.BOT_START,
            "send_time": None
        })
        
        for i in range(1, len(dialogs)):
            messages = dialogs[i].split(self.start_sequence)
            
            for msg_idx in range(len(messages)):
                if msg_idx == 0:
                    from_idt = self.user_name
                    to_idt = self.chatbot_name
                else:
                    to_idt = self.user_name
                    from_idt = self.chatbot_name
                
                convo = []
                for text in messages[msg_idx].split("\n"):
                    if len(text) != 0:
                        convo.append({
                            "from": from_idt,
                            "to": to_idt,
                            "message": text.strip(),
                            "send_time": None
                        })
                converation.extend(convo)
        
        if end:
            converation.append({
                "from": self.chatbot_name,
                "to": self.END,
                "message": "This conversation is ended. Your username is the secret key, which you have to paste in the previous survey window.",
                "send_time": None
            })
            converation.append({
                "from": self.chatbot_name,
                "to": self.END,
                "message": "To copy the secret key (i.e. username), you can click the blue button on the bottom left of your screen.",
                "send_time": None
            })
            
        return converation
        
