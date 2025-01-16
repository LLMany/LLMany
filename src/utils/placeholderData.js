import {CHAT_GPT, CLAUDE, GEMINI, MODEL_MESSAGE, USER_MESSAGE} from "./constants";

export const placeholderMessages = [
    { owner: USER_MESSAGE, content: "Hello World!" },
    { owner: MODEL_MESSAGE, content: "Hi!" },
]

export const placeholderChats = [
    { model: CHAT_GPT, chat_id: 1000 },
    { model: GEMINI, chat_id: 1001 },
    { model: CHAT_GPT, chat_id: 2000 },
    { model: CLAUDE, chat_id: 1015 },
]