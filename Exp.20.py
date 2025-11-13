#1. Audio bisualization....

# import soundfile as sf
# # Load audio file
# audio, sample_rate = sf.read(r'C:\Users\Administrator\Desktop\Hackey_18\PWP\Class_Test\LMLYD.mp3')

# # Write audio file
# sf.write('new_audio_file.wav', audio, sample_rate)

# import matplotlib.pyplot as plt
# import numpy as np
# # Load audio file
# #audio, sample_rate = sf.read('audio_file.wav')
# time = np.arange(0, len(audio)) / sample_rate
# plt.plot(time, audio)
# plt.title('Sine Signal of 44 LMLYD.mp3')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()

#2. Audio Effects...

from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file('audio.wav')

# Add fade in effect
audio_fade_in = audio.fade_in(2000)  # 2 seconds

# Export audio file with fade in effect
audio_fade_in.export('audio_file_fade_in', format='wav')