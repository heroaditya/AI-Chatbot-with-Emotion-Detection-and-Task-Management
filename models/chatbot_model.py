import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import CHATBOT_MODEL
from task_manager import TaskManager

class Chatbot:
    def __init__(self):
        # Load pre-trained DialoGPT model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(CHATBOT_MODEL)
        self.model = AutoModelForCausalLM.from_pretrained(CHATBOT_MODEL)
        self.task_manager = TaskManager()

    def generate_response(self, user_input, chat_history=None):
        try:
            if chat_history is None:
                chat_history = []

            # ** Check for Task or Reminder Keywords **
            if any(keyword in user_input.lower() for keyword in ["remind", "set a task", "schedule", "add task"]):
                task_text = user_input.replace("remind me to", "").replace("set a task", "").strip()
                if task_text:
                    self.task_manager.add_task(task_text)
                    return f"✅ Task added: '{task_text}'", chat_history
                else:
                    return "⚠️ Please specify the task or reminder.", chat_history

            new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')
            bot_input_ids = torch.cat([torch.tensor(chat_history), new_user_input_ids], dim=-1) if chat_history else new_user_input_ids

            response_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
            response = self.tokenizer.decode(response_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

            # Update chat history
            chat_history.extend(new_user_input_ids[0].tolist())
            chat_history.extend(response_ids[0].tolist())

            return response  # Only return the response, not the token IDs
        except Exception as e:
            print(f"Error in generating response: {e}")
            return "I'm sorry, something went wrong."


# Example Usage (Optional for testing)
if __name__ == "__main__":
    chatbot = Chatbot()
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        response, chat_history = chatbot.generate_response(user_input, chat_history)
        print(f"Chatbot: {response}")
