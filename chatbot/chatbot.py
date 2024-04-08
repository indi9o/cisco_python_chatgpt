import os
from openai import OpenAI
from dotenv import load_dotenv

# Muat variabel lingkungan dari file .env
load_dotenv()

# Tetapkan variabel api_key dari variabel lingkungan
api_key = os.getenv("OPENAI_API_KEY")

# Buat instance dari kelas OpenAI dengan api_key
client = OpenAI(api_key=api_key)

# Masukkan loop yang tidak terbatas yang meminta pengguna untuk pertanyaan
while True:
    question = input('Apa pertanyaan Anda (ketik "quit" untuk keluar): ')

    # Keluarkan loop jika pengguna mengetik "quit"
    if question.lower() == 'quit':
        break

    # Buat permintaan completions ke API OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Anda adalah chatbot yang berspesialisasi dalam jaringan Cisco. Ingatlah untuk selalu menggunakan bahasa dan terminologi Cisco dalam penjelasan Anda."},
            {"role": "user", "content": f"{question}"},
            {"role": "assistant", "content": "Sebagai asisten yang berfokus pada Cisco, saya dapat membantu Anda dengan pertanyaan terkait konfigurasi jaringan, produk Cisco, pemecahan masalah, dan banyak lagi."}
        ]
    )

    # Ekstrak respons dari model GPT-3
    result = ''
    for choice in response.choices:
        result += choice.message.content

    # Cetak respons ke konsol
    print(f"Kami bertanya kepada ChatGPT: {question} - Berikut adalah jawabannya:")
    print("---------------------------------------------------------")
    print(result)