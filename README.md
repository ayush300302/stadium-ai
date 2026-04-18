# StadiumAI - Smart Physical Event Experience

## Vertical Chosen: Physical Event Experience
This project was created to enhance the fan experience at large sports venues and events by providing a smart, responsive assistant.

## The Problem
Navigating a massive stadium can be confusing. Fans often struggle to find food stalls with the shortest queues, locate their seats or specific gates, stay updated on crowd levels, or find emergency assistance quickly.

## The Solution: StadiumAI
StadiumAI is an intelligent assistant built to solve these problems. It provides real-time, interactive help to fans directly on their phones.

## How it Works
The application uses a conversational AI interface built with Streamlit and powered by the **Gemini API**. It processes fan queries based on a structured system prompt that includes instructions on navigation, food queues, crowd control, and emergency protocols. 

### Core Features:
- **Food & Queues**: Recommends stalls and shortest queues.
- **Navigation**: Provides step-by-step guidance to seats and gates.
- **Crowd Information**: Offers advice on avoiding congested areas.
- **Emergency Help**: Directs fans to safety and medical personnel.
- **Event Schedule**: Keeps fans informed about match timings and shows.

## Google Services Used
- **Gemini API (gemini-2.5-flash)**: Acts as the brain of the assistant, understanding user queries and generating helpful, context-aware responses.

## Assumptions Made
- The assistant is provided to fans via a mobile-friendly web interface or kiosk.
- Real-time queue and crowd data would ideally be fed into the system in a production environment; currently, the AI simulates this based on its context instructions.

## How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your Gemini API key in a `.env` file: `GEMINI_API_KEY=your_key_here`
4. Run the app: `streamlit run app.py`
