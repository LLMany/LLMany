import {CHAT_GPT, CLAUDE, GEMINI, MODEL_MESSAGE, USER_MESSAGE} from "./constants";

export const placeholderMessages = [
    { owner: USER_MESSAGE, content: "Hello World!" },
    { owner: MODEL_MESSAGE, content: "Hi!" },
]

export const placeholderChats = [
    { model: CHAT_GPT, chatID: 1000 },
    { model: GEMINI, chatID: 1001 },
    { model: CHAT_GPT, chatID: 2000 },
    { model: CLAUDE, chatID: 1015 },
]