import {useState} from "react";
import {CHAT_GPT, CLAUDE, GEMINI} from "./constants";
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
        provider: "Amazon",
        color: "orange",
        icon: "",
    }
);


export const modelMap = {
    [CHAT_GPT]: ChatGPTDetails,
    [GEMINI]: GeminiDetails,
    [CLAUDE]: ClaudeDetails,
}

export const modelList = [
    CHAT_GPT,
    GEMINI,
    CLAUDE
];
