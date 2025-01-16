import {useState} from "react";
import {CHAT_GPT, CLAUDE, GEMINI, HUGGING_FACE} from "./constants";
import ModelList from "../components/ModelList";



class ModelDetails {
    constructor(props) {
        this.displayName = props.displayName;
        this.provider = props.provider;
        this.color = props.color;
        this.icon = props.icon;
    }
}


const ChatGPTDetails = new ModelDetails(
    {
        displayName: "Chat GPT",
        provider: "OpenAI",
        color: "green",
        icon: "",
    }
);

const GeminiDetails = new ModelDetails(
    {
        displayName: "Gemini",
        provider: "Google",
        color: "blue",
        icon: "",
    }
);

const ClaudeDetails = new ModelDetails(
    {
        displayName: "Claude",
        provider: "Anthropic",
        color: "orange",
        icon: "",
    }
);

const HuggingFaceDetails = new ModelDetails(
    {
        displayName: "HuggingFace",
        provider: "Qwen",
        color: "green",
        icon: "",
    }
)


export const modelMap = {
    [CHAT_GPT]: ChatGPTDetails,
    [GEMINI]: GeminiDetails,
    [CLAUDE]: ClaudeDetails,
    [HUGGING_FACE]: HuggingFaceDetails,
}

export const modelList = [
    CHAT_GPT,
    GEMINI,
    CLAUDE,
    HUGGING_FACE
];
