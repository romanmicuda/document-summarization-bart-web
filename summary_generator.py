# summary_generator.py
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from pathlib import Path

class SummaryGenerator:
    def __init__(self, model_path="best_model.pt"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(self.device)
        
        # Load trained weights
        if Path(model_path).exists():
            self.model.load_state_dict(torch.load(model_path, map_location=self.device))
            print(f"Loaded trained model weights from {model_path}")
        else:
            print("Using pretrained weights (no fine-tuning)")
        
        self.model.eval()
    
    def summarize(self, text, max_length=150, min_length=40):
        inputs = self.tokenizer(
            text,
            max_length=1024,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        ).to(self.device)
        
        summary_ids = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)