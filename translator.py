import os
import whisper

class AudioTranslator:
    def input_file(self, file_path):
        self.file_path = file_path
        # self.file_title = file_path.split(".mkv")[0]
        self.file_title = file_path.strip('.mkv')

        print(f'inputted audio file: {self.file_path}')
        return self.file_path

    def use_whisper(self, model_size='base'):
        model = whisper.load_model(model_size)
        text_file_name = f"{self.file_title}.txt"

        if not os.path.exists(text_file_name):
            result = model.transcribe(self.file_path)
            with open(text_file_name, "w", encoding="utf-8") as txt:
                txt.write(result["text"])
        
        return text_file_name