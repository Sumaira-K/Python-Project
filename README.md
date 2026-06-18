# AI Chat Automation Bot

An intelligent automation tool that uses OpenAI's GPT API to automatically respond to chat messages. This project combines browser automation with AI to provide real-time, context-aware responses in chat applications.

## Features

- **AI-Powered Responses** - Uses OpenAI's GPT-3.5 Turbo to generate intelligent replies
- **Browser Automation** - Automatically interacts with chat applications using PyAutoGUI
- **Clipboard Integration** - Extracts chat history and pastes responses seamlessly
- **Cursor Position Detection** - Utility to find exact coordinates for automation

## Project Structure

- **`1. get_cursor.py`** - Utility script to get current mouse cursor position (helps find coordinates for automation)
- **`2. open_ai.py`** - OpenAI API integration template with example usage
- **`3. bot.py`** - Main automation script that orchestrates the chat automation workflow

## Requirements

- pyautogui
- openai
- pyperclip

## How It Works

- Capture Chat History - Uses PyAutoGUI to select and copy chat messages
- Parse Messages - Extracts the message history from clipboard
- Generate Response - Sends chat history to OpenAI API for response generation
- Send Reply - Automatically pastes and sends the AI-generated response
