# Task_06_Deep-Fake

# AI-Generated Sports Podcast

Hey there! Welcome to my little corner of the web where I've taught a computer to be a sports analyst. This project uses AI to take raw Olympic sports data, analyze it for cool insights, and then turn those insights into a full "deepfake" podcast interview.

The whole thing is an experiment to see how far we can push modern AI tools in a creative pipeline.

---

## What's Going On Here?

This project is a multi-step journey from a simple data file to a finished audio interview:

1.  **AI Data Analyst**: The process starts with a CSV file full of historical Olympic data. We use Google's Gemini AI to dynamically ask interesting questions about the data and then write Python code to answer them.
    
2.  **AI Scriptwriter**: Once we have our interesting facts (like "who won the most medals?" or "what's the average age of a gold medalist?"), we feed all of that to Gemini again. This time, we ask it to act like a podcast scriptwriter, creating a natural-sounding conversation between a host and a data expert.
    
3.  **AI Voice Actors**: With the script in hand, we use the ElevenLabs API to generate realistic voices for our host and expert. Each line of the script is converted into an audio snippet.
    
4.  **Audio Production**: Finally, we use Python to stitch all the little audio snippets together into a single, seamless MP3 file that sounds like a real podcast conversation.

---

## Tools & Technologies Used 🛠️

This project is built by standing on the shoulders of some amazing tools and technologies. Here's a quick rundown of what's under the hood:

* **Python**: The backbone of the whole project, used to write all the logic that connects the different services.

* **Google Gemini**: The 'brain' of the operation. It acts as both the **data analyst** that figures out what's interesting in the data and the **creative scriptwriter** that turns those facts into a conversation.

* **ElevenLabs**: The 'voice' of the project. This service provides the realistic, human-like AI voices for our podcast host and expert.

* **Pandas**: A workhorse library for data handling. We use it to read the initial Olympic CSV file and get it ready for analysis.

* **Pydub**: The project's 'audio engineer'. This handy library takes all the individual audio clips from ElevenLabs and stitches them together into one seamless MP3 file.

* **FFmpeg**: A crucial behind-the-scenes helper. Pydub needs this powerful audio-video processing tool to do its magic with MP3 files.

---

## How to Run This Thing

If you want to try this out yourself, here's the basic idea:

1.  **Get Your Data**: You'll need the `athlete_events.csv` file. You can find this dataset on Kaggle.
2.  **Set Up Your Keys**: This project needs API keys for both Google Gemini and ElevenLabs. You'll need to plug those into the Python script.
3.  **Install the Goodies**: You'll need a few Python libraries to get going. You can install them with pip:
    
    ```bash
    pip install pandas google-generativeai elevenlabs pydub
    ```
4.  **Run the Script**: Just run the main Python file. It'll handle everything from analyzing the data to spitting out the final `conversation.mp3`.
    
    ```bash
    python your_script_name.py
    ```

---

## My Big Takeaway

This was a super fun project that showed me how different AI models can be chained together to create something cool. It's one thing to have an AI answer a question, but it's another thing entirely to have it tell a story with data and then give that story a voice. Hope you enjoy it!

This was a super fun project that showed me how different AI models can be chained together to create something cool. It's one thing to have an AI answer a question, but it's another thing entirely to have it tell a story with data and then give that story a voice. Hope you enjoy it!
