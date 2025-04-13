import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Chatbot:
    def __init__(self):
        # Load the DialoGPT model and tokenizer
        model_name = "microsoft/DialoGPT-medium"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None

    def generate_response(self, user_input):
        try:
            # Tokenize user input and append to chat history
            new_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')
            
            if self.chat_history_ids is None:
                self.chat_history_ids = new_input_ids
            else:
                self.chat_history_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)

            # Generate chatbot response
            response_ids = self.model.generate(self.chat_history_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
            response = self.tokenizer.decode(response_ids[:, self.chat_history_ids.shape[-1]:][0], skip_special_tokens=True)
            
            return response
        except Exception as e:
            return f"❗ Sorry, I encountered an error: {str(e)}"
