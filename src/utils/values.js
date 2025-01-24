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
        color: "rgb(116, 170, 156)",
        icon: "",
    }
);

const GeminiDetails = new ModelDetails(
    {
        displayName: "Gemini",
        provider: "Google",
        color: "rgb(71, 150, 227)",
        icon: "",
    }
);

const ClaudeDetails = new ModelDetails(
    {
        displayName: "Claude",
        provider: "Anthropic",
        color: "rgb(218, 119, 86)",
        icon: "",
    }
);

const HuggingFaceDetails = new ModelDetails(
    {
        displayName: "HuggingFace",
        provider: "Qwen",
        color: "rgb(254, 210, 57)",
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
