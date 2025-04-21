# AbroadMates-Chatbot
Abroadmates AI is a smart chatbot that helps students get answers about studying abroad—covering visas, tuition, scholarships, and more. Built with Rasa, it’s your AI-powered study abroad assistant with plans for avatar chat, document uploads, and personalized advice.


# Abroadmates AI Chatbot

Abroadmates AI is an intelligent chatbot built with **Rasa** that helps students navigate their study abroad journey. From visa requirements to university selection, the bot answers questions and supports students in making informed decisions.

## Features

- Built with **Rasa** for natural language understanding
- Answers queries on:
  - Visa requirements
  - Accommodation
  - Universities
  - Tuition fees
  - Scholarships
  - Part-time jobs
  - Internships
  - Campus life
  - Health insurance
  - And more!
- Integrates with a **custom web frontend**
- Deployed via subdomain: `chatbot.abroadmates.com` (Planned)
- Future plans:
  - Avatar-based interactive chat experience
  - Document upload & organization
  - Personalized student assistant

## Project Structure

```bash
Abroadmates_Chatbot/
├── actions/                  # Custom Python actions (e.g., for LLaMA or web search)
├── data/                     # NLU data and stories
│   ├── nlu.yml
│   └── rules.yml
├── domain.yml                # Intents, responses, and actions
├── config.yml                # Rasa pipeline and policies
├── credentials.yml           # Channels and credentials
├── endpoints.yml             # Webhook endpoints
├── index.html                # Simple HTML frontend for chatbot UI
├── static/                   # (Optional) Any assets like logo, stylesheets
├── server.py                 # (Optional) Python server to host the chatbot frontend
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
