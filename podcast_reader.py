from audio import YoutubeVideo
from translator import AudioTranslator
from summarizer import Summarizer

podcast_audio = YoutubeVideo("@yutinghao")
podcast_audio.download_video()
audio_file = podcast_audio.get_video_path()

translator = AudioTranslator()
translator.input_file(audio_file)
text = translator.use_whisper()

# chatgpt = Summarizer()
# response = chatgpt.read_text(text)